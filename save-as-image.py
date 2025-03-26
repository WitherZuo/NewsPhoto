from playwright.sync_api import sync_playwright
import os
import argparse

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
    required=False,
    help="The browser used for Playwright. ( chromium | firefox | webkit | msedge | chrome, Default: chromium )",
)

"""
文件名 NewsPhoto.png，所在位置为 outputs 目录下，打印文件本地 URL
"""
file_name = "outputs/NewsPhoto.png"
url = "file:///" + os.getcwd() + r"\outputs\NewsPhoto.html"
print(url)

# 存在旧文件则删除
if os.path.exists(file_name):
    os.unlink(file_name)

# 处理浏览器平台参数
args = parser.parse_args()
browser_target = args.browser

with sync_playwright() as p:
    if browser_target == "chromium":
        browser = p.chromium.launch(headless=True)
    elif browser_target == "firefox":
        browser = p.firefox.launch(headless=True)
    elif browser_target == "webkit":
        browser = p.webkit.launch(headless=True)
    elif browser_target == "chrome":
        browser = p.chromium.launch(channel="chrome", headless=True)
    elif browser_target == "msedge":
        browser = p.chromium.launch(channel="msedge", headless=True)
    else:
        browser = p.chromium.launch(headless=True)

    page = browser.new_page()
    page.goto(url)
    page.locator("body").screenshot(path=file_name, type="jpeg", quality=100)
    print(page.title())
    browser.close()
