import argparse

"""
参数说明：
-g, --greeting：祝贺内容文本
-s, --style：生成 NewsPhoto 所使用的样式，可选值：light | dark | springfestival
news_file: 生成 NewsPhoto 所使用的新闻稿
"""
parser = argparse.ArgumentParser(description="News Photo: News Photo everyday!")

parser.add_argument(
    "-g",
    "--greeting",
    metavar="GREETING TEXT",
    type=str,
    default="……",
    nargs="?",
    help="问候语文本，默认值：……",
)
parser.add_argument(
    "-s",
    "--style",
    metavar="STYLE NAME",
    type=str,
    choices=["light", "dark", "springfestival"],
    default="light",
    nargs="?",
    help="生成 NewsPhoto 所用的样式 ( light | dark | springfestival )，默认值：light",
)
parser.add_argument(
    "news_file",
    metavar="NEWS_FILE",
    type=str,
    default="./news.txt",
    nargs="?",
    help="生成 NewsPhoto 所用的新闻稿，默认值：./news.txt",
)
