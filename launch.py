#!/usr/bin/python

import sys
import os.path
from MainWindow import MainWindow
from ZeroNet import zeronet
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
from multiprocessing import Process
import time

if __name__ == '__main__':

    print("Python sys.executable:\n\t%s" % sys.executable)
    print("Python sys.path:\n\t%s" % "\n\t".join(sys.path))
    print('Qt5 Libraries path:\n\t%s' % \
            QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.LibrariesPath))
    print('Qt5 Library Executables path:\n\t%s' % \
            QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.LibraryExecutablesPath))
    print('Qt5 Binaries path:\n\t%s' % \
            QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.BinariesPath))
    print('Qt5 Data path:\n\t%s' % \
            QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.DataPath))
    print('Qt5 Imports path:\n\t%s' % \
            QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.ImportsPath))
    print('Qt5 Plugins path:\n\t%s' % \
            QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.PluginsPath))
    print('Qt5 Settings path:\n\t%s' % \
            QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.SettingsPath))
    print('Qt5 Prefix path:\n\t%s' % \
            QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.PrefixPath))

    # Create a process for Zeronet
    p = Process(target=zeronet.main)
    p.start()

    time.sleep(5)

    print os.environ['PATH']
    print sys.path

    # Start the PyQt application
    app = QApplication(sys.argv)
    print("Python sys.executable:\n\t%s" % sys.executable)
    print("Python sys.path:\n\t%s" % "\n\t".join(sys.path))
    print('Qt5 Libraries path:\n\t%s' % \
            QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.LibrariesPath))
    print('Qt5 Library Executables path:\n\t%s' % \
            QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.LibraryExecutablesPath))
    print('Qt5 Binaries path:\n\t%s' % \
            QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.BinariesPath))
    print('Qt5 Data path:\n\t%s' % \
            QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.DataPath))
    print('Qt5 Imports path:\n\t%s' % \
            QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.ImportsPath))
    print('Qt5 Plugins path:\n\t%s' % \
            QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.PluginsPath))
    print('Qt5 Settings path:\n\t%s' % \
            QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.SettingsPath))
    print('Qt5 Prefix path:\n\t%s' % \
            QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.PrefixPath))
    print("Qt5 app.libraryPaths():\n\t%s" % "\n\t".join((app.libraryPaths())))
    mainWindow = MainWindow()
    app.exec_()

    # Shutdown Zeronet
    p.terminate()
