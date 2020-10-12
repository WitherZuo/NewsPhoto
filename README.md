# News Photo  

![PandocTask](https://github.com/WitherZuo/NewsPhoto/workflows/PandocTask/badge.svg)  

News Photo every day.  

这是一个生成新闻长图片的小项目，使用 Pandoc 作为转换核心。

## 项目文件结构：

|           文件名称           |                           对应描述                           |
| :--------------------------: | :----------------------------------------------------------: |
| `.github\workflows\main.yml` |     GitHub Actions 工作流文件，用于 Actions 生成最终成品     |
| `ref\avatar-normal-new.png`  |                      必需资源：水印图片                      |
|       `ref\bundle.js`        |           必需资源：已打包好功能的 Javascript 脚本           |
|       `ref\index.css`        | 必需资源：样式表（控制成品的最终显示行为），用于生成最终成品的源文件之一 |
|        `ref\news.txt`        |                      必需资源：新闻源稿                      |
|       `ref\photo.jpg`        |           必需资源：顶部图片（成品的顶部显示图片）           |
|         `.gitignore`         |     Git 忽略列表：告知 Git 应当被忽略且无需被上传的文件      |
|        `bs-config.js`        |           用于 Browser-Sync 插件的调试预览配置文件           |
|          `LICENSE`           |                   该项目遵守的相关开源协议                   |
|          `news.md`           | 必需资源：经过整合的 Markdown 源文件，用于生成最终成品的源文件之一 |
|         `publish.sh`         |             用于上传所有文件并发布项目的执行脚本             |
|         `README.md`          |                         项目自述文件                         |
|          `test.cmd`          |          用于测试项目显示效果的执行脚本（Windows）           |
|          `test.sh`           |        用于测试项目显示效果的执行脚本（macOS、Linux）        |

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

## 注意事项：

- 在测试项目、运行成品文件之前，请先安装并配置好 `Git`、`Node.js`，然后执行如下命令来安装并配置 `Browser-Sync`。

  ```bash
  npm install browser-sync -g
  ```
  
- 最好不要同时运行项目测试和成品预览（可能会造成冲突，当然也很可能分不清你到底在看哪一个）🤣  

## 感谢：

- Pandoc：[Pandoc - About pandoc](https://pandoc.org/index.html)  
- Pandoc with GitHub Actions：https://github.com/pandoc/pandoc-action-example  
- GitHub Actions：[GitHub Actions](https://github.com/features/actions)  
- Browser-Sync：[Browsersync - Time-saving synchronised browser testing](https://www.browsersync.io/)
- html-to-image：[bubkoo/html-to-image: ✂️ Generates an image from a DOM node using HTML5 canvas and SVG. (github.com)](https://github.com/bubkoo/html-to-image)