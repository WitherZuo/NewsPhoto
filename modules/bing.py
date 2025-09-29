# coding=utf-8
import os
import sys
import time
from functools import wraps

import requests

# 全局最大重试次数
MAX_RETRIES = 3
# 每次重试的等待时间（秒）
RETRY_DELAY = 2


# 装饰器：重试指定
def retryable(max_retries=MAX_RETRIES, delay=RETRY_DELAY):
    # 处理任务，失败则每隔一段时间重试，全部失败后抛出最后异常
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Failed after {attempt} attempt(s): {e}")
                    if attempt < max_retries:
                        time.sleep(delay)
            sys.exit(1)

        return wrapper

    return decorator


# 获取必应图片的 JSON 文件
@retryable()
def get_bing_json():
    print("- Getting the metadata of Bing image...")
    # 请求头：使用火狐的用户代理字符串
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/141.0"
    }

    # 获取必应图片的 json 数据
    r = requests.get(
        "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN",
        headers=headers,
        timeout=20,
    )
    bingimage_fulldata = r.json()

    # 解析 json 对象
    bingimage_data = bingimage_fulldata["images"][0]

    # 返回解析后的 json 数据
    return bingimage_data


# 获取必应图片的标题和版权所有者
def get_bing_title(bingimage_data):
    print("- Getting the title and copyright owner of Bing image...")
    # 拆分图片标题和版权所有者字符串
    bingimage_title = bingimage_data.get("copyright").split(" (© ")

    # 将分离的字符串处理后写入变量
    """
    bingimage_title[0]：图片标题；
    bingimage_title[1]：图片所有者；
    """
    title = bingimage_title[0]
    copyright_owner = "© " + bingimage_title[1].replace(")", "")

    # 返回处理后的图片标题和所有者
    return title, copyright_owner


# 获取必应图片到本地
@retryable()
def get_bing_image(bingimage_data):
    print("- Downloading the Bing image...")
    # 获取图片地址，然后拼接
    """
    获取图片网址和详细信息
    bingimage_url：从 json 中解析的图片链接，需要拼接；
    bingimage_fullurl：拼接的完整图片链接；
    bingimage_title：从 json 中解析的图片标题信息
    """
    bingimage_url = bingimage_data.get("url")
    bingimage_fullurl = "https://s.cn.bing.net" + bingimage_url

    # 下载图片到本地
    bingimage = requests.get(bingimage_fullurl, timeout=20)
    photo_location = os.path.join("outputs", "photo.jpg")

    with open(photo_location, "wb") as f:
        f.write(bingimage.content)
