#!/usr/bin/python

import sys
import os.path
from MainWindow import MainWindow
from ZeroNet import zeronet
from PyQt5.QtWidgets import QApplication
from multiprocessing import Process
import time

if __name__ == '__main__':
    # Create a process for Zeronet
    p = Process(target=zeronet.main)
    p.start()

    #time.sleep(5)

    # Start the PyQt application
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    app.exec_()

    # Shutdown Zeronet
    p.terminate()
