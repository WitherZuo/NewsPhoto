# coding=utf-8
from modules.today import get_simple_date, get_full_date, get_weekday, get_zh_date
from modules.bing import get_bing_json, get_bing_title, get_bing_image
from modules.arguments import parser
import os, pangu, re, subprocess

# 获取所有命令行参数
args = parser.parse_args()


# 函数：写入头文件 header.md
def write_header_md(greeting: str, today_simple_date, today_weekday, today_zhdate):
    # 写入头文件：header.md
    header_text = [
        "<header>  \n\n",
        "![News Photo](sources/images/photo.jpg)  \n\n",
        "</header>  \n\n",
        "<section>  \n\n",
        f"## {today_simple_date} · {today_weekday} · {today_zhdate}\n\n",
        f"【 {greeting} 】\n\n",
    ]  # fmt: skip

    f = open("sources/header.md", "w", encoding="utf_8")
    f.writelines(header_text)
    f.close()


# 函数：写入正文文件 content.md
def write_content_md(file_path: str):
    # 处理正文文本 news.txt，写入到新的正文文件：content.md
    a = open(file_path, "r", encoding="utf_8")
    text = a.read()
    text_with_space = pangu.spacing(text)
    text_new = re.sub("\n", "  \n\n", text_with_space)

    b = open("sources/content.md", "w", encoding="utf_8")
    b.write(text_new + "\n\n")

    b.close()
    a.close()


# 函数：写入底部文件 footer.md
def write_footer_md(style, bing_title, today_full_date):
    # 判断当前使用的样式，决定使用何种样式的二维码
    if style == "light" or style == "dark":
        qrcode = '![qrcode](sources/images/qrcode.png "qrcode")'
    elif style == "springfestival":
        qrcode = '![qrcode](sources/images/qrcode-springfestival.png "qrcode")'

    # 写入底部文件：footer.md
    footer_text = [
        "</section>  \n\n",
        "<footer>  \n\n",
        f"**{bing_title[0]}**<br>",
        f"**{bing_title[1]}**  \n\n",
        f"> 最后更新: {today_full_date} / UTC+8<br>",
        f"最后修订: {today_full_date} / UTC+8  \n\n",
        f"{qrcode}  \n\n",
        "</footer>",
    ]

    c = open("sources/footer.md", "w", encoding="utf_8")
    c.writelines(footer_text)
    c.close()


# 函数：使用 Pandoc 导出文档
def convert_with_pandoc(style):
    # 判断当前使用的样式，决定使用何种样式表
    if style == "light":
        style_file = "sources/styles/light.css"
    elif style == "dark":
        style_file = "sources/styles/dark.css"
    elif style == "springfestival":
        style_file = "sources/styles/springfestival.css"

    subprocess.run(
        [
            "pandoc",
            "--metadata",
            "title=NewsPhoto",
            "--embed-resources",
            "--standalone",
            f"--css={style_file}",
            "sources/index.md",
            "--output=outputs/index.html",
        ]
    )  # fmt: skip


if __name__ == "__main__":
    # 清理过时文件
    outdated_files = [
        "sources/header.md",
        "sources/content.md",
        "sources/index.md",
        "sources/footer.md",
        "sources/images/photo.jpg",
        "outputs/index.html",
    ]
    for outdated_file in outdated_files:
        if os.path.exists(outdated_file):
            os.unlink(outdated_file)

    # 获取所需要的日期时间值
    today_simple_date = get_simple_date()
    today_full_date = get_full_date()
    today_weekday = get_weekday(today_full_date)
    today_zhdate = get_zh_date()

    # 获取必应图片
    json_data = get_bing_json()
    bing_title = get_bing_title(json_data)
    get_bing_image(json_data)

    # 生成 index.md 的各个部分
    write_header_md(
        greeting=args.greeting,
        today_simple_date=today_simple_date,
        today_weekday=today_weekday,
        today_zhdate=today_zhdate,
    )
    write_content_md(file_path=args.news_file)
    write_footer_md(
        style=args.style, bing_title=bing_title, today_full_date=today_full_date
    )

    # 汇总后综合写入 index.md
    index_md = open("sources/index.md", "a", encoding="utf_8")

    header_md = open("sources/header.md", "r", encoding="utf_8")
    content_md = open("sources/content.md", "r", encoding="utf_8")
    footer_md = open("sources/footer.md", "r", encoding="utf_8")

    header_source = header_md.read()
    content_source = content_md.read()
    footer_source = footer_md.read()

    index_md.write(header_source + content_source + footer_source)

    source_files = [header_md, content_md, footer_md, index_md]
    for sources_file in source_files:
        sources_file.close()

    # 将 Markdown 文档转换为 HTML 格式
    convert_with_pandoc(style=args.style)
