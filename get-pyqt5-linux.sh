#!/bin/bash

echo "=========== Install QT5 ==========="
sudo add-apt-repository --yes ppa:ubuntu-sdk-team/ppa
sudo apt-get update -qq

# Install Qt5, QtMultimedia and QtSvg
sudo apt-get install -qq qtdeclarative5-dev libqt5svg5-dev qtmultimedia5-dev

echo "=========== Install SIP ==========="
wget https://sourceforge.net/projects/pyqt/files/sip/sip-4.19.13/sip-4.19.13.tar.gz
tar -xvzf sip-4.19.13.tar.gz
cd sip-4.19.13
python configure.py
make
sudo make install
echo "Done !"

cd ..

echo "=========== Install PyQt5 ==========="
wget https://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.10.1/PyQt5_gpl-5.10.1.tar.gz
tar -xvzf PyQt5_gpl-5.10.1.tar.gz
cd PyQt5_gpl-5.10.1
python configure.py --confirm-license --disable=QtNfc --qmake=/usr/lib/x86_64-linux-gnu/qt5/bin/qmake
make
sudo make install
echo "Done !"
