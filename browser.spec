# -*- mode: python -*-

from PyInstaller.utils.hooks import collect_data_files
from sys import platform
import os

block_cipher = None

datas = Tree('ZeroNet', prefix='ZeroNet', excludes=['.github','*.pyc', 'data', 'log'])
datas += Tree('icons', prefix='icons', excludes=[])
datas += Tree('data/__plugins__/1AzHmVFhffXjZHexSn78nBpCTJ1wTqskpB', prefix='__plugins__/1AzHmVFhffXjZHexSn78nBpCTJ1wTqskpB', excludes=['.git', '.gitignore'])

a = Analysis(['launch.py'],
             #pathex=['/home/lola/Workspace/ZeroNet/Browser/ZeroNet/src', '/home/lola/Workspace/ZeroNet/Browser/ZeroNet/plugins', '/home/lola/Workspace/ZeroNet/Browser/ZeroNet/src/lib', '/home/lola/Workspace/ZeroNet/Browser'],
             binaries=[],
             datas=[],
             hiddenimports=['gevent', 'configparser', 'json', 'sqlite3', 'msgpack', 'setuptools', 'cgi', 'xml.dom', 'posixpath', 'logging.handlers', 'argparse', 'enum', 'pypiwin32', 'socks', 'bencode', 'sockshandler', 'geventwebsocket', 'merkletools', 'coincurve', 'bitcoin', 'base58', 'bitcoin.signmessage', 'ctypes.wintypes'],
             #hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['ZeroNet'],
             #excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

icon = None
if platform.startswith("darwin"):
  icon = "icons/zeronet-logo.icns"

if platform.startswith("win"):
  icon = "icons\zeronet-logo.ico"

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
          icon=icon,
          console=True )

if platform.startswith("linux"):
    # linux; add .desktop
    datas += [('install.sh', 'install.sh', 'DATA')]

if platform.startswith("win32"):
    for data in a.datas:
        if 'QtWebEngineProcess' in data[0]:
            a.datas[a.datas.index(data)] = (u'PyQt5\\Qt\\bin\\'+data[0].split('\\')[-1], data[1], data[2])

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               datas,
               strip=False,
               upx=True,
               name='ZeronetBrowser')

version = '0.0.0'

if os.environ.get('TRAVIS_TAG'):
    version = os.environ['TRAVIS_TAG'][1:]

app = BUNDLE(coll,
  name='ZeronetBrowser.app',
  icon=icon,
  bundle_identifier=None,
  info_plist={
    'CFBundleVersion': version,
    'CFBundleShortVersionString': version
  })
