import argparse


def get_parser():
    """
    参数说明：
    -g, --greeting：问候内容文本
    -s, --style：生成 NewsPhoto 时所使用的样式，可选值：light | dark | springfestival
    news_file: 生成 NewsPhoto 时所使用的新闻稿
    """
    parser = argparse.ArgumentParser(description="News Photo: News Photo everyday!")

    parser.add_argument(
        "-g",
        "--greeting",
        metavar="GREETING_TEXT",
        type=str,
        default="……",
        required=False,
        help="Greeting text ( Default: …… )",
    )
    parser.add_argument(
        "-s",
        "--style",
        metavar="STYLE_NAME",
        type=str,
        choices=["light", "dark", "springfestival"],
        default="light",
        required=False,
        help="NewsPhoto style ( light | dark | springfestival, Default: light )",
    )
    parser.add_argument(
        "news_file",
        metavar="NEWS_FILE",
        type=str,
        default="./news.txt",
        nargs="?",
        help="Raw file of news source ( Default: ./news.txt )",
    )

    return parser
