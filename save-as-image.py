#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import os
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright


# 函数：获取命令行参数解析器
def get_parser():
    """
    参数说明：
    -b, --browser：Playwright 运行调用的浏览器
    """
    parser = argparse.ArgumentParser(description="News Photo: News Photo everyday!")
    parser.add_argument(
        "-b",
        "--browser",
        metavar="BROWSER",
        type=str,
        choices=("chromium", "firefox", "webkit", "msedge", "chrome"),
        default="chromium",
        help="The browser used for Playwright. (chromium* | firefox | webkit | msedge | chrome)",
    )
    return parser


# 函数：检测目标文件是否存在，如果存在即删除
def delete_if_exists(file_path: Path):
    print("Cleaning up output image...")
    try:
        if Path(file_path).exists():
            Path(file_path).unlink()
    except Exception as e:
        print(f"Error occurred while deleting file {file_path}: {e}")
        sys.exit(1)


# 函数：获取目标文件位置，为 URI 地址
def get_target_url(file_path: Path) -> str:
    print("- Getting NewsPhoto HTML...")
    # 检查目标文件是否存在，不存在则退出
    try:
        if file_path.resolve().exists():
            return file_path.resolve().as_uri()
        else:
            print(f"File not found: {file_path.resolve()}.")
            sys.exit(1)
    except Exception as e:
        print(f"Error occurred while getting target URL: {e}")
        sys.exit(1)


# 函数：将页面保存为图片
def save_as_image(browser_name: str, html_path: Path, output_path: Path):
    print("\nPreparing necessary info...")
    # 获取 NewsPhoto 页面
    url = get_target_url(html_path)

    # 检测浏览器
    print(r"- Checking browser(s)...")
    try:
        with sync_playwright() as p:
            # 浏览器映射表
            launchers = {
                "chromium": p.chromium.launch,
                "firefox": p.firefox.launch,
                "webkit": p.webkit.launch,
                "chrome": p.chromium.launch,
                "msedge": p.chromium.launch,
            }

            browser_name = browser_name.lower()
            launch = launchers.get(browser_name)

            # 识别浏览器
            if launch:
                if browser_name in ["chrome", "msedge"]:
                    browser = launch(channel=browser_name, headless=True)
                else:
                    browser = launch(headless=True)
            else:
                print(f"Unsupported browser: {browser_name}. Falling back to chromium.")
                browser = p.chromium.launch(headless=True)

            # 导出为图片
            print("\nGenerating NewsPhoto image...")
            # 加载 NewsPhoto 页面，生成 NewsPhoto 图片
            print(f"- Loading: {url}")
            page = browser.new_page()
            page.goto(url)
            page.locator("body").screenshot(path=output_path, type="png")
            print(f"{page.title()}")
            browser.close()
    except Exception as e:
        print(f"Error occurred while saving as image: {e}")
        sys.exit(1)


# 主函数
def main():
    try:
        # 获取命令行参数
        parser = get_parser()
        args = parser.parse_args()

        # 获取脚本的基础路径，设置 Playwright 浏览器标记
        if "__compiled__" in globals():
            base_path = Path(sys.argv[0]).parent
            os.environ["PLAYWRIGHT_BROWSERS_PATH"] = str(base_path / "browser")
        else:
            base_path = Path(__file__).parent

        # 获取基础路径
        output_dir = base_path / "outputs"
        html_path = output_dir / "NewsPhoto.html"
        image_path = output_dir / "NewsPhoto.png"

        # 生成图片
        delete_if_exists(file_path=image_path)
        save_as_image(
            browser_name=args.browser,
            html_path=html_path,
            output_path=image_path,
        )
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting...")
        sys.exit(130)
    except Exception as e:
        print(f"Error occurred while saving NewsPhoto as image: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
