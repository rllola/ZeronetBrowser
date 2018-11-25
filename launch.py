#!/usr/bin/python

import sys
import os.path
from MainWindow import MainWindow
from ZeroNet import zeronet
from PyQt5.QtWidgets import QApplication
from multiprocessing import Process, freeze_support
import time

if __name__ == '__main__':
    freeze_support()
    print "Inside main !"
    # Create a process for Zeronet
    p = Process(target=zeronet.main)
    print "Created Process"
    p.start()
    print "Starting Process"

    time.sleep(5)

    print os.environ['PATH']
    print sys.path

    # Start the PyQt application
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    app.exec_()

    # Shutdown Zeronet
    p.terminate()
