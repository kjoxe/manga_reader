## TODO: Split picture up and display half on either side of screen
## TODO: Zooming??

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QSizePolicy
from PyQt5.QtGui import QPixmap, QImage, QGuiApplication

import mangazip

class Image_Viewer(QMainWindow):
 
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
        self.label = QLabel(self)
        self.label.setScaledContents(True)
        self.setCentralWidget(self.label)
        self.label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

        self.updateUI(self.imagepaths[self.current_image_index])

        self.show()

    def updateUI(self, imagepath):
        print(imagepath)
        with self.zip.open(imagepath) as f:
            image=f.read()
            pixmap = QPixmap.fromImage(QImage.fromData(image))
            img_height=QGuiApplication.primaryScreen().availableSize().height()
            self.label.setPixmap(pixmap.scaledToHeight(img_height, Qt.SmoothTransformation))
            self.resize(pixmap.width(),img_height)

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
