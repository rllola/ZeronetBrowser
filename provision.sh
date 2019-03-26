#!/usr/bin/env bash

echo "===== INSTALL DEPENDENCIES ====="
sudo apt update
sudo apt install -y python3-pip libgl1-mesa-glx libnss3 libxcomposite-dev libxcursor-dev libxi6 libxtst6 libasound2 libegl1-mesa libfontconfig1 libxkbcommon-x11-0

echo "===== INSTALL PYQT5 ====="
pip3 install PyQt5-sip PyQt5 PyQtWebEngine

echo "===== INSTALL ZERONET DEPENDENCIES ====="
cd ./Browser/ZeroNet
pip3 install -r requirements.txt

echo "===== INSTALL PYINSTALLER ====="
#export LC_ALL="en_US.UTF-8"
#export LC_CTYPE="en_US.UTF-8"
#sudo dpkg-reconfigure locales
pip3 install pyinstaller
# Avoid missing _vendor.sox error
#sudo pip install --upgrade setuptools
