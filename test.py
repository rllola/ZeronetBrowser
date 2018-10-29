import unittest
import sys

import PyQt5

print sys.path
print sys.modules

from PyQt5.QtWidgets import QApplication

class TestBuild(unittest.TestCase):

    def test_pyqt5(self):
        # Need access to screen
        #app = QApplication(sys.argv)
        pass

if __name__ == '__main__':
    unittest.main()
