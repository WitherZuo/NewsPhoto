from playwright.sync_api import sync_playwright
import os

file_name = "sources/NewsPhoto.png"
url = "file:///"+os.getcwd()+r"\sources\index.html"
print(url)

if os.path.exists(file_name):
    os.unlink(file_name)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(url)
    page.locator("body").screenshot(path=file_name, type="jpeg", quality=100)
    print(page.title())
    browser.close()
