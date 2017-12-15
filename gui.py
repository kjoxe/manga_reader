## TODO: Add zip loading support
## TODO: Add KEYBINDS! j/down/space=next k/up=prev q=quit
## TODO: Split picture up and display half on either side of screen
## TODO: Zooming??

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QScrollArea
from PyQt5.QtGui import QIcon, QPixmap, QPalette

import time
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'Manga Reader'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create widgets
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.label = QLabel(self.scrollArea)
        self.label.setScaledContents(True)
 
        self.show()

    def updateUI(self, image):
        pixmap = QPixmap(image)
        self.label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
        self.scrollArea.resize(self.size())
        self.label.resize(self.size())

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Q:
            self.close()

        elif e.key() == Qt.Key_J or e.key() == Qt.Key_Space:
            self.updateUI(Loader.getNextImage())
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.updateUI('vohiyo.jpg')
    sys.exit(app.exec_())
