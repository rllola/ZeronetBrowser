#!/usr/bin/env bash

echo "===== INSTALL DEPENDENCIES ====="
sudo apt update
sudo apt install -y python-pip msgpack-python python-gevent python-dev
sudo pip install enum34

echo "===== INSTALL PYQT5 ====="
sudo add-apt-repository --yes ppa:ubuntu-sdk-team/ppa
sudo apt-get update -qq

# Install Qt5, QtMultimedia and QtSvg
sudo apt-get install -qq qtdeclarative5-dev libqt5svg5-dev qtmultimedia5-dev
export QMAKE=/usr/lib/x86_64-linux-gnu/qt5/bin/qmake

# Library versions
PYQT_VERSION=5.11.3
SIP_VERSION=4.19.13

# Install sip
wget --retry-connrefused https://sourceforge.net/projects/pyqt/files/sip/sip-$SIP_VERSION/sip-$SIP_VERSION.tar.gz
tar -xzf sip-$SIP_VERSION.tar.gz
cd sip-$SIP_VERSION
python configure.py
make
sudo make install
cd ..

# Install PyQt5
wget --retry-connrefused https://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-$PYQT_VERSION/PyQt5_gpl-$PYQT_VERSION.tar.gz
tar -xzf PyQt5_gpl-$PYQT_VERSION.tar.gz
cd PyQt5_gpl-$PYQT_VERSION
python configure.py --confirm-license --qmake=/usr/lib/x86_64-linux-gnu/qt5/bin/qmake --sip-module PyQt5.sip --no-tools
make
sudo make install

echo "===== INSTALL PYINSTALLER ====="
sudo pip install pyinstaller
