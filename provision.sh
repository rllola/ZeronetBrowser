#!/usr/bin/env bash

echo "===== INSTALL DEPENDENCIES ====="
sudo apt update
sudo apt install -y python-pip msgpack-python python-gevent python-pyqt5 python-pyqt5.qtwebengine python-pyqt5.qtwebkit

echo "===== INSTALL PYINSTALLER ====="
sudo pip install pyinstaller
