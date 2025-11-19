# News Photo

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/WitherZuo/NewsPhoto/main.yml?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/WitherZuo/NewsPhoto/actions)
[![Use Pandoc](https://img.shields.io/badge/Pandoc-%23f5f5f5?style=for-the-badge&logo=markdown&logoColor=%23000&labelColor=%23ddd)](https://pandoc.org)
[![Open in GitHub Codespaces](https://img.shields.io/badge/_-Open%20in%20GitHub%20Codespaces-%2324292e?style=for-the-badge&logo=github&logoColor=%23ffffff&labelColor=%232f363d&color=%2324292e)](https://codespaces.new/WitherZuo/NewsPhoto?quickstart=1)

News Photo everyday. / 使用 Pandoc 生成新闻长图。

## 本地预览：

### 1. 准备环境

- uv: [Installation | uv](https://docs.astral.sh/uv/getting-started/installation/)
- Pandoc: [Pandoc - Installing pandoc](https://pandoc.org/installing.html)

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

### 3. 生成网页和图片

> [!TIP]
> **建议使用项目内的交互式生成脚本 `preview.py`，该脚本位于 `scripts` 目录下。**

确保处于**项目根目录**中，然后在终端中输入：

```bash
# 确保处于项目根目录中
uv run poe preview
```

<details>
<summary><b>🔴 手动分步操作（点此展开）</b></summary>

确保处于**项目根目录**中，然后在终端中输入：

```bash
uv run main.py
```

生成 NewsPhoto 的网页版本：`NewsPhoto.html`。`NewsPhoto.html` 位于 `outputs` 目录下。

之后在终端中输入：

```bash
uv run save-as-image.py
```

生成图片。生成的图片位于 `outputs` 目录下，名称为 `NewsPhoto.png`。

**📌 可用的开关 / 参数**：

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

</details>

## 打包为可执行文件

> [!NOTE]
> 请参阅 [Nuitka 的说明](https://nuitka.net/user-documentation/user-manual.html#c-compiler) 设置编译器。

> [!CAUTION]
> **Windows 平台必须使用 MSVC 作为编译器**。请安装 Visual Studio Build Tools，在“单个组件”中选择以下组件：
> - 适用于 x64/x86 的 MSVC 生成工具(最新版) **或** 适用于 ARM64/ARM64EC 的 MSVC 生成工具(最新版)
> - 最新版本的 Windows SDK

配置完成后，在**项目根目录**中打开终端，输入：

```bash
# 确保处于项目根目录中
uv run poe build

# 完成后结果
main.py -> dist/np-gen.exe (Windows), dist/np-gen (macOS / Linux)
save-as-image.py -> dist/np-save.exe (Windows), dist/np-save (macOS / Linux)
```

打包生成可执行文件。生成的文件位于 `dist` 目录下，且包含所需的浏览器组件。
