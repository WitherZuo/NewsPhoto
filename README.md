# News Photo

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/WitherZuo/NewsPhoto/main.yml?style=for-the-badge&logo=github-actions&logoColor=white)  ![I-Love-GitHubActions](https://img.shields.io/badge/I%20%E2%9D%A4%20YOU-GITHUB%20ACTIONS-blue?style=for-the-badge&logo=github&logoColor=white)  ![Use-Pandoc](https://img.shields.io/badge/USE-Pandoc-red?style=for-the-badge&logo=markdown&logoColor=white)

News Photo everyday. / 使用 Pandoc 生成新闻长图。

## 本地预览：

### 1. 准备环境

在测试项目、运行成品文件之前，请先安装并配置好**最新版本**的 `Git`、`Python`、`Playwright`、`Git LFS` 以及 `Pandoc`，执行如下命令来安装并配置所需要的环境，建议使用如 `venv` 这样的虚拟环境模块。

- [Git](https://git-scm.com/downloads)
- [Git LFS](https://github.com/git-lfs/git-lfs#installing)
- [Python](https://www.python.org/downloads/)
- [Pandoc](https://pandoc.org/installing.html)
- [Playwright](https://playwright.dev/python/docs/intro#installing-playwright)

### 2. 克隆项目
```bash
# 克隆项目到本地
git clone https://github.com/WitherZuo/NewsPhoto.git

# 安装所需第三方库
pip install -r requirements.txt

# 安装并配置 Playwright 和 Chromium
playwright install chromium --with-deps
```

### 3. 生成网页

确保处于项目根目录中，然后在终端中输入

```bash
# main.py 执行时可用的开关 / 参数：
#
# NEWS_FILE：
# 生成 NewsPhoto 时所使用的新闻稿文件路径。（默认值：./news.txt）
#
# -g / --greeting GREETING_TEXT：
# 问候内容文本。（默认值：……）
#
# -s / --style STYLE_NAME：
# 生成 NewsPhoto 时所使用的样式，可选值：light | dark | springfestival。（默认值：light）

python main.py
```

生成 NewsPhoto 的网页版本：`index.html`。`index.html` 位于 `outputs` 目录下。

### 4. 生成图片

在终端中输入

```bash
python save-as-image.py
```

生成图片。生成的图片位于 `outputs` 目录下，名称为 `NewsPhoto.png`。

⚠️（注：请**使用 `git clone` 方式获取项目源代码到本地**而非通过 Releases 或 Tags 页面，由于项目使用了 Git LFS，使用后者获取源码可能无法获取字体文件导致显示异常！）

## 感谢：

- Pandoc：[Pandoc - About pandoc](https://pandoc.org/index.html)
- GitHub Actions：[GitHub Actions](https://github.com/features/actions)
- Playwright：[Playwright Python](https://playwright.dev/python/)
- 项目依赖的其它第三方项目：pangu、zhdate
