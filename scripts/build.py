#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import sys
from pathlib import Path
from shutil import copytree, rmtree, which

# 构建配置目录
spec_path = "scripts"
# 编译产物输出目录名
output_dirname = "dist"


# 函数：检查 uv 是否安装
def check_uv():
    print("检查本机是否安装 uv...")
    uv_install = which("uv")
    if uv_install != None:
        print(f"uv 已安装：{uv_install}")
    else:
        raise FileNotFoundError("未找到 uv。本项目由 uv 管理，请先安装 uv 后重试")


# 函数：检查 upx 是否安装
def check_upx():
    print("检查本机是否安装 upx...")
    upx_exe = which("upx")
    if upx_exe != None:
        print(f"upx 已安装：{upx_exe}")
    else:
        print(
            "未找到 upx，跳过程序压缩。建议安装 upx 来减小最终产物体积，安装方法请参考：https://upx.github.io/"
        )

    return upx_exe


# 返回 PyInstaller 生成命令并执行
def build_with_pyinstaller(spec_file, include_browser=False):
    # 获取构建配置文件路径
    spec_file_path = Path(spec_path) / f"{spec_file}.spec"
    if not spec_file_path.exists():
        raise FileNotFoundError(f"未找到 spec 文件：{spec_file_path}")

    # 通过 uv 运行 PyInstaller，所有平台的公共参数
    pyinstaller_cmd = [
        "uv",
        "run",
        "pyinstaller",
        f"{spec_file_path}",
        f"--distpath={output_dirname}",
    ]
    # 特定系统的参数，获取 Playwright 浏览器路径
    system = sys.platform

    match system:
        # Windows
        case "win32":
            check_upx()
            browser_path = Path.home() / "AppData" / "Local" / "ms-playwright"
        # macOS
        case "darwin":
            browser_path = Path.home() / "Library" / "Caches" / "ms-playwright"
        # Linux
        case "linux":
            browser_path = Path.home() / ".cache" / "ms-playwright"
        # 不支持的操作系统
        case _:
            raise RuntimeError(f"不支持的操作系统：{system}")

    # 执行生成命令，如果 include_browser 为 True，则复制浏览器到 dist 目录
    print(f"\n正在生成：{spec_file}")
    print(f"执行命令：{' '.join(pyinstaller_cmd)}\n")

    subprocess.run(pyinstaller_cmd, check=True)

    if include_browser:
        print("\n正在复制浏览器文件...")
        copytree(browser_path, Path(output_dirname) / "browser")

    return pyinstaller_cmd


# 主函数
def main():
    try:
        # 检查 uv 是否安装
        check_uv()
        # 删除上一次输出目录，创建新的输出目录
        rmtree("dist", ignore_errors=True)
        Path("dist").mkdir()
        # 获取 PyInstaller 编译命令并执行
        build_with_pyinstaller(
            spec_file="np-gen",
            include_browser=False,
        )
        build_with_pyinstaller(
            spec_file="np-save",
            include_browser=True,
        )
    except KeyboardInterrupt:
        raise ("\n用户中断了操作，正在退出")
    except Exception as e:
        raise (e)
    finally:
        pass


if __name__ == "__main__":
    main()
