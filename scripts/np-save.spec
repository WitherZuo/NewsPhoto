# -*- mode: python ; coding: utf-8 -*-
import sys

os_name = sys.platform

if os_name == "win32":
    a = Analysis(
        ["..\\save-as-image.py"],
        pathex=[],
        binaries=[],
        datas=[],
        hiddenimports=[],
        hookspath=[],
        hooksconfig={},
        runtime_hooks=[],
        excludes=[],
        noarchive=False,
        optimize=2,
    )
elif os_name == "darwin" or os_name == "linux":
    a = Analysis(
        ["../save-as-image.py"],
        pathex=[],
        binaries=[],
        datas=[],
        hiddenimports=[],
        hookspath=[],
        hooksconfig={},
        runtime_hooks=[],
        excludes=[],
        noarchive=False,
        optimize=2,
    )

pyz = PYZ(a.pure)

if os_name == "win32":
    exe = EXE(
        pyz,
        a.scripts,
        a.binaries,
        a.datas,
        [("O", None, "OPTION"), ("O", None, "OPTION")],
        name=".\\dist\\np-save",
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        upx_exclude=[],
        runtime_tmpdir=None,
        console=True,
        disable_windowed_traceback=False,
        argv_emulation=False,
        target_arch=None,
        codesign_identity=None,
        entitlements_file=None,
        icon=["..\\icons\\icon-dark.ico"],
    )
elif os_name == "darwin":
    exe = EXE(
        pyz,
        a.scripts,
        a.binaries,
        a.datas,
        [("O", None, "OPTION"), ("O", None, "OPTION")],
        name="./dist/np-save",
        debug=False,
        bootloader_ignore_signals=False,
        strip=True,
        upx=False,
        upx_exclude=[],
        runtime_tmpdir=None,
        console=True,
        disable_windowed_traceback=False,
        argv_emulation=False,
        target_arch=None,
        codesign_identity=None,
        entitlements_file=None,
        icon=["../icons/icon-dark.icns"],
    )
elif os_name == "linux":
    exe = EXE(
        pyz,
        a.scripts,
        a.binaries,
        a.datas,
        [("O", None, "OPTION"), ("O", None, "OPTION")],
        name="./dist/np-save",
        debug=False,
        bootloader_ignore_signals=False,
        strip=True,
        upx=False,
        upx_exclude=[],
        runtime_tmpdir=None,
        console=True,
        disable_windowed_traceback=False,
        argv_emulation=False,
        target_arch=None,
        codesign_identity=None,
        entitlements_file=None,
    )
else:
    print(f"Unsupported operating system: {os_name}")
    sys.exit(1)
