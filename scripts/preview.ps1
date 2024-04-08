Write-Host 'NewsPhoto 交互式生成'
Write-Host '欢迎使用 NewsPhoto 交互式生成，可按 CTRL+C 在任意步骤退出。'

# 获取新闻稿存储路径
$news_file = Read-Host '请输入新闻稿的存储路径'
if ($news_file -eq '') {
    $news_file = './news.txt'
}

# 获取问候语文本
$greeting_text = Read-Host '请输入问候语文本'
if ($greeting_text -eq '') {
    $greeting_text = '……'
}

# 选择 NewsPhoto 所使用的样式
$options = @(
    [System.Management.Automation.Host.ChoiceDescription]::new('&Light / 浅色', 'Light: 使用浅色样式')
    [System.Management.Automation.Host.ChoiceDescription]::new('&Dark / 深色', 'Dark：使用深色样式')
    [System.Management.Automation.Host.ChoiceDescription]::new('&Spring Festival / 春节', 'Spring Festival：使用春节样式')
)

$title = ''
$message = '请选择生成 NewsPhoto 时使用的样式：'
$result = $host.ui.PromptForChoice($title, $message, $options, 0)
switch ($result) {
    0 { $style_name = 'light' }
    1 { $style_name = 'dark' }
    2 { $style_name = 'springfestival' }
    Default { $style_name = 'light' }
}

Write-Host '正在生成 NewsPhoto'
python ./main.py --greeting "$greeting_text" --style $style_name "$news_file"
python ./save-as-image.py
