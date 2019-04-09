from PyQt5.QtWidgets import QToolBar, QLineEdit, QAction, QShortcut, QToolButton, QMenu
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import QSize

import os
import sys

class NavigationBar(QToolBar):

    def __init__(self, *args, **kwargs):
        super(QToolBar,self).__init__(*args, **kwargs)

        self.setIconSize(QSize(18,18))

        # Going backward button
        self.back_btn = QAction( QIcon(os.path.join('icons','321-arrow-left2.svg')), 'Back', self)
        self.back_btn.setDisabled(True)
        self.addAction(self.back_btn)

        # Going forward button
        self.next_btn = QAction( QIcon(os.path.join('icons','317-arrow-right2.svg')), 'Next', self)
        self.next_btn.setDisabled(True)
        self.addAction(self.next_btn)

        # Reload button
        self.reload_btn = QAction( QIcon(os.path.join('icons','133-spinner11.svg')), 'Reload', self)
        self.addAction(self.reload_btn)

        # Shortcut reload
        self.shortcut_reload = QShortcut(QKeySequence('Ctrl+R'), self)
        self.shortcut_reload_f5 = QShortcut(QKeySequence('F5'), self)

        # Home button
        self.home_btn = QAction( QIcon(os.path.join('icons','001-home.svg')), 'Home', self)
        self.addAction(self.home_btn)

        # Styles
        self.setStyleSheet("QToolBar { padding: 1ex; } QWidget { margin-right: 2ex; } QLineEdit { margin-right: 5ex; padding: 3px; padding-left: 3ex; }")


        #Url bar
        self.url_bar = QLineEdit()
        self.addWidget(self.url_bar)

        # Menu button
        self.menu = QMenu(self)
        self.edit_config_action = QAction('Edit config file', self)
        self.menu.addAction(self.edit_config_action)
        tool_button = QToolButton(self)
        tool_button.setStyleSheet("QToolButton::menu-indicator { image: none; }")
        tool_button.setIcon(QIcon(os.path.join('icons','190-menu.svg')))
        tool_button.setMenu(self.menu)
        tool_button.setPopupMode(QToolButton.InstantPopup)
        self.addWidget(tool_button)
        #self.addAction(self.button_menu)

        # We dont want it to move elsewhere
        self.setMovable(False)
