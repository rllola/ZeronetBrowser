#!/bin/bash

echo "=========== Install SIP ==========="
wget -nv https://sourceforge.net/projects/pyqt/files/sip/sip-4.19.13/sip-4.19.13.tar.gz
tar -xvzf sip-4.19.13.tar.gz
cd sip-4.19.13
python configure.py
make -j 8
sudo make install
echo "Done !"

cd ..

echo "=========== Install PyQt5 ==========="
wget -nv https://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.10.1/PyQt5_gpl-5.10.1.tar.gz
tar -xvzf PyQt5_gpl-5.10.1.tar.gz
cd PyQt5_gpl-5.10.1
python configure.py --confirm-license --disable=QtNfc --qmake=/opt/qt510/bin/qmake
make -j 8
sudo make install
echo "Done !"
