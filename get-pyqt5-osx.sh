#!/bin/bash

NP="$(sysctl -n hw.ncpu)"
PYTHON_EXE=python2
PYTHON_VERSON=2.7

QT5_VERSION=5.11.2
QMAKE_EXE=$(brew --prefix qt)/bin/qmake

PYQTSIP_VERSION=4.19.13
PYQTSIP_CHECKSUM=e353a7056599bf5fbd5d3ff9842a6ab2ea3cf4e0304a0f925ec5862907c0d15e

PYQT5_VERSION=5.11.2
PYQT5_CHECKSUM=7caa581155c3433716b7e6aba71fe1378cd7d92f4155c266d60e5cffb64e9603

echo "=========== Install SIP ==========="
rm -rf sip-$PYQTSIP_VERSION.tar.gz sip-$PYQTSIP_VERSION
wget -nv "https://sourceforge.net/projects/pyqt/files/sip/sip-$PYQTSIP_VERSION/sip-$PYQTSIP_VERSION.tar.gz"
echo "$PYQTSIP_CHECKSUM  sip-$PYQTSIP_VERSION.tar.gz" | shasum -a 256 -c
if [ $? -ne 0 ]
then
   echo "Invalid sip"
   exit 1
fi
tar -xvzf sip-$PYQTSIP_VERSION.tar.gz
cd sip-$PYQTSIP_VERSION
$PYTHON_EXE configure.py --sip-module=PyQt5.sip
make -j $NP
sudo make install
sudo touch "$($PYTHON_EXE-config --prefix)/lib/python$PYTHON_VERSON/site-packages/PyQt5/__init__.py"
echo "Done !"

cd ..

echo "=========== Install PyQt5 ==========="
rm -rf PyQt5_gpl-$PYQT5_VERSION.tar.gz PyQt5_gpl-$PYQT5_VERSION
wget -nv "https://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-$PYQT5_VERSION/PyQt5_gpl-$PYQT5_VERSION.tar.gz"
echo "$PYQT5_CHECKSUM  PyQt5_gpl-$PYQT5_VERSION.tar.gz" | shasum -a 256 -c
if [ $? -ne 0 ]
then
   echo "Invalid PyQt5"
   exit 1
fi
tar -xvzf "PyQt5_gpl-$PYQT5_VERSION.tar.gz"
cd "PyQt5_gpl-$PYQT5_VERSION"
ls "$($PYTHON_EXE-config --prefix)/bin/"
$PYTHON_EXE configure.py --confirm-license --disable=QtNfc --qmake=$QMAKE_EXE -n PyQt5.sip --sip="$($PYTHON_EXE-config --prefix)/bin/sip"
make -j $NP
sudo make install
echo "Done !"
