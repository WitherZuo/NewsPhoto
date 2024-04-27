# News Photo

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/WitherZuo/NewsPhoto/main.yml?style=for-the-badge&logo=github-actions&logoColor=white) ![Use Pandoc](https://img.shields.io/badge/Pandoc-%23f5f5f5?style=for-the-badge&logo=markdown&logoColor=%23000&labelColor=%23ddd) ![I-Love-GitHubActions](https://img.shields.io/badge/I%20%E2%9D%A4%20YOU-GITHUB%20ACTIONS-blue?style=for-the-badge&logo=github&logoColor=white)

News Photo everyday. / 使用 Pandoc 生成新闻长图。

## 本地预览：

### 1. 准备环境

在测试项目、运行成品文件之前，请先安装并配置好**最新版本**的 `Git`、`Python`、`Playwright`、以及 `Pandoc`，执行如下命令来安装并配置所需要的环境，建议使用如 `venv` 这样的虚拟环境模块。

- [Git](https://git-scm.com/downloads)
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
python main.py
```

生成 NewsPhoto 的网页版本：`index.html`。`index.html` 位于 `outputs` 目录下。

<details>
<summary><b>📌 可用的开关 / 参数（点此展开）</b></summary>

```bash
# 命令格式
python main.py [-h] [-g GREETING_TEXT] [-s STYLE_NAME] [NEWS_FILE]

# 开关 / 参数说明：
NEWS_FILE：
生成 NewsPhoto 时所使用的新闻稿文件路径。（默认值：./news.txt）

-g / --greeting GREETING_TEXT：
问候内容文本。（默认值：……）

-s / --style STYLE_NAME：
生成 NewsPhoto 时所使用的样式，可选值：light | dark | springfestival。（默认值：light）
```

</details>

### 4. 生成图片

在终端中输入

```bash
python save-as-image.py
```

生成图片。生成的图片位于 `outputs` 目录下，名称为 `NewsPhoto.png`。

## 感谢：

- Pandoc：[Pandoc - About pandoc](https://pandoc.org/index.html)
- GitHub Actions：[GitHub Actions](https://github.com/features/actions)
- Playwright：[Playwright Python](https://playwright.dev/python/)
- Mi Sans: [Mi Sans](https://hyperos.mi.com/font)
- 项目依赖的其它第三方项目：pangu、zhdate
