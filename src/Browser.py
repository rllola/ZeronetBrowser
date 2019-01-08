from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Browser(QWebEngineView):
    def __init__(self, *args, **kwargs):
        super(Browser,self).__init__(*args, **kwargs)

    def can_go_back(self):
        return self.history().canGoBack()

    def can_go_forward(self):
        return self.history().canGoForward()
