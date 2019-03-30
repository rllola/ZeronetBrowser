#!/usr/bin/python

import sys
import os
import configparser

from PyQt5.QtCore import QLibraryInfo, QCoreApplication
from PyQt5.QtWidgets import QApplication
from src.MainWindow import MainWindow
from multiprocessing import Process, freeze_support
from ZeroNet import zeronet
import time
import imp

# See if it is lock or not
def openLocked(path, mode="wb"):
    try:
        if os.name == "posix":
            import fcntl
            f = open(path, mode)
            fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
        elif os.name == "nt":
            import msvcrt
            f = open(path, mode)
            msvcrt.locking(f.fileno(), msvcrt.LK_NBLCK, 1)
        else:
            f = open(path, mode)
    except (IOError, PermissionError, BlockingIOError) as err:
        raise BlockingIOError("Unable to lock file: %s" % err)
    return f


if __name__ == '__main__':
    freeze_support()

    url = None
    if len(sys.argv) > 1 and sys.argv[1].startswith('zero:'):
        url = sys.argv[1]
        sys.argv.pop(1)

    p = None

    config = configparser.ConfigParser()
    config.read(os.path.join(os.sep, os.getcwd(), "ZeroNet", "zeronet.conf"))

    try:
        zeronet_path = config.get('global', 'data_dir')
    except configparser.Error:
        zeronet_path = os.path.join(os.sep, os.getcwd(), "ZeroNet", "data")

    if zeronet_path:
        # See if it is already running
        try:
            lock = openLocked(os.path.join(os.sep, zeronet_path, "lock.pid"), "w")
            lock.close()
            # Create a process for Zeronet using this version of ZeroNet
            p = Process(target=zeronet.main)
            p.start()
        except BlockingIOError as err:
            print(err)
            print("Can't open lock file, your ZeroNet client is probably already running, opening browser without starting Zeronet in the background...")
    else:
        # Create a process for Zeronet
        p = Process(target=zeronet.main)
        p.start()

    time.sleep(5)

    kwargs = {}
    if url :
        kwargs = {"url": url}

    # Start the PyQt application
    app = QApplication(sys.argv)
    mainWindow = MainWindow(**kwargs)
    app.exec_()

    if p:
        # Shutdown Zeronet if runingin the background
        p.terminate()
