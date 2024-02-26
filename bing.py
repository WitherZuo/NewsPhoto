# coding=utf-8
import requests

# 获取必应图片的 JSON 文件
def get_bing_json():
    # 请求头：使用火狐的用户代理字符串
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0"}

    # 获取必应图片的 json 数据
    r = requests.get(
        "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN", headers=headers)
    bingimage_fulldata = r.json()

    # 解析 json 对象
    bingimage_data = bingimage_fulldata["images"][0]

    # 返回解析后的 json 数据
    return bingimage_data

# 获取必应图片的标题和版权所有者
def get_bing_title(bingimage_data):
    # 拆分图片标题和版权所有者字符串
    bingimage_title = bingimage_data.get("copyright").split(" (")

    # 将分离的字符串处理后写入变量
    """
    bingimage_title[0]：图片标题；
    bingimage_title[1]：图片所有者；
    """
    title = bingimage_title[0]
    copyright_owner = bingimage_title[1].replace(")", "")

    # 返回处理后的图片标题和所有者
    return title, copyright_owner

# 获取必应图片到本地
def get_bing_image(bingimage_data):
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
    bingimage = requests.get(bingimage_fullurl)
    photo_location = "sources/images/photo.jpg"

    with open(photo_location, "wb") as f:
        f.write(bingimage.content)
        f.close()


# 调用函数
if __name__ == "__main__":
    json_data = get_bing_json()
    get_bing_title(json_data)
    get_bing_image(json_data)
