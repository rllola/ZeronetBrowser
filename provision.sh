#!/usr/bin/env bash

QT5_VERSION=5.12.0

echo "===== INSTALL DEPENDENCIES ====="
sudo apt update
sudo apt install -y python-pip msgpack-python python-gevent python-dev
sudo pip install enum34

echo "===== INSTALL PYQT5 ====="
sudo add-apt-repository --yes ppa:beineri/opt-qt-$QT5_VERSION-xenial
sudo apt-get update

# Install Qt5, QtWebEngine and QtSvg
sudo apt-get install -y build-essential libgl1-mesa-dev qt512-meta-minimal qt512webengine qt512svg

sudo chmod +x /opt/qt512/bin/qt512-env.sh
/opt/qt512/bin/qt512-env.sh

chmod +x ./Browser/get-pyqt5-linux.sh
./Browser/get-pyqt5-linux.sh

echo "===== INSTALL PYINSTALLER ====="
#export LC_ALL="en_US.UTF-8"
#export LC_CTYPE="en_US.UTF-8"
#sudo dpkg-reconfigure locales
sudo pip install pyinstaller
# Avoid missing _vendor.sox error
sudo pip install --upgrade setuptools
