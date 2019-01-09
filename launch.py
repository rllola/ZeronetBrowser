#!/usr/bin/python

import sys
import os
import ConfigParser
from src.MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication
from multiprocessing import Process, freeze_support
from ZeroNet import zeronet
import time
import imp

# See if it is lock or not
def openLocked(path, mode="w"):
    if os.name == "posix":
        import fcntl
        f = open(path, mode)
        fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
    elif os.name == "nt":
        import msvcrt
        f = open(path, mode)
        msvcrt.locking(f.fileno(), msvcrt.LK_NBLCK, -1)
    else:
        f = open(path, mode)
    return f

if __name__ == '__main__':
    freeze_support()

    url = None
    if len(sys.argv) > 1 and sys.argv[1].startswith('zero:'):
        url = sys.argv[1]
        sys.argv.pop(1)

    p = None

    config = ConfigParser.ConfigParser()
    config.read('browser.conf')

    if not config.has_section('global'):
        config.add_section('global')

        answer = raw_input("Do you already have ZeroNet installed somewhere ? (Y\\N) \n")

        if (answer == 'Y'):
            home = os.path.expanduser("~")
            zeronet_path = False
            for root, dirs, files in os.walk(home):
                if not root.startswith('.'):
                    for dir in dirs:
                        if dir.startswith('ZeroNet'):
                            path = os.path.join(root, dir)
                            answer = raw_input("Is it this path correct "+path+" ?")
                            if (answer == 'Y'):
                                if (os.path.exists(path) and os.path.isdir(path)):
                                    zeronet_path = path
                                    break
                if zeronet_path:
                    config.set('global', 'zeronet_path', zeronet_path)
                    # Create a __init__.py file
                    open(os.path.join(zeronet_path, '__init__.py'), 'w')
                    break
        else:
            config.set('global', 'zeronet_path', '')

        with open('browser.conf', 'wb') as configfile:
            config.write(configfile)

        print "Please restart to load the config"
        sys.exit(0)
    else:
        zeronet_path = config.get('global', 'zeronet_path')
        if zeronet_path:
            try:
                zeronet = imp.load_source('zeronet', os.path.join(zeronet_path, 'zeronet.py'))
            except:
                print "Error - Couldn't load ZeroNet from given path. Loading local ZeroNet."

    if zeronet_path:
        # See if it is already running
        try:
            lock = openLocked("%s/lock.pid" % os.path.join(zeronet_path,'data'), "w")
            lock.close()
            # Create a process for Zeronet using this version of ZeroNet
            p = Process(target=zeronet.main)
            p.start()
        except IOError as err:
            print "Can't open lock file, your ZeroNet client is probably already running, opening browser without starting Zeronet in the background..."
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
