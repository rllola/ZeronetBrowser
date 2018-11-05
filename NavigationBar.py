from PyQt5.QtWidgets import QToolBar, QLineEdit, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

import os

class NavigationBar(QToolBar):

    def __init__(self, *args, **kwargs):
        super(QToolBar,self).__init__(*args, **kwargs)

        self.setIconSize(QSize(18,18))

        # Going backward button
        self.back_btn = QAction( QIcon(os.path.join('icons','321-arrow-left2.svg')), 'Back', self)
        # self.back_btn.setDisabled(True)
        self.addAction(self.back_btn)

        # Going forward button
        self.next_btn = QAction( QIcon(os.path.join('icons','317-arrow-right2.svg')), 'Next', self)
        # self.next_btn.setDisabled(True)
        self.addAction(self.next_btn)

        # Reload button
        self.reload_btn = QAction( QIcon(os.path.join('icons','133-spinner11.svg')), 'Reload', self)
        self.addAction(self.reload_btn)

        # Home button
        self.home_btn = QAction( QIcon(os.path.join('icons','001-home.svg')), 'Home', self)
        self.addAction(self.home_btn)

        # Styles
        self.setStyleSheet("QToolBar { padding: 1ex; } QWidget { margin-right: 2ex; } QLineEdit { margin-right: 5ex; padding: 3px; padding-left: 3ex; }")


        #Url bar
        self.url_bar = QLineEdit()
        self.addWidget(self.url_bar)

        # We dont want it to move elsewhere
        self.setMovable(False)
