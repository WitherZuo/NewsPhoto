#!/bin/bash
echo "NewsPhoto 交互式生成"
echo -e "欢迎使用 NewsPhoto 交互式生成，可按 CTRL+C 在任意步骤退出。\n"

# 函数，获取用户输入文件路径
get_news_file() {
    read -p "请输入文件路径 (默认值为 ./news.txt): " news_file
    if [ -z "$news_file" ]; then news_file="./news.txt"; fi
    echo -e "文件路径: $news_file \n"
}

# 函数，获取用户输入的问候语
get_greeting_text() {
    read -p "请输入问候语 (默认值为 ……): " greeting_text
    if [ -z "$greeting_text" ]; then greeting_text="……"; fi
    echo -e "问候语: $greeting_text \n"
}

# 函数，提示用户选择主题
choose_theme() {
    while true; do
        echo "请选择一个主题："
        echo "- [L] 浅色 / Light"
        echo "- [D] 深色 / Dark"
        echo "- [S] 春节 / Spring Festival"

        # 提示用户输入第一个字母
        read -p "请输入对应选项的字母（L/D/S）: " choice

        # 将输入转换为小写以便兼容大小写
        choice=$(echo "$choice" | tr '[:upper:]' '[:lower:]')

        case $choice in
            l) echo -e "浅色 / Light \n"; theme="light"; break ;;
            d) echo -e "深色 / Dark \n"; theme="dark"; break ;;
            s) echo -e "春节 / Spring Festival \n"; theme="springfestival"; break ;;
            *) echo -e "输入无效，请重试。 \n" ;;
        esac
    done
}

# 调用函数获取文件路径、问候语和主题
get_news_file
get_greeting_text
choose_theme

# 生成内容
python ./main.py --greeting "$greeting_text" --style $theme "$news_file"
python ./save-as-image.py
