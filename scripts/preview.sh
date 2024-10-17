#!/bin/bash
echo "NewsPhoto 交互式生成"
echo "欢迎使用 NewsPhoto 交互式生成，可按 CTRL+C 在任意步骤退出。"

# 函数，获取用户输入文件路径
get_news_file() {
    read -p "请输入文件路径 (默认值为 ./news.txt): " news_file
    if [ -z "$news_file" ]; then news_file="./news.txt"; fi
    echo "文件路径是: $news_file"
}

# 函数，获取用户输入的问候语
get_greeting_text() {
    read -p "请输入问候语 (默认值为 ……): " greeting_text
    if [ -z "$greeting_text" ]; then greeting_text="……"; fi
    echo "问候语是: $greeting_text"
}

# 函数，提示用户选择主题
choose_theme() {
    while true; do
        echo "请选择一个主题："
        echo "[L] 浅色 / Light"
        echo "[D] 深色 / Dark"
        echo "[S] 春节 / Spring Festival"

        # 提示用户输入第一个字母
        read -p "请输入对应选项的第一个字母（L/D/S）: " choice

        # 将输入转换为小写以便兼容大小写
        choice=$(echo "$choice" | tr '[:upper:]' '[:lower:]')

        case $choice in
            l) echo "浅色 / Light 主题"; theme="light"; break ;;
            d) echo "深色 / Dark 主题"; theme="dark"; break ;;
            s) echo "春节 / Spring Festival 主题"; theme="springfestival"; break ;;
            *) echo "输入无效，请重试。" ;;
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