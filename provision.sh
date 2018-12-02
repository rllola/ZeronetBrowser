#!/usr/bin/env bash

echo "===== INSTALL DEPENDENCIES ====="
sudo apt update
sudo apt install -y python-pip msgpack-python python-gevent python-dev
sudo pip install enum34

echo "===== INSTALL PYQT5 ====="
sudo add-apt-repository --yes ppa:beineri/opt-qt-5.11.2-xenial
sudo apt-get update

# Install Qt5, QtWebEngine and QtSvg
sudo apt-get install -y msgpack-python python-gevent python-dev build-essential libgl1-mesa-dev qt511-meta-minimal qt511webengine qt511svg

chmod +x ./Browser/get-pyqt5-linux.sh
./Browser/get-pyqt5-linux.sh

echo "===== INSTALL PYINSTALLER ====="
#export LC_ALL="en_US.UTF-8"
#export LC_CTYPE="en_US.UTF-8"
#sudo dpkg-reconfigure locales
sudo pip install pyinstaller
# Avoid missing _vendor.sox error
sudo pip install --upgrade setuptools
