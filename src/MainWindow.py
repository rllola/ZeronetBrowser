from Browser import Browser
from NavigationBar import NavigationBar
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QToolBar, QTabWidget, QToolButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        url = "http://127.0.0.1:43110/1HeLLo4uzjaLetFx6NH3PMwFP3qbRbTf3D/"
        if "url" in kwargs:
            url = kwargs["url"]
            del kwargs["url"]
        super(MainWindow,self).__init__(*args, **kwargs)

        # Tabs
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)

        # New tab button
        #self.tab_add_button_index = self.tabs.addTab(QWidget(), '+')
        self.add_tab_button = QToolButton()
        self.add_tab_button.setText('+')
        self.add_tab_button.setStyleSheet(
            'QToolButton {border: none; margin: 4px 20px 4px 0px; height: 480px; border-left: 1px solid lightgrey; padding: 0px 4px 0px 4px; font-weight: bold; color: #5d5b59}'
            'QToolButton:hover { background-color: lightgrey }'
            'QToolButton:pressed { background-color: grey }'
            )
        self.add_tab_button.clicked.connect(self.new_tab_clicked)
        self.tabs.setCornerWidget(self.add_tab_button)


        # Navigation bar
        self.navigation = NavigationBar()
        self.navigation.url_bar.returnPressed.connect(self.navigate_to_url)

        # Back
        self.navigation.back_btn.triggered.connect(lambda : self.tabs.currentWidget().back())

        # Next
        self.navigation.next_btn.triggered.connect(lambda : self.tabs.currentWidget().forward())

        # Reload
        self.navigation.reload_btn.triggered.connect(lambda : self.tabs.currentWidget().reload())
        self.navigation.shortcut_reload.activated.connect(lambda : self.tabs.currentWidget().reload())
        self.navigation.shortcut_reload_f5.activated.connect(lambda : self.tabs.currentWidget().reload())

        # Home
        self.navigation.home_btn.triggered.connect(self.go_home)

        # Add new tab
        self.add_new_tab(url, "Home")

        # Get everything fitting in the main window
        self.addToolBar(self.navigation)
        self.setCentralWidget(self.tabs)
        self.show()
        self.setWindowTitle("ZeroNet Browser")
        self.setWindowIcon(QIcon("icons/zeronet-logo.svg"))
        self.showMaximized()

    def contextMenuEvent(self, event):
        print event

    def update_url_bar(self, q, browser=None):

        if browser != self.tabs.currentWidget():
            # If this signal is not from the current tab, ignore
            return

        url_array = q.toString().split('/')[3:]
        formatted_url = '/'.join(str(x) for x in url_array)
        self.navigation.url_bar.setText('zero://' + formatted_url)
        self.navigation.url_bar.setCursorPosition(0)

        if (self.tabs.currentWidget().can_go_back()):
            self.navigation.back_btn.setDisabled(False)
        else:
            self.navigation.back_btn.setDisabled(True)

        if (self.tabs.currentWidget().can_go_forward()):
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

        self.tabs.currentWidget().setUrl(QUrl(url))

    def go_home(self):
        self.tabs.currentWidget().setUrl(QUrl("http://127.0.0.1:43110/1HeLLo4uzjaLetFx6NH3PMwFP3qbRbTf3D/"))

    def new_tab_clicked(self):
        self.add_new_tab("http://127.0.0.1:43110/1HeLLo4uzjaLetFx6NH3PMwFP3qbRbTf3D/", "Home")

    def add_new_tab(self, qurl, label):
        # Instead of browser it should be called WebView !
        browser = Browser()
        browser.urlChanged.connect(lambda qurl, browser=browser: self.update_url_bar(qurl, browser))
        indexTab = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(indexTab)
        # We need to update the url !
        if qurl.startswith('zero://') :
            # ZeroNet protocol
            url_array = qurl.split('/')
            qurl = 'http://127.0.0.1:43110/' + url_array[2]
        elif qurl.startswith('http://'):
            # http protocol
            pass
        else :
            # Nothing mentionned
            qurl = 'http://127.0.0.1:43110/' + qurl
        self.tabs.currentWidget().setUrl(QUrl(qurl))
        return indexTab

    def close_tab(self, index):
        if self.tabs.count() == 1:
            self.tabs.currentWidget().setUrl(QUrl("http://127.0.0.1:43110/1HeLLo4uzjaLetFx6NH3PMwFP3qbRbTf3D/"))
            return
        self.tabs.removeTab(index)
