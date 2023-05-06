# News Photo

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/WitherZuo/NewsPhoto/main.yml?style=for-the-badge&logo=github-actions&logoColor=white)  ![I-Love-GitHubActions](https://img.shields.io/badge/I%20%E2%9D%A4%20YOU-GITHUB%20ACTIONS-blue?style=for-the-badge&logo=github&logoColor=white)  ![Use-Pandoc](https://img.shields.io/badge/USE-Pandoc-red?style=for-the-badge&logo=markdown&logoColor=white)

News Photo every day.

这是一个生成新闻长图片的小项目，使用 Pandoc 作为转换核心。

## 项目文件结构：

|           文件名称           |                           对应描述                           |
| :--------------------------: | :----------------------------------------------------------: |
| `.github\workflows\main.yml` |     GitHub Actions 工作流文件，用于 Actions 生成最终成品     |
| `souurces\images\logo.png`  |                      必需资源：水印图片                      |
|       `sources\styles\index.css`        | 必需资源：样式表（控制成品的最终显示行为），用于生成最终成品的源文件之一 |
|        `news.txt`        |                      必需资源：新闻源稿                      |
|       `sources\images\photo.jpg`        |           必需资源：顶部图片（成品的顶部显示图片）           |
|         `.gitignore`         |     Git 忽略列表：告知 Git 应当被忽略且无需被上传的文件      |
|          `LICENSE`           |                   该项目遵守的相关开源协议                   |
|          `sources\index.md`           | 必需资源：经过整合的 Markdown 源文件，用于生成最终成品的源文件之一 |
|         `README.md`          |                         项目自述文件                         |

## 成品压缩包文件结构：

从 GitHub Actions 每次的执行结果中下载到生成好的成品文件，解压后转到释放文件的目录，然后执行`run.cmd`（Windows）或`run.sh`（macOS、Linux）可运行并预览成品效果。目录内其它文件的说明如下：

|          文件名称           |                           对应描述                           |
| :-------------------------: | :----------------------------------------------------------: |
| `ref\avatar-normal-new.png` |                      必需资源：水印图片                      |
|       `ref\bundle.js`       |           必需资源：已打包好功能的 Javascript 脚本           |
|       `ref\index.css`       |          必需资源：样式表（控制成品的最终显示行为）          |
|       `ref\news.txt`        |                      必需资源：新闻源稿                      |
|       `ref\photo.jpg`       |           必需资源：顶部图片（成品的顶部显示图片）           |
|       `bs-config.js`        |           用于 Browser-Sync 插件的调试预览配置文件           |
|        `index.html`         | 必需资源：经由 Pandoc 和 GitHub Actions 工作流生成的最终成品文件 |
|          `news.md`          |             必需资源：经过整合的 Markdown 源文件             |
|          `run.cmd`          |            用于运行整个成品的执行脚本（Windows）             |
|          `run.sh`           |          用于运行整个成品的执行脚本（macOS、Linux）          |

## 本地预览：

1. 在测试项目、运行成品文件之前，请先安装并配置好 `Git`、`Python`、`Playwright` 以及 `Pandoc`，然后执行如下命令来安装并配置所需要的环境，建议使用如 `venv` 这样的虚拟环境模块。

  ```bash
  pip install -r requirements.txt
  ```

2. 导航到项目根目录，并激活在上一步安装配置好的虚拟环境。
3. 确保处于项目根目录中，然后在终端中输入 `python main.py` 生成需要的源文件 `index.md`。`index.md` 位于 `sources` 目录下。
4. 完成上一步后，在终端中输入 `pandoc --metadata title='NewsPhoto' --embed-resources --standalone --css sources/styles/index.css sources/index.md --output sources/index.html` 生成 `index.html` 文件。该文件同样位于 `sources` 目录下。
5. 在终端中输入 `python browser-autotest.py` 生成图片。

## 感谢：

- Pandoc：[Pandoc - About pandoc](https://pandoc.org/index.html)
- Pandoc with GitHub Actions：https://github.com/pandoc/pandoc-action-example
- GitHub Actions：[GitHub Actions](https://github.com/features/actions)
- Playwright：[Playwright Python](https://playwright.dev/python/)
- 项目依赖的其它第三方项目：pangu、zhdate