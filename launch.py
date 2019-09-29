#!/usr/bin/python

import sys
import os
import configparser
import errno

from PyQt5.QtCore import QLibraryInfo, QCoreApplication
from PyQt5.QtWidgets import QApplication
from src.MainWindow import MainWindow
from src.version import VERSION
from src.UpdateNotification import UpdateNotification
from multiprocessing import Process, freeze_support

import time
import imp

# version1 > version2 --> True (outdated)
# Else --> False
def compare_version(version1, version2):
    version1 = version1.split('.')
    version2 = version2.split('.')

    if version1[0] > version2[0]:
        return True
    elif version2[0] > version1[0]:
        return False
    elif version1[1] > version2[1]:
        return True
    elif version2[1] > version1[1]:
        return False
    elif version1[2] > version2[2]:
        return True
    elif version2[2] > version1[2]:
        return False
    else:
        return False

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

    use_internal_zeronet = config.getboolean('global', 'use_internal_zeronet', fallback=True)
    zeronet_base_url = config.get('global', 'zeronet_base_url', fallback="http://127.0.0.1:43110")
    zeronet_base_url = zeronet_base_url.rstrip("/")
    auto_update = config.get('browser', 'auto_update', fallback=True)

    if use_internal_zeronet:
        from ZeroNet import zeronet
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

    kwargs["homepage"] = config.get('global', 'homepage', fallback='1HeLLo4uzjaLetFx6NH3PMwFP3qbRbTf3D')
    kwargs["zeronet_base_url"] = zeronet_base_url

    # Start the PyQt application
    app = QApplication(sys.argv)
    mainWindow = MainWindow(**kwargs)

    if auto_update and sys.platform.startswith('linux'):
        import requests
        r = requests.get('https://api.update.rocks/update/github.com/rllola/ZeronetBrowser/stable/linux/{}'.format(VERSION))
        response = r.json()
        if response['url']:
            latest_version = response['url'].split('/')[-2][1:]
            if latest_version.startswith('v'):
                outdated = compare_version(latest_version, VERSION)
                if outdated:
                    update_dialog = UpdateNotification(response['url'])
                    update_dialog.open()

    app.exec_()

    if p:
        # Shutdown Zeronet if runingin the background
        p.terminate()
