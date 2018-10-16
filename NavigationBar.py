from PyQt5.QtWidgets import QToolBar, QLineEdit

class NavigationBar(QToolBar):

    def __init__(self, *args, **kwargs):
        super(QToolBar,self).__init__(*args, **kwargs)

        self.url_bar = QLineEdit()
        self.addWidget(self.url_bar)

        # We dont want it to move elsewhere
        self.setMovable(False)
