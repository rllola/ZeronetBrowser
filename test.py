import unittest
import sys

from PyQt5.QtWidgets import QApplication

class TestBuild(unittest.TestCase):

    def test_pyqt5(self):
        # Need access to screen
        # app = QtWidgets.QApplication(sys.argv)
        pass

    def test_import_qtwebengine(self):
        from PyQt5.QtWebEngineWidgets import QWebEngineView



if __name__ == '__main__':
    unittest.main()
