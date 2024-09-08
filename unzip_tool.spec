# -*- mode: python ; coding: utf-8 -*-
import os
import shutil
import sys
from PyInstaller.utils.hooks import collect_all

block_cipher = None

# 获取当前工作目录
current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

# 手动指定 tkinterdnd2 的路径（你可能需要调整这个路径）
try:
    import tkinterdnd2
    tkdnd_path = os.path.join(os.path.dirname(tkinterdnd2.__file__), 'tkdnd')
except ImportError:
    tkdnd_path = os.path.join(sys.prefix, 'Lib', 'site-packages', 'tkinterdnd2', 'tkdnd')

# 收集 tkinterdnd2 的所有文件
tkdnd_datas = collect_all('tkinterdnd2')

a = Analysis(['main.py'],
             pathex=[current_dir],
             binaries=[],
             datas=[
                 (os.path.join(current_dir, 'icon.ico'), '.'), 
                 (os.path.join(current_dir, 'github.png'), '.'), 
                 (tkdnd_path, 'tkdnd')  # 包含 tkinterdnd2 的文件夹
             ] + tkdnd_datas[0],  # 添加 tkinterdnd2 的数据文件
             hiddenimports=['tkinter', 'tkinter.ttk', 'tkinterdnd2'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='yt解压工具',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None,
          icon=os.path.join(current_dir, 'icon.ico'))

# 添加代码来复制 tkdnd 文件夹到输出目录
output_path = os.path.join('dist', 'tkdnd')
if not os.path.exists(output_path):
    shutil.copytree(tkdnd_path, output_path)
