## TODO: Add KEYBINDS! j/down/space=next k/up=prev q=quit
## TODO: Split picture up and display half on either side of screen
## TODO: Zooming??

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QScrollArea
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QImage

import mangazip

class Image_Viewer(QWidget):
 
    def __init__(self, myzip, imagepaths):
        super().__init__()
        self.title = 'Manga Reader'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480

        self.zip=myzip
        self.imagepaths=imagepaths
        self.current_image_index=0

        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create widgets
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.label = QLabel(self.scrollArea)
        self.label.setScaledContents(True)

        self.updateUI(self.imagepaths[self.current_image_index])

        self.show()

    def updateUI(self, imagepath):
        print(imagepath)
        with self.zip.open(imagepath) as f:
            image=f.read()
            pixmap = QPixmap.fromImage(QImage.fromData(image))
            self.label.setPixmap(pixmap)
            self.resize(pixmap.width(),pixmap.height())
            self.scrollArea.resize(self.size())
            self.label.resize(self.size())

    def nextImage(self):
        if self.current_image_index<len(self.imagepaths)-1:
            self.current_image_index+=1
        self.updateUI(self.imagepaths[self.current_image_index])

    def prevImage(self):
        if self.current_image_index>0:
            self.current_image_index-=1
        self.updateUI(self.imagepaths[self.current_image_index])

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Q:
            self.close()

        elif e.key() == Qt.Key_J or e.key() == Qt.Key_Space:
            self.nextImage()
        elif e.key() == Qt.Key_K:
            self.prevImage()
 
class Manga_Gui():
    def __init__(self, myzip, imagepaths):
        app = QApplication(sys.argv)
        self.viewer = Image_Viewer(myzip, imagepaths)
        sys.exit(app.exec_())
