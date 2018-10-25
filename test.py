import unittest
import sys
import PyQt5
from PyQt5.QtWidgets import QApplication

class TestBuild(unittest.TestCase):

    def test_pyqt5(self):
        app = QApplication(sys.argv)

if __name__ == '__main__':
    unittest.main()
