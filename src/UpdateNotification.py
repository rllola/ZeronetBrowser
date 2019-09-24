from PyQt5.QtWidgets import QDialog, QGridLayout, QLabel
from PyQt5.QtCore import Qt

class UpdateNotification(QDialog):

    def __init__(self, url):
        super(QDialog,self).__init__()

        self.url = url
        self.setWindowTitle("Update!")
        self.layout = QGridLayout(self)
        label = QLabel("New update available. You download it here : <br/> <a href='{}'>New Release!</a>".format(self.url))
        label.setTextFormat(Qt.RichText)
        label.linkActivated.connect(self.link_update_clicked)
        self.layout.addWidget(label)



    def link_update_clicked(self, link):
        import webbrowser
        webbrowser.open(link)
        self.close()
