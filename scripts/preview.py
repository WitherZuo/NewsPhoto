#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess


# 函数：获取新闻文件路径
def get_news_file():
    news_file = input("请输入文件路径 (默认值为 ./news.txt): ").strip()
    if not news_file:
        news_file = "./news.txt"
    print(f"文件路径: {news_file}\n")
    return news_file


# 函数：获取问候语
def get_greeting_text():
    greeting_text = input("请输入问候语 (默认值为 ……): ").strip()
    if not greeting_text:
        greeting_text = "……"
    print(f"问候语: {greeting_text}\n")
    return greeting_text


# 函数：选择 NewsPhoto 主题
def choose_theme():
    print("请选择一个主题：")
    print("- [L] 浅色 / Light")
    print("- [D] 深色 / Dark")
    print("- [S] 春节 / Spring Festival")

    while True:
        choice = input("请输入对应选项的字母（L/D/S）: ").strip().lower()

        match choice:
            case "l":
                print("浅色 / Light\n")
                return "light"
            case "d":
                print("深色 / Dark\n")
                return "dark"
            case "s":
                print("春节 / Spring Festival\n")
                return "springfestival"
            case _:
                print("输入无效，请重试。\n", end="\r")


# 主函数
def main():
    print("NewsPhoto 交互式生成")
    print("欢迎使用 NewsPhoto 交互式生成，可按 CTRL+C 在任意步骤退出。\n")

    news_file = get_news_file()
    greeting_text = get_greeting_text()
    theme = choose_theme()

    # 调用外部命令，相当于 shell 脚本中的 uv run
    subprocess.run(
        [
            "uv",
            "run",
            "./main.py",
            "--greeting",
            greeting_text,
            "--style",
            theme,
            news_file,
        ],
        check=True,
    )
    subprocess.run(["uv", "run", "./save-as-image.py"], check=True)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n用户主动取消操作，已退出。")
