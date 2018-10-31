import unittest
import sys

from PyQt5.QtCore import QUrl

print sys.path
print sys.modules

from PyQt5 import QtWidgets

# from PyQt5.QtWidgets import QApplication

class TestBuild(unittest.TestCase):

    def test_pyqt5(self):
        # Need access to screen
        # app = QtWidgets.QApplication(sys.argv)
        pass

if __name__ == '__main__':
    unittest.main()
