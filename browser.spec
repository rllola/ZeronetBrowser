# -*- mode: python -*-

from PyInstaller.utils.hooks import collect_data_files
from sys import platform

block_cipher = None

datas = Tree('ZeroNet', prefix='ZeroNet', excludes=['.github','*.pyc', 'data', 'log'])
datas += Tree('icons', prefix='icons', excludes=[])

a = Analysis(['launch.py'],
             #pathex=['/home/lola/Workspace/ZeroNet/Browser/ZeroNet/src', '/home/lola/Workspace/ZeroNet/Browser/ZeroNet/plugins', '/home/lola/Workspace/ZeroNet/Browser/ZeroNet/src/lib', '/home/lola/Workspace/ZeroNet/Browser'],
             binaries=[],
             datas=[],
             hiddenimports=['gevent', 'ConfigParser', 'json', 'sqlite3', 'msgpack', 'setuptools', 'cgi', 'xml.dom', 'posixpath', 'logging.handlers', 'argparse'],
             #hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['ZeroNet'],
             #excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='ZeronetBrowser',
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )

if platform.startswith("linux"):
    # linux; add .desktop
    datas += [('install.sh', 'install.sh', 'DATA')]

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               datas,
               strip=False,
               upx=True,
               name='ZeronetBrowser')
