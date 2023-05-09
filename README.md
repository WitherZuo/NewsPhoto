# News Photo

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/WitherZuo/NewsPhoto/main.yml?style=for-the-badge&logo=github-actions&logoColor=white)  ![I-Love-GitHubActions](https://img.shields.io/badge/I%20%E2%9D%A4%20YOU-GITHUB%20ACTIONS-blue?style=for-the-badge&logo=github&logoColor=white)  ![Use-Pandoc](https://img.shields.io/badge/USE-Pandoc-red?style=for-the-badge&logo=markdown&logoColor=white)

News Photo every day.

这是一个生成新闻长图片的小项目，使用 Pandoc 作为转换核心。

## 项目文件结构：

|           文件名称           |                           对应描述                           |
| :--------------------------: | :----------------------------------------------------------: |
| `.github\workflows\main.yml` |     GitHub Actions 工作流文件，用于 Actions 生成最终成品     |
| `souurces\`  |                      所需要的资源：图片、字体、文本 等                      |
|        `news.txt`        |                      必需资源：新闻源稿                      |
|         `.gitignore`         |     Git 忽略列表：告知 Git 应当被忽略且无需被上传的文件      |
|          `LICENSE`           |                   该项目遵守的相关开源协议                   |
|         `README.md`          |                         项目自述文件                         |

## 本地预览：

### 1. 准备环境

在测试项目、运行成品文件之前，请先安装并配置好 `Git`、`Python`、`Playwright`、`Git LFS` 以及 `Pandoc`，然后执行如下命令来安装并配置所需要的环境，建议使用如 `venv` 这样的虚拟环境模块。

```bash
pip install -r requirements.txt
```

### 2. 激活虚拟环境（可选）

导航到项目根目录，并激活在上一步安装配置好的虚拟环境。

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