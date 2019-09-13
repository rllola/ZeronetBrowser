#!/usr/bin/python

import sys
import os
import configparser
import errno

from PyQt5.QtCore import QLibraryInfo, QCoreApplication
from PyQt5.QtWidgets import QApplication
from src.MainWindow import MainWindow
from multiprocessing import Process, freeze_support
from ZeroNet import zeronet
import time
import imp

def osx_first_run():
    zeronet_browser_path = os.path.join(os.path.expanduser("~"), "Library", "Application Support", "Zeronet Browser")

    try:
        os.makedirs(zeronet_browser_path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    try:
        os.makedirs(os.path.join(zeronet_browser_path, "data"))
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    # Create lock.pid file
    open(os.path.join(zeronet_browser_path, "lock.pid"), "w").close()

    # Create zeronet.conf file
    f = open(os.path.join(zeronet_browser_path, "zeronet.conf"), 'w')
    f.write("[global]\n")
    f.write("data_dir = {} \n".format(zeronet_browser_path))
    f.close()


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

    # Adding plugin repo (The plugins could placed somewhere else)
    app_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, os.path.join(app_dir,"ZeroNet"))  # Imports relative to ZeroNet

    url = None
    if len(sys.argv) > 1 and sys.argv[1].startswith('zero:'):
        url = sys.argv[1]
        sys.argv.pop(1)

    p = None

    config = configparser.ConfigParser()

    zeronet_path = None
    conf_path = None

    if sys.platform.startswith("linux") and not os.environ.get("DEV"):
        conf_path = os.path.join(os.sep, os.path.expanduser("~"), ".zeronet", "zeronet.conf")
        sys.argv.append("--config_file")
        sys.argv.append(conf_path)
        config.read(conf_path)
    elif sys.platform.startswith("win") and not os.environ.get("DEV"):
        conf_path = os.path.join(os.sep, os.path.expanduser("~"), "AppData","Roaming", "Zeronet Browser", "zeronet.conf")
        sys.argv.append("--config_file")
        sys.argv.append(conf_path)
        config.read(conf_path)
    elif sys.platform.startswith("darwin") and not os.environ.get("DEV"):
        conf_path = os.path.join(os.sep, os.path.expanduser("~"), "Library", "Application Support", "Zeronet Browser", "zeronet.conf")
        if not os.path.isfile(conf_path):
            osx_first_run()
        sys.argv.append("--config_file")
        sys.argv.append(conf_path)
        config.read(conf_path)
    else:
        config.read(os.path.join(os.sep, os.getcwd(), "ZeroNet", "zeronet.conf"))

    try:
        zeronet_path = config.get('global', 'data_dir')
    except configparser.Error:
        zeronet_path = os.path.join(os.getcwd(), "ZeroNet")

    if zeronet_path:
        # See if it is already running
        try:
            lock = openLocked(os.path.join(zeronet_path, "lock.pid"), "w")
            lock.close()
            # Create a process for Zeronet using this version of ZeroNet
            p = Process(target=zeronet.start)
            p.start()
        except BlockingIOError as err:
            print(err)
            print("Can't open lock file, your ZeroNet client is probably already running, opening browser without starting Zeronet in the background...")
    else:
        # Create a process for Zeronet
        p = Process(target=zeronet.start)
        p.start()

    time.sleep(5)

    kwargs = {}
    if url:
        kwargs = {"url": url}

    if zeronet_path:
        kwargs["zeronet_path"] = zeronet_path

    # Start the PyQt application
    app = QApplication(sys.argv)
    mainWindow = MainWindow(**kwargs)
    app.exec_()

    if p:
        # Shutdown Zeronet if runingin the background
        p.terminate()
