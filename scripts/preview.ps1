Write-Host 'NewsPhoto 交互式生成'
Write-Host '欢迎使用 NewsPhoto 交互式生成，可按 CTRL+C 在任意步骤退出。'

# 函数：获取新闻稿存储路径
function Get-NewsFile {
    $news_file = Read-Host '请输入新闻稿的存储路径'
    if ($news_file -eq '') {
        $news_file = './news.txt'
    }
    return $news_file
}

# 函数：获取问候语文本
function Get-Greeting {
    $greeting_text = Read-Host '请输入问候语文本'
    if ($greeting_text -eq '') {
        $greeting_text = '……'
    }
    return $greeting_text
}

# 函数：获取样式名
function Get-StyleName {
    $styles = 'light', 'dark', 'springfestival'
    $style_name = Read-Host '请输入样式名称（light | dark | springfestival）'

    if ($style_name -notin $styles) {
        Write-Host '无效输入，请重试。'
        Get-StyleName
    }
    return $style_name
}

# 执行操作
$news_file = Get-NewsFile
$greeting_text = Get-Greeting
$style_name = Get-StyleName

Write-Host '正在生成 NewsPhoto'
python .\main.py --greeting "$greeting_text" --style $style_name "$news_file"
python .\save-as-image.py
