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
    # 可用浏览器列表
    
    browser_launchers = {
        "chromium": p.chromium.launch,
        "firefox": p.firefox.launch,
        "webkit": p.webkit.launch,
        "chrome": p.chromium.launch,
        "msedge": p.chromium.launch,
    }

    browser_target = args.browser.lower()
    launch_func = browser_launchers.get(browser_target)

    if launch_func:
        if browser_target in ["chrome", "msedge"]:
            browser = launch_func(channel=browser_target, headless=True)
        else:
            browser = launch_func(headless=True)
    else:
        print(f"Unsupported browser: {browser_target}. Launching chromium instead.")
        browser = p.chromium.launch(headless=True)

    page = browser.new_page()
    page.goto(url)
    page.locator("body").screenshot(path=file_name, type="png")
    print(page.title())
    browser.close()
