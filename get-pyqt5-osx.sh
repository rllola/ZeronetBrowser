#!/bin/bash

echo "=========== Install SIP ==========="
wget -nv https://sourceforge.net/projects/pyqt/files/sip/sip-4.19.13/sip-4.19.13.tar.gz
tar -xvzf sip-4.19.13.tar.gz
cd sip-4.19.13
python configure.py --sip-module=PyQt5.sip
make -j 8
sudo make install
sudo touch /usr/local/Cellar/python@2/2.7.15_1/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/PyQt5/__init__.py
echo "Done !"

cd ..

echo "=========== Install PyQt5 ==========="
wget -nv https://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.11.2/PyQt5_gpl-5.11.2.tar.gz
tar -xvzf PyQt5_gpl-5.11.2.tar.gz
cd PyQt5_gpl-5.11.2
ls /usr/local/Cellar/python@2/2.7.15_1/Frameworks/Python.framework/Versions/2.7/bin/
python configure.py --confirm-license --disable=QtNfc --qmake=/usr/local/opt/qt5/bin/qmake -n PyQt5.sip --sip=/usr/local/Cellar/python@2/2.7.15_1/Frameworks/Python.framework/Versions/2.7/bin/sip
make -j 8
sudo make install
echo "Done !"
