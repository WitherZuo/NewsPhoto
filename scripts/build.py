#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import importlib
import pathlib
import platform
import shutil
import subprocess
import sys

# 添加本地模块路径
sys.path.append(".")

# 创建不同类别模块列表
installed_modules = []
imported_modules = []
failed_modules = []

# 处理模块名称与导入名称不一致的情况
module_alias = {
    "pillow": "PIL",
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


# 返回 Nuitka 编译命令并执行
def build_with_nuitka(input_file, output_file, icon_file):
    # 通过 uv 运行 nuitka 基础命令
    nuitka_exec = ["uv", "run", "nuitka"]
    # 所有平台的公共参数
    common_args = [
        "--onefile",
        f"{input_file}",
        "--remove-output",
        "--output-dir=dist",
        "--assume-yes-for-downloads",
    ]

    platform_args = []
    system = platform.system().lower()

    match system:
        # Windows 特定参数
        case "windows":
            args = [
                f"--output-filename={output_file}.exe",
                "--lto=yes",
                f"--windows-icon-from-ico={icon_file}",
            ]

        # macOS 特定参数
        case "darwin":
            args = [
                f"--output-filename={output_file}",
                f"--macos-app-icon={icon_file}",
            ]
        # Linux 特定参数
        case "linux":
            args = [
                f"--output-filename={output_file}",
                "--lto=yes",
                f"--linux-icon={icon_file}",
            ]
        # 不支持的操作系统
        case _:
            raise RuntimeError(f"不支持的操作系统：{system}")

    # 合并所有参数
    platform_args.extend(args)
    cmd = nuitka_exec + common_args + platform_args
    # 执行编译命令
    print(f"\n正在编译：{input_file}")
    print(f"执行命令：{cmd}\n")
    subprocess.run(cmd, check=True)

    return cmd


# 函数：检查 uv 是否安装
def check_uv():
    print("检查本机是否安装 uv...")
    try:
        uv_install = shutil.which("uv")
        print(f"uv 已安装：{uv_install}\n")
    except Exception as e:
        print(e)
        raise FileNotFoundError(
            "本机上没有找到 uv。本项目由 uv 管理，请先安装 uv 后重试"
        )


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
        print(e)


# 函数：获取外部已安装模块
def get_installed_modules(module_list_file):
    # 以只读模式打开 requirements.txt 文件
    with open(module_list_file, "r", encoding="utf-8") as requirements:
        # 读取每一行模块定义，以 = 分割，取模块名称部分，处理别名后添加到已安装模块列表
        for line in requirements.readlines():
            module = line.split("==")[0]
            if module in module_alias:
                module = module_alias[module]
            installed_modules.append(module)

    return installed_modules


# 函数：检查模块是否能被导入
def check_modules(module):
    # 遍历所有模块，尝试导入
    for installed_module in module:
        print(f"尝试导入模块：{installed_module}...")
        try:
            result = importlib.import_module(installed_module)
            print(result)
            print(f"🟢 模块 {installed_module} 已安装，且可以被导入。\n")
            # 导入成功，添加到已导入模块列表
            imported_modules.append(installed_module)
        except Exception as e:
            print(e)
            print(f"🔴 模块 {installed_module} 无法被导入！\n")
            # 导入失败，添加到导入失败模块列表
            failed_modules.append(installed_module)

    return imported_modules, failed_modules


# 主函数
def main():
    try:
        # 定义 requirements.txt 文件路径
        requirements_txt = (
            pathlib.Path().resolve() / "dist" / "requirements.txt"
        )

        # 检查 uv 是否安装
        check_uv()

        # 删除上一次输出目录，创建新的输出目录
        shutil.rmtree("dist", ignore_errors=True)
        pathlib.Path("dist").mkdir()

        # 生成 requirements.txt 文件
        create_requirements_txt(output_file=requirements_txt)

        # 获取外部已安装模块列表
        installed_modules = get_installed_modules(
            module_list_file=requirements_txt
        )
        # 合并外部已安装模块列表和本地模块列表，为所有模块列表
        all_modules = installed_modules + self_modules
        # 检查所有模块的导入情况
        success, fail = check_modules(module=all_modules)

        # 输出导入成功和失败的模块列表
        print(f"这些模块导入成功：{success}")
        print(f"这些模块导入失败：{fail}")

        # 如果出现导入失败的模块，则退出并返回错误码 1
        if len(fail) > 0:
            raise RuntimeError(
                "发现有导入失败的模块，请通过 uv sync 刷新项目依赖"
            )

        # 获取 Nuitka 编译命令并执行
        build_with_nuitka(
            input_file="main.py",
            output_file="newsphoto",
            icon_file="icons/icon-light.png",
        )
        build_with_nuitka(
            input_file="save-as-image.py",
            output_file="save-as-image",
            icon_file="icons/icon-dark.png",
        )
    except Exception as e:
        print(e)
        sys.exit(1)
    finally:
        pathlib.Path(requirements_txt).unlink()


if __name__ == "__main__":
    main()
