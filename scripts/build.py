#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import platform
import re
import subprocess
import sys
from importlib.util import find_spec
from pathlib import Path
from shutil import copytree, rmtree, which

# 添加本地模块路径
sys.path.append(".")
# 处理模块名称与导入名称不一致的情况
module_alias = {
    "charset-normalizer": "charset_normalizer",
    "ordered-set": "ordered_set",
    "pyyaml": "yaml",
    "typing-extensions": "typing_extensions",
}
# 本地模块列表
self_modules = [
    "modules",
    "modules.bing",
    "modules.today",
    "modules.arguments",
    "modules.constants",
    "modules.zhdate",
]
# 编译产物输出目录名
output_dirname = "dist"
# 定义 requirements.txt 文件路径
requirements_txt = Path().resolve() / output_dirname / "requirements.txt"


# 返回 Nuitka 编译命令并执行
def build_with_nuitka(input_file, output_file, icon_file, include_browser=False):
    # 通过 uv 运行 nuitka，所有平台的公共参数
    base_cmd = [
        "uv",
        "run",
        "nuitka",
        "--onefile",
        f"{input_file}",
        "--remove-output",
        f"--output-dir={output_dirname}",
        "--assume-yes-for-downloads",
    ]
    # 特定系统的参数
    platform_args = []
    system = platform.system().lower()

    match system:
        # Windows 特定参数
        case "windows":
            args = [
                f"--output-filename={output_file}.exe",
                "--lto=yes",
                f"--windows-icon-from-ico={icon_file}.ico",
            ]
            browser_path = Path.home() / "AppData" / "Local" / "ms-playwright"
        # macOS 特定参数
        case "darwin":
            args = [
                f"--output-filename={output_file}",
                f"--macos-app-icon={icon_file}.icns",
            ]
            browser_path = Path.home() / "Library" / "Caches" / "ms-playwright"
        # Linux 特定参数
        case "linux":
            args = [
                f"--output-filename={output_file}",
                "--lto=yes",
            ]
            browser_path = Path.home() / ".cache" / "ms-playwright"
        # 不支持的操作系统
        case _:
            raise RuntimeError(f"不支持的操作系统：{system}")

    # 合并所有参数，如果 include_browser 为 True，则复制浏览器到 dist 目录
    platform_args.extend(args)
    cmd = base_cmd + platform_args
    # 执行编译命令
    print(f"\n正在编译：{input_file}")
    print(f"执行命令：{' '.join(cmd)}\n")
    subprocess.run(cmd, check=True)
    if include_browser:
        print("正在复制浏览器文件...")
        copytree(browser_path, Path(output_dirname) / "browser")

    return cmd


# 函数：检查 uv 是否安装
def check_uv():
    print("检查本机是否安装 uv...")
    uv_install = which("uv")
    if uv_install != None:
        print(f"uv 已安装：{uv_install}\n")
    else:
        raise FileNotFoundError("未找到 uv。本项目由 uv 管理，请先安装 uv 后重试")


# 函数：生成 requirements.txt 文件
def create_requirements_txt(output_file):
    print("导出项目依赖...\n")
    cmd = [
        "uv",
        "export",
        "--format",
        "requirements.txt",
        "--no-annotate",
        "--no-header",
        "--no-hashes",
    ]
    result = subprocess.run(cmd, check=True, text=True, capture_output=True)
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result.stdout)
    except Exception as e:
        raise (e)


# 函数：获取外部已安装模块
def get_installed_modules(module_list_file):
    installed_modules = []
    # 以只读模式打开 requirements.txt 文件
    with open(module_list_file, "r", encoding="utf-8") as requirements:
        # 读取每一行模块定义，取模块名称部分，处理别名后添加到已安装模块列表
        for line in requirements.readlines():
            module = re.split(r"[=<>~!]", line, maxsplit=1)[0]
            if module in module_alias:
                module = module_alias[module]
            installed_modules.append(module)

    return installed_modules


# 函数：检查模块是否能被导入
def check_modules(module):
    imported_modules, failed_modules = [], []
    # 遍历所有模块，尝试导入
    for installed_module in module:
        print(f"尝试导入模块：{installed_module}...")
        # 查找模块定义，并输出检查结果
        result = find_spec(installed_module)
        print(result)
        # 如果为 None 则未找到模块
        if result == None:
            print(f"🔴 模块 {installed_module} 无法被导入！\n")
            # 导入失败，添加到导入失败模块列表
            failed_modules.append(installed_module)
        else:
            print(f"🟢 模块 {installed_module} 已安装，且可以被导入。\n")
            # 导入成功，添加到已导入模块列表
            imported_modules.append(installed_module)

    # 输出导入成功和失败的模块列表
    print(f"• 这些模块导入成功：{', '.join(imported_modules)}")
    if failed_modules:
        print(f"• 这些模块导入失败：{', '.join(failed_modules)}")
    else:
        print("• 没有发现导入失败的模块")

    return imported_modules, failed_modules


# 主函数
def main():
    try:
        # 检查 uv 是否安装
        check_uv()
        # 删除上一次输出目录，创建新的输出目录
        rmtree("dist", ignore_errors=True)
        Path("dist").mkdir()
        # 生成 requirements.txt 文件
        create_requirements_txt(output_file=requirements_txt)
        # 获取外部已安装模块列表
        installed_modules = get_installed_modules(module_list_file=requirements_txt)
        # 合并外部已安装模块列表和本地模块列表，为所有模块列表
        all_modules = installed_modules + self_modules
        # 检查所有模块的导入情况，出现导入失败的模块，则退出
        if check_modules(module=all_modules)[1]:
            raise RuntimeError("发现有导入失败的模块，请通过 uv sync 刷新项目依赖")
        # 获取 Nuitka 编译命令并执行
        build_with_nuitka(
            input_file="main.py",
            output_file="newsphoto",
            icon_file="icons/icon-light",
        )
        build_with_nuitka(
            input_file="save-as-image.py",
            output_file="save-as-image",
            icon_file="icons/icon-dark",
            include_browser=True,
        )
        # 复制资源文件
        print("\n正在复制资源文件...")
        copytree(Path("sources"), Path(output_dirname) / "sources")
    except KeyboardInterrupt:
        raise ("用户中断了操作，正在退出")
    except Exception as e:
        raise (e)
    finally:
        Path(requirements_txt).unlink()


if __name__ == "__main__":
    main()
