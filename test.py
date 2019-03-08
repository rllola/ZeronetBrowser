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

    def test_webview(self):
        from PyQt5.QtWebEngineWidgets import QWebEngineView
        from PyQt5.QtCore import QUrl, QTimer

        app = QApplication([])
        view = QWebEngineView()
        # Use a raw string to avoid accidental special characters in Windows filenames:
        # ``c:\temp`` is `c<tab>emp`!
        view.load(QUrl("http://www.pyinstaller.org"))
        view.show()

        view.page().loadFinished.connect(
            # Display the web page for one second after it loads.
            lambda ok: QTimer.singleShot(5000, app.quit))
        app.exec_()



if __name__ == '__main__':
    unittest.main()
