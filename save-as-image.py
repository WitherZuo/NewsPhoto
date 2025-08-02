# coding=utf-8
import argparse
from pathlib import Path
from playwright.sync_api import sync_playwright


def get_parser():
    """
    参数说明：
    -b, --browser：Playwright 运行调用的浏览器
    """
    parser = argparse.ArgumentParser(description="Save as image")
    parser.add_argument(
        "-b",
        "--browser",
        metavar="BROWSER",
        type=str,
        choices=["chromium", "firefox", "webkit", "msedge", "chrome"],
        default="chromium",
        help="The browser used for Playwright. (chromium | firefox | webkit | msedge | chrome, Default: chromium)",
    )
    return parser


# 函数：获取目标文件位置，为 URI 地址
def get_target_url(file_path: Path) -> str:
    return file_path.resolve().as_uri()


# 函数：检测目标文件是否存在，如果存在即删除
def delete_if_exists(path: Path):
    if path.exists():
        path.unlink()


# 函数：将页面保存为图片
def save_as_image(browser_name: str, html_path: Path, output_path: Path):
    url = get_target_url(html_path)
    print(f"Loading: {url}")

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

        if launch:
            if browser_name in ["chrome", "msedge"]:
                browser = launch(channel=browser_name, headless=True)
            else:
                browser = launch(headless=True)
        else:
            print(
                f"Unsupported browser: {browser_name}. Falling back to chromium."
            )
            browser = p.chromium.launch(headless=True)

        page = browser.new_page()
        page.goto(url)
        page.locator("body").screenshot(path=output_path, type="png")
        print(f"Page title: {page.title()}")
        browser.close()


# 主函数
def main():
    parser = get_parser()
    args = parser.parse_args()

    html_path = Path("outputs/NewsPhoto.html")
    image_path = Path("outputs/NewsPhoto.png")

    delete_if_exists(path=image_path)
    save_as_image(
        browser_name=args.browser, html_path=html_path, output_path=image_path
    )


if __name__ == "__main__":
    main()
