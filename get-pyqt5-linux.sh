#!/bin/bash

echo "=========== Install QT5 ==========="
#wget -nv http://download.qt.io/official_releases/qt/5.10/5.10.1/qt-opensource-linux-x64-5.10.1.run
#chmod +x qt-opensource-linux-x64-5.10.1.run
#sudo ./qt-opensource-linux-x64-5.10.1.run
#qtchooser -print-env
#qmake -v
sudo add-apt-repository --yes ppa:beineri/opt-qt-5.10.1-xenial
sudo apt-get update
sudo apt-get install -qq qt510-meta-full
echo "Done !"

echo "=========== Install SIP ==========="
wget -nv https://sourceforge.net/projects/pyqt/files/sip/sip-4.19.13/sip-4.19.13.tar.gz
tar -xvzf sip-4.19.13.tar.gz
cd sip-4.19.13
python configure.py
make
sudo make install
echo "Done !"

cd ..

echo "=========== Install PyQt5 ==========="
wget -nv https://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.10.1/PyQt5_gpl-5.10.1.tar.gz
tar -xvzf PyQt5_gpl-5.10.1.tar.gz
cd PyQt5_gpl-5.10.1
python configure.py --confirm-license --disable=QtNfc --qmake=/usr/lib/x86_64-linux-gnu/qt5/bin/qmake
make
sudo make install
echo "Done !"
