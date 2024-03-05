# coding=utf-8
from modules.today import get_simple_date, get_full_date, get_weekday, get_zh_date
from modules.bing import get_bing_json, get_bing_title, get_bing_image
import os
import pangu
import re

# 清理过时文件
outdated_files = [
    "sources/header.md",
    "sources/content.md",
    "sources/index.md",
    "sources/footer.md",
    "sources/images/photo.jpg",
    "sources/index.html",
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

# 祝贺文本
greeting = "不是由 ChatGPT 生成的"

# 写入头文件：header.md
header_text = [
    "<header>  \n\n",
    "![News Photo · 半日刊](sources/images/photo.jpg)  \n\n",
    "</header>  \n\n",
    "<section>  \n\n",
    "## " + today_simple_date + " · " + today_weekday + " · " + today_zhdate + "\n\n",
    "【 " + greeting + " 】" + "  \n\n",
]
f = open("sources/header.md", "w", encoding="utf_8")
f.writelines(header_text)
f.close()

# 处理正文文本 news.txt，写入到新的正文文件：content.md
a = open("news.txt", "r", encoding="utf_8")
text = a.read()
text_with_space = pangu.spacing(text)
text_new = re.sub("\n", "  \n\n", text_with_space)

b = open("sources/content.md", "w", encoding="utf_8")
b.write(text_new + "\n\n")

b.close()
a.close()

# 写入底部文件：footer.md
footer_text = [
    "</section>  \n\n",
    "<footer>  \n\n",
    "**" + bing_title[0] + "**<br>",
    "**" + bing_title[1] + "**  \n\n",
    "> 最后更新: " + today_full_date + " / UTC+8<br>",
    "最后修订: " + today_full_date + " / UTC+8  \n\n",
    '![qrcode](sources/images/qrcode.png "qrcode")  \n\n',
    "</footer>",
]
c = open("sources/footer.md", "w", encoding="utf_8")
c.writelines(footer_text)
c.close()

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

# 清理不需要的文件
unused_files = ["sources/header.md", "sources/content.md", "sources/footer.md"]
for unused_file in unused_files:
    if os.path.exists(unused_file):
        os.unlink(unused_file)
