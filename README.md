# News Photo

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/WitherZuo/NewsPhoto/main.yml?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/WitherZuo/NewsPhoto/actions) [![Use Pandoc](https://img.shields.io/badge/Pandoc-%23f5f5f5?style=for-the-badge&logo=markdown&logoColor=%23000&labelColor=%23ddd)](https://pandoc.org) [![Open in GitHub Codespaces](https://img.shields.io/badge/_-Open%20in%20GitHub%20Codespaces-%2324292e?style=for-the-badge&logo=github&logoColor=%23ffffff&labelColor=%232f363d&color=%2324292e)](https://codespaces.new/WitherZuo/NewsPhoto?quickstart=1)

News Photo everyday. / 使用 Pandoc 生成新闻长图。

## 本地预览：

### 1. 准备环境

在测试项目、运行成品文件之前，请先安装并配置好**最新版本**的 [`Git`](https://git-scm.com/downloads)、[`uv`](https://docs.astral.sh/uv/getting-started/installation/)、[`Playwright`](https://playwright.dev/python/docs/intro#installing-playwright)、以及 [`Pandoc`](https://pandoc.org/installing.html)。

### 2. 克隆项目
```bash
# 克隆项目到本地
git clone https://github.com/WitherZuo/NewsPhoto.git
cd NewsPhoto

# 安装所需第三方库
uv sync

# 安装并配置 Playwright 和 Chromium
uv run playwright install chromium-headless-shell --with-deps
```

### 3. 生成网页

确保处于项目根目录中，然后在终端中输入

```bash
uv run main.py
```

生成 NewsPhoto 的网页版本：`NewsPhoto.html`。`NewsPhoto.html` 位于 `outputs` 目录下。

<details>
<summary><b>📌 可用的开关 / 参数（点此展开）</b></summary>

```bash
# 命令格式
uv run main.py [-h] [-g GREETING_TEXT] [-s STYLE_NAME] [NEWS_FILE]

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
uv run save-as-image.py
```

生成图片。生成的图片位于 `outputs` 目录下，名称为 `NewsPhoto.png`。

**或者也可以使用项目内的交互式生成脚本 `preview.sh`，该脚本位于 `scripts` 目录下。**

- **Windows**：确保 `<Git 安装目录>\usr\bin\` 在 `PATH` 环境变量中，然后在项目根目录下，执行 `sh scripts\preview.sh`。
- **macOS、Linux**：赋予脚本 `preview.sh` 执行权限，然后在项目根目录下，从当前 shell 中执行 `scripts/preview.sh`。

## 感谢：

- Pandoc：[Pandoc - About pandoc](https://pandoc.org)
- GitHub Actions：[GitHub Actions](https://github.com/features/actions)
- Playwright：[Playwright Python](https://playwright.dev/python/)
- Mi Sans: [Mi Sans](https://hyperos.mi.com/font)
- 项目依赖的其它第三方项目：pangu、zhdate
