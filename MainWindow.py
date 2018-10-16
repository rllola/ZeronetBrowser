from Browser import Browser
from NavigationBar import NavigationBar
from PyQt5.QtWidgets import QMainWindow, QToolBar

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)

        # Browser view
        self.browser = Browser()
        self.browser.urlChanged.connect(self.update_url_bar)

        # Navigation bar
        self.navigation = NavigationBar()

        # Get everything fitting in the main window
        self.addToolBar(self.navigation)
        self.setCentralWidget(self.browser)
        self.show()
        self.setWindowTitle("ZeroNet Browser")
        self.showMaximized()

    def update_url_bar(self, q):
        url_array = q.toString().split('/')[3:]
        formatted_url = '/'.join(str(x) for x in url_array)
        self.navigation.url_bar.setText('zero://' + formatted_url)
