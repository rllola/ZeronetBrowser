from Browser import Browser
from NavigationBar import NavigationBar
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QToolBar, QTabWidget, QToolButton, QWidget
from PyQt5.QtCore import QUrl

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)

        # Tabs
        self.tabs = QTabWidget()
        
        # New tab button
        self.tab_add_button_index = self.tabs.addTab(QWidget(), '+')
        self.tabs.tabBarClicked.connect(self.tab_bar_clicked)

        # Add new tab
        index = self.add_new_tab("http://127.0.0.1:43110/1HeLLo4uzjaLetFx6NH3PMwFP3qbRbTf3D/", "Home")
        self.tabs.setCurrentIndex(0)


        # Browser view
        # self.tabs.currentWidget().urlChanged.connect(self.update_url_bar)

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

        # Get everything fitting in the main window
        self.addToolBar(self.navigation)
        self.setCentralWidget(self.tabs)
        self.show()
        self.setWindowTitle("ZeroNet Browser")
        self.showMaximized()

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

    def tab_bar_clicked(self, index):
        if index == self.tab_add_button_index:
            self.add_new_tab("http://127.0.0.1:43110/1HeLLo4uzjaLetFx6NH3PMwFP3qbRbTf3D/", "Home")


    def add_new_tab(self, qurl, label):
        browser = Browser()
        index = self.tab_add_button_index
        # Not really optimize. Should query for position.
        # indexOf(QWidget *w) ?
        self.tab_add_button_index += 1

        browser.urlChanged.connect(lambda qurl, browser=browser: self.update_url_bar(qurl, browser))
        return self.tabs.insertTab(index, browser, label)
