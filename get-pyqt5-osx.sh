#!/bin/bash
NP="$(sysctl -n hw.ncpu)"

PYQTSIP_VERSION=4.19.14

QT5_VERSION=5.12

echo "=========== Install SIP ==========="
wget -nv https://www.riverbankcomputing.com/static/Downloads/sip/sip-$PYQTSIP_VERSION.tar.gz
tar -xvzf sip-$PYQTSIP_VERSION.tar.gz
cd sip-$PYQTSIP_VERSION
python configure.py --sip-module=PyQt5.sip
make -j $NP
sudo make install
sudo touch /usr/local/Cellar/python@2/2.7.15_1/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/PyQt5/__init__.py
echo "Done !"

cd ..

echo "=========== Install PyQt5 ==========="
wget -nv https://www.riverbankcomputing.com/static/Downloads/PyQt5/PyQt5_gpl-$QT5_VERSION.tar.gz
tar -xvzf PyQt5_gpl-$QT5_VERSION.tar.gz
cd PyQt5_gpl-$QT5_VERSION
ls /usr/local/Cellar/python@2/2.7.15_1/Frameworks/Python.framework/Versions/2.7/bin/
DYLD_LIBRARY_PATH=/usr/local/opt/qt5/lib python configure.py --confirm-license --no-docstrings --no-designer-plugin --no-tools --enable=QtWidgets --enable=QtCore --enable=QtGui --enable=QtPrintSupport --enable=QtPositioning --enable=QtNetwork --enable=QtQuick --enable=QtQuickWidgets --enable=QtWebChannel --enable=QtQml --qmake=/usr/local/opt/qt5/bin/qmake --sip=/usr/local/Cellar/python@2/2.7.15_1/Frameworks/Python.framework/Versions/2.7/bin/sip QMAKE_LFLAGS_RPATH=
make -j $NP
sudo make install
echo "Done !"

cd ..

echo "=========== Install PyQtWebEngine ==========="
wget -nv https://www.riverbankcomputing.com/static/Downloads/PyQtWebEngine/PyQtWebEngine_gpl-$QT5_VERSION.tar.gz
tar -xvzf PyQtWebEngine_gpl-$QT5_VERSION.tar.gz
cd PyQtWebEngine_gpl-$QT5_VERSION
DYLD_LIBRARY_PATH=/usr/local/opt/qt5/lib python configure.py --qmake=/usr/local/opt/qt5/bin/qmake --sip=/usr/local/Cellar/python@2/2.7.15_1/Frameworks/Python.framework/Versions/2.7/bin/sip
make -j $NP
sudo make install
echo "Done !"
