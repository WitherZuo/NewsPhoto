# coding=utf-8
import os
import re
import subprocess
import sys

import pangu

import modules.arguments as MainArgs
import modules.bing as Bing
import modules.today as Today

# 样式信息
style_map = {
    "light": {
        "qrcode": "qrcode-normal.png",
        "stylesheet": "light.css",
    },
    "dark": {
        "qrcode": "qrcode-normal.png",
        "stylesheet": "dark.css",
    },
    "springfestival": {
        "qrcode": "qrcode-springfestival.png",
        "stylesheet": "springfestival.css",
    },
}


# 函数：生成头部内容
def write_header_md(
    greeting: str, today_simple_date, today_weekday, today_zhdate
):
    # 写入头文件：header.md
    header_text = [
        "<header>  \n\n",
        "![News Photo](outputs/photo.jpg)  \n\n",
        "</header>  \n\n",
        "<section>  \n\n",
        f"## {today_simple_date} · {today_weekday} · {today_zhdate}\n\n",
        f"【 {greeting} 】\n\n",
    ]  # fmt: skip

    return header_text


# 函数：生成正文新闻
def write_content_md(file_path: str):
    # 处理正文文本 news.txt，写入到新的正文文件：content.md
    with open(file_path, "r", encoding="utf_8") as a:
        text = a.read()

    text_with_space = pangu.spacing(text)
    text_new = re.sub("\n", "  \n\n", text_with_space)
    content_text = text_new + "\n\n"

    return content_text


# 函数：生成底部内容
def write_footer_md(style, bing_title, today_full_date, timezone):
    # 判断当前使用的样式，决定使用何种样式的二维码
    style_info = style_map.get(style)
    qrcode = f"![qrcode](sources/images/{style_info.get('qrcode')} 'qrcode')"

    # 写入底部文件：footer.md
    footer_text = [
        "</section>  \n\n",
        "<footer>  \n\n",
        f"**{bing_title[0]}**<br>",
        f"**{bing_title[1]}**  \n\n",
        f"> 最后更新: {today_full_date} / {timezone}<br>",
        f"最后修订: {today_full_date} / {timezone}  \n\n",
        f"{qrcode}  \n\n",
        "</footer>",
    ]

    return footer_text


# 函数：使用 Pandoc 导出文档
def convert_with_pandoc(style):
    # 判断当前使用的样式，决定使用何种样式表
    style_info = style_map.get(style)
    style_file = f"sources/styles/{style_info.get('stylesheet')}"

    subprocess.run(
        [
            "pandoc",
            "--metadata",
            "title=NewsPhoto",
            "--embed-resources",
            "--standalone",
            f"--css={style_file}",
            "outputs/NewsPhoto.md",
            "--output=outputs/NewsPhoto.html",
        ]
    )  # fmt: skip


# 主函数
def main():
    # 获取所有命令行参数
    parser = MainArgs.get_parser()
    args = parser.parse_args()

    # 获取基础路径
    if "__compiled__" in globals():
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(__file__)

    # 检查导出目录是否存在，存在则清空，不存在则创建
    output_dir = os.path.join(base_path, "outputs")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    else:
        for filename in os.listdir(output_dir):
            file_path = os.path.join(output_dir, filename)
            os.remove(file_path)

    # 获取所需要的日期时间值
    today_timezone = Today.get_timezone()
    today_simple_date = Today.get_simple_date()
    today_full_date = Today.get_full_date()
    today_weekday = Today.get_weekday(today_full_date)
    today_zhdate = Today.get_zh_date()

    # 获取必应图片
    json_data = Bing.get_bing_json()
    bing_title = Bing.get_bing_title(json_data)
    Bing.get_bing_image(json_data)

    # 生成 NewsPhoto.md 的各个部分
    header = write_header_md(
        greeting=args.greeting,
        today_simple_date=today_simple_date,
        today_weekday=today_weekday,
        today_zhdate=today_zhdate,
    )
    content = write_content_md(file_path=args.news_file)
    footer = write_footer_md(
        style=args.style,
        bing_title=bing_title,
        today_full_date=today_full_date,
        timezone=today_timezone,
    )

    # 汇总后综合写入 NewsPhoto.md
    newsphoto_md_path = os.path.join(output_dir, "NewsPhoto.md")
    with open(newsphoto_md_path, "a", encoding="utf_8") as newsphoto_md:
        newsphoto_md.writelines(header)
        newsphoto_md.write(content)
        newsphoto_md.writelines(footer)

    # 将 Markdown 文档转换为 HTML 格式
    convert_with_pandoc(style=args.style)


if __name__ == "__main__":
    main()
