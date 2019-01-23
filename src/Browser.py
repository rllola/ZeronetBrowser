from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtWidgets import QMenu

class Browser(QWebEngineView):
    def __init__(self, *args, **kwargs):
        super(Browser,self).__init__(*args, **kwargs)
        print dir(self)
        openLinkInNewTabAction = self.pageAction(QWebEnginePage.OpenLinkInNewTab)
        openLinkInNewTabAction.triggered.connect(self.openLinkInNewTabTriggered)
        self.addAction(openLinkInNewTabAction)
        print self.actions()

    def can_go_back(self):
        return self.history().canGoBack()

    def can_go_forward(self):
        return self.history().canGoForward()

    def openLinkInNewTabTriggered(self):
        print "lol"
