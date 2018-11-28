#!/usr/bin/env bash

echo "===== INSTALL DEPENDENCIES ====="
sudo apt update
sudo apt install -y python-pip msgpack-python python-gevent python-dev
sudo pip install enum34

echo "===== INSTALL PYQT5 ====="
sudo add-apt-repository --yes ppa:beineri/opt-qt-5.11.2-xenial
sudo apt-get update

# Install Qt5, QtWebEngine and QtSvg
sudo apt-get install -y msgpack-python python-gevent python-dev build-essential libgl1-mesa-dev qt511-meta-minimal qt511webengine qt511svg mlocate

chmod +x ./get-pyst5-linux.sh
./get-pyqt5-linux.sh

echo "===== INSTALL PYINSTALLER ====="
sudo pip install pyinstaller
