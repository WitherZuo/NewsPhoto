# News Photo

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/WitherZuo/NewsPhoto/main.yml?style=for-the-badge&logo=github-actions&logoColor=white)  ![I-Love-GitHubActions](https://img.shields.io/badge/I%20%E2%9D%A4%20YOU-GITHUB%20ACTIONS-blue?style=for-the-badge&logo=github&logoColor=white)  ![Use-Pandoc](https://img.shields.io/badge/USE-Pandoc-red?style=for-the-badge&logo=markdown&logoColor=white)

News Photo every day.

这是一个生成新闻长图片的小项目，使用 Pandoc 作为转换核心。

## 项目文件结构：
<details>
<summary>点击此处显示</summary>

```
./NewsPhoto
│   .gitattributes（用于控制 Git LFS 大文件存储特性的设置）
│   .gitignore（配置应被 Git 忽略追踪的文件）
│   browser-autotest.py（浏览器自动化，从生成的页面截图）
│   LICENSE（项目许可）
│   main.py（项目主入口，生成所需的源文件：index.md）
│   news.txt（初始的新闻源稿，必需）
│   NewsPhoto.code-workspace（VS Code 工作区配置）
│   README.md（项目自述）
│   requirements.txt（项目的依赖项配置文件）
│
├───.github（GitHub 相关）
│   └───workflows（GitHub Actions 工作流）
│           main.yml（工作流任务配置）
│
├───.vscode（VS Code 项目配置）
│       tasks.json（项目中的可执行任务）
│
├───modules（项目功能模块）
│       __init__.py（模块初始化文件）
│       today.py（获取和当前日期时间有关的信息，包括农历日期）
│       bing.py（获取必应每日图片的数据，包括描述和图片自身）
│       zhdate.py（获取中国农历日期）
│       constants.py（农历月份数据）
│
├───push（可重用的任务）
│       preview.ps1（用于一键生成 NewsPhoto 并预览）
│       publish.ps1（用于一键上传 NewsPhoto 成品并生成 Release）
│
├───sources（项目源文件）
│   │   index.html（NewsPhoto 页面，默认不存在）
│   │   index.md（Markdown 版 NewsPhoto 文档，用于生成 index.html，默认不存在）
│   │   NewsPhoto.png（生成的 NewsPhoto 图片，默认不存在）
│   │
│   ├───fonts（字体）
│   │       .gitkeep（缺省文件）
│   │       MiSans-Regular.woff2（Mi Sans 字体，Regular 字重）
│   │       MiSans-Semibold.woff2（Mi Sans 字体，Semibold 字重）
│   │
│   ├───images（图片）
│   │       photo.jpg（当日的必应图片，默认不存在）
│   │       qrcode-springfestival.png（二维码，春节风格）
│   │       qrcode.png（二维码，正常风格）
│   │
│   └───styles（样式表）
│           footer.css（底部栏样式）
│           global.css（全局样式）
│           header.css（顶部栏样式）
│           index.css（样式主入口）
│           section.css（主要内容样式）
│           springfestival.css（春节特殊样式）
│
└───template（模板）
        newsphoto.html5（Pandoc 生成 HTML 文件时所需模板）
```

</details>

## 本地预览：

### 1. 准备环境

在测试项目、运行成品文件之前，请先安装并配置好**最新版本**的 `Git`、`Python`、`Playwright`、`Git LFS` 以及 `Pandoc`，执行如下命令来安装并配置所需要的环境，建议使用如 `venv` 这样的虚拟环境模块。

- [Git](https://git-scm.com/downloads)
- [Git LFS](https://github.com/git-lfs/git-lfs#installing)
- [Python](https://www.python.org/downloads/)
- [Pandoc](https://pandoc.org/installing.html)
- [Playwright](https://playwright.dev/python/docs/intro#installing-playwright)
    ```
    # 安装并配置 Playwright 和 Chromium
    playwright install chromium --with-deps
    ```

### 2. 克隆项目
```bash
# 克隆项目到本地
git clone https://github.com/WitherZuo/NewsPhoto.git

# 安装所需第三方库
pip install -r requirements.txt
```

### 3. 生成源文件

确保处于项目根目录中，然后在终端中输入

```bash
python main.py
```

生成需要的源文件 `index.md`。`index.md` 位于 `sources` 目录下。

### 4. 生成网页

完成上一步后，在终端中输入

```bash
pandoc --metadata title='NewsPhoto' --embed-resources --standalone --template='template/newsphoto.html5' --css sources/styles/index.css sources/index.md --output sources/index.html
```

生成 `index.html` 文件。该文件同样位于 `sources` 目录下。

### 5. 生成图片

在终端中输入

```bash
python browser-autotest.py
```

生成图片。生成的图片位于 `sources` 目录下，名称为 `NewsPhoto.png`。

⚠️（注：从 Release/Tag 页获取的源码包可能**不包含**字体文件，如果需要，可从仓库的 `sources/fonts` 目录下单独获取，放到本地指定位置即可 ）

## 感谢：

- Pandoc：[Pandoc - About pandoc](https://pandoc.org/index.html)
- GitHub Actions：[GitHub Actions](https://github.com/features/actions)
- Playwright：[Playwright Python](https://playwright.dev/python/)
- 项目依赖的其它第三方项目：pangu、zhdate