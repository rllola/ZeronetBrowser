from Browser import Browser
from NavigationBar import NavigationBar
from PyQt5.QtWidgets import QMainWindow, QToolBar
from PyQt5.QtCore import QUrl

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)

        # Browser view
        self.browser = Browser()
        self.browser.urlChanged.connect(self.update_url_bar)

        # Navigation bar
        self.navigation = NavigationBar()
        self.navigation.url_bar.returnPressed.connect(self.navigate_to_url)

        # Back
        self.navigation.back_btn.triggered.connect(self.browser.back)

        # Next
        self.navigation.next_btn.triggered.connect(self.browser.forward)

        # Reload
        self.navigation.reload_btn.triggered.connect(self.browser.reload)

        # Home
        self.navigation.home_btn.triggered.connect(self.go_home)

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
        self.navigation.url_bar.setCursorPosition(0)

        if (self.browser.can_go_back()):
            self.navigation.back_btn.setDisabled(False)
        else:
            self.navigation.back_btn.setDisabled(True)

        if (self.browser.can_go_forward()):
            self.navigation.next_btn.setDisabled(False)
        else:
            self.navigation.next_btn.setDisabled(True)

    def navigate_to_url(self):
        # Get url
        url = self.navigation.url_bar.text()

        if url.startswith('zero://') :
            # ZeroNet protocol
            url_array = url.split('/')
            url = 'http://127.0.0.1:43110/' + url_array[2]
        elif url.startswith('http://'):
            # http protocol
            pass
        else :
            # Nothing mentionned
            url = 'http://127.0.0.1:43110/' + url

        self.browser.setUrl(QUrl(url))

    def go_home(self):
        self.browser.setUrl(QUrl("http://127.0.0.1:43110/1HeLLo4uzjaLetFx6NH3PMwFP3qbRbTf3D/"))
