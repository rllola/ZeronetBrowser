from Browser import Browser
from PyQt5.QtWidgets import QMainWindow, QGridLayout

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)

        self.browser = Browser()

        self.setCentralWidget(self.browser)
        self.show()
        self.setWindowTitle("ZeroNet Browser")
        self.showMaximized()
