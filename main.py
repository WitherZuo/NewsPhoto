# coding=utf-8
from today import getSimpleDate, getFullDate, getWeekday, getZhDate
from bing import getBingJSON, getBingTitle, getBingImage
import os
import pangu
import re

# 清理过时文件
outdated_files = ["sources/header.md", "sources/content.md",
                  "sources/index.md", "sources/footer.md",
                  "sources/images/photo.jpg", "sources/index.html"]
for outdated_file in outdated_files:
    if os.path.exists(outdated_file):
        os.unlink(outdated_file)

# 获取所需要的日期时间值
today_simple_date = getSimpleDate()
today_full_date = getFullDate()
today_weekday = getWeekday(today_full_date)
today_zhdate = getZhDate()

# 获取必应图片
json_data = getBingJSON()
bing_title = getBingTitle(json_data)
getBingImage(json_data)

# 祝贺文本
greeting = "不是由 ChatGPT 生成的"

# 写入头文件：header.md
f = open("sources/header.md", "w", encoding="utf_8")
f.writelines("<header>  \n\n")
f.writelines("![News Photo · 半日刊](sources/images/photo.jpg)  \n\n")
f.writelines("</header>  \n\n")
f.writelines("<section>  \n\n")
f.writelines("## "+today_simple_date+" · " +
             today_weekday+" · "+today_zhdate+"\n\n")
f.writelines("【 "+greeting+" 】"+"  \n\n")
f.close()

# 处理正文文本 news.txt，写入到新的正文文件：content.md
a = open("news.txt", "r", encoding="utf_8")
text = a.read()
text_with_space = pangu.spacing(text)
text_new = re.sub("\n", "  \n\n", text_with_space)

b = open("sources/content.md", "w", encoding="utf_8")
b.write(text_new+"\n\n")

b.close()
a.close()

# 写入底部文件：footer.md
c = open("sources/footer.md", "w", encoding="utf_8")
c.writelines("</section>  \n\n")
c.writelines("<footer>  \n\n")
c.writelines("**"+bing_title[0]+"**<br>")
c.writelines("**"+bing_title[1]+"**  \n\n")
c.writelines("> 最后更新: "+today_full_date+" / UTC+8<br>")
c.writelines("最后修订: "+today_full_date+" / UTC+8  \n\n")
c.writelines('![qrcode](sources/images/qrcode.png "qrcode")  \n\n')
c.writelines("</footer>")
c.close()

# 汇总后综合写入 index.md
index_md = open("sources/index.md", "a", encoding="utf_8")

header = open("sources/header.md", "r", encoding="utf_8")
content = open("sources/content.md", "r", encoding="utf_8")
footer = open("sources/footer.md", "r", encoding="utf_8")

header_source = header.read()
content_source = content.read()
footer_source = footer.read()

index_md.write(header_source)
index_md.write(content_source)
index_md.write(footer_source)

source_files = [header, content, footer, index_md]
for sources_file in source_files:
    sources_file.close()

# 清理不需要的文件
unused_files = ["sources/header.md", "sources/content.md", "sources/footer.md"]
for unused_file in unused_files:
    if os.path.exists(unused_file):
        os.unlink(unused_file)
