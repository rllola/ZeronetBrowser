#!/bin/bash

echo "=========== Install SIP ==========="
wget -nv https://sourceforge.net/projects/pyqt/files/sip/sip-4.19.13/sip-4.19.13.tar.gz
tar -xvzf sip-4.19.13.tar.gz
cd sip-4.19.13
python configure.py --sip-module=PyQt5.sip
make -j 8
sudo make install
sudo touch /usr/lib/python2.7/dist-packages/PyQt5/__init__.py
echo "Done !"

cd ..

echo "=========== Install PyQt5 ==========="
wget -nv https://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.11.2/PyQt5_gpl-5.11.2.tar.gz
tar -xvzf PyQt5_gpl-5.11.2.tar.gz
cd PyQt5_gpl-5.11.2
python configure.py --confirm-license --disable=QtNfc --qmake=/opt/qt511/bin/qmake -n PyQt5.sip
make -j 8
sudo make install
echo "Done !"
