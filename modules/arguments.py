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
    help="Greeting text",
)
parser.add_argument(
    "-s",
    "--style",
    metavar="STYLE NAME",
    type=str,
    choices=["light", "dark", "springfestival"],
    default="light",
    nargs="?",
    help="NewsPhoto style ( light | dark | springfestival )",
)
parser.add_argument(
    "news_file",
    metavar="NEWS_FILE",
    type=str,
    default="./news.txt",
    nargs="?",
    help="News file you want to use",
)
