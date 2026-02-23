#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import sys
from pathlib import Path

import modules.arguments as MainArgs
import modules.bing as Bing
import modules.today as Today

# 样式信息
sources_folder = Path(__file__).parent / "sources"

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
    greeting: str, today_simple_date, today_weekday, today_zhdate, header_image
):
    print("Generating the header of NewsPhoto...")

    # 获取头图的绝对路径，转换为 POSIX 格式
    header_image_url = Path(header_image).resolve().as_posix()
    # 写入头文件：header.md
    header_text = [
        "<header>  \n\n",
        f"![News Photo]({header_image_url} 'header_image')  \n\n",
        "</header>  \n\n",
        "<section>  \n\n",
        f"## {today_simple_date} · {today_weekday} · {today_zhdate}\n\n",
        f"【 {greeting} 】\n\n",
    ]  # fmt: skip

    return "".join(header_text)


# 函数：生成正文新闻
def write_content_md(file_path: Path):
    print("Generating the main content of NewsPhoto...")
    # 处理正文文本 news.txt，写入到新的正文文件：content.md
    try:
        with open(file_path, "r", encoding="utf_8") as a:
            text = a.read()
    except Exception as e:
        print(f"Error occurred while reading {file_path}: {e}")
        sys.exit(1)

    content_text = text.replace("\n", "  \n\n") + "\n\n"

    return content_text


# 函数：生成底部内容
def write_footer_md(style, bing_title, today_full_date, timezone):
    print("Generating the footer of NewsPhoto...")
    # 判断当前使用的样式，决定使用何种样式的二维码
    style_info = style_map.get(style)
    qrcode_file = sources_folder / "images" / style_info.get("qrcode")

    # 获取二维码的绝对路径，转换为 POSIX 格式
    qrcode_file_url=Path(qrcode_file).resolve().as_posix()
    # 写入底部文件：footer.md
    footer_text = [
        "</section>  \n\n",
        "<footer>  \n\n",
        f"**{bing_title[0]}**<br>",
        f"**{bing_title[1]}**  \n\n",
        f"> 更新于: {today_full_date} / {timezone}<br>",
        f"修订于: {today_full_date} / {timezone}  \n\n",
        f"![qrcode]({qrcode_file_url} 'qrcode')  \n\n",
        "</footer>",
    ]

    return "".join(footer_text)


# 函数：使用 Pandoc 导出文档
def convert_with_pandoc(input_file, output_file, style):
    print("Converting NewsPhoto to HTML with Pandoc...")
    # 判断当前使用的样式，决定使用何种样式表
    style_info = style_map.get(style)
    style_file = sources_folder / "styles" / style_info.get("stylesheet")

    # 获取样式表的绝对路径，转换为 POSIX 格式
    style_file_url = Path(style_file).resolve().as_posix()

    # 运行 pandoc --version 检测 Pandoc 安装状态
    try:
        subprocess.run(
            ["pandoc", "--version"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
    except Exception:
        print("We cannot find Pandoc, please install it from https://pandoc.org.")
        sys.exit(1)

    # 运行 Pandoc 转换
    try:
        subprocess.run(
            [
                "pandoc",
                "--metadata",
                "title=NewsPhoto",
                "--embed-resources",
                "--standalone",
                f"--css={style_file_url}",
                f"{input_file}",
                f"--output={output_file}",
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
    except Exception as e:
        print(f"Error occurred while converting with Pandoc: {e}")
        sys.exit(1)


# 主函数
def main():
    try:
        # 获取所有命令行参数
        parser = MainArgs.get_parser()
        args = parser.parse_args()

        # 获取基础路径
        if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
            base_path = Path(sys.executable).parent
        else:
            base_path = Path(__file__).parent

        # 检查导出目录是否存在，存在则清空，不存在则创建
        output_dir = base_path / "outputs"
        if not output_dir.exists():
            print("Creating output folder...")
            output_dir.mkdir()
        else:
            print("Cleaning up output folder...")
            for filename in output_dir.iterdir():
                file_path = output_dir / filename
                file_path.unlink()

        print("\nPreparing necessary info...")
        # 获取所需要的日期时间值
        today_timezone = Today.get_timezone()
        today_simple_date = Today.get_simple_date()
        today_full_date = Today.get_full_date()
        today_weekday = Today.get_weekday()
        today_zhdate = Today.get_zh_date()

        # 获取必应图片
        json_data = Bing.get_bing_json()
        bing_title = Bing.get_bing_title(json_data)

        bing_image_path = output_dir / "photo.jpg"
        Bing.get_bing_image(json_data, save_path=bing_image_path)

        # 生成 NewsPhoto.md 的各个部分
        header = write_header_md(
            greeting=args.greeting,
            today_simple_date=today_simple_date,
            today_weekday=today_weekday,
            today_zhdate=today_zhdate,
            header_image=bing_image_path,
        )
        content = write_content_md(file_path=args.news_file)
        footer = write_footer_md(
            style=args.style,
            bing_title=bing_title,
            today_full_date=today_full_date,
            timezone=today_timezone,
        )

        # 汇总后综合写入 NewsPhoto.md
        print("\nGenerating NewsPhoto...")
        newsphoto_md_path = output_dir / "NewsPhoto.md"
        with open(newsphoto_md_path, "a", encoding="utf_8") as newsphoto_md:
            newsphoto_md.write(header + content + footer)

        # 将 Markdown 文档转换为 HTML 格式
        newsphoto_html_path = output_dir / "NewsPhoto.html"
        convert_with_pandoc(
            input_file=newsphoto_md_path,
            output_file=newsphoto_html_path,
            style=args.style,
        )
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting...")
        sys.exit(130)
    except Exception as e:
        print(f"Error occurred while generating NewsPhoto: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
