import PyQt5
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWebKitWidgets import QWebView , QWebPage
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtNetwork import *
from optparse import OptionParser
import os

class Browser(QWebEngineView):
    def __init__(self, *args, **kwargs):
        super(Browser,self).__init__(*args, **kwargs)
        #fname =  os.getcwd()+ '/index.html'
        #self.setUrl(QUrl.fromLocalFile(fname))
        self.setUrl(QUrl("http://127.0.0.1:43110/1HeLLo4uzjaLetFx6NH3PMwFP3qbRbTf3D/"))
        # Hack ! Otherwise the page doesnt properly load
        self.reload()
