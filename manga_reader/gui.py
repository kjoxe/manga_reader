## TODO: Zooming??

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QSizePolicy
from PyQt5.QtGui import QPixmap, QImage, QGuiApplication

import manga_reader.mangazip as mangazip

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
        self.jump_distance=""

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

    def nextImage(self, distance):
        self.current_image_index+=distance
        if self.current_image_index>len(self.imagepaths)-1:
            self.current_image_index=len(self.imagepaths)-1
        self.updateUI(self.imagepaths[self.current_image_index])

    def prevImage(self, distance):
        self.current_image_index-=distance
        if self.current_image_index<0:
            self.current_image_index=0
        self.updateUI(self.imagepaths[self.current_image_index])

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Q:
            self.close()

        elif e.key() == Qt.Key_J or e.key() == Qt.Key_Space:
            if self.jump_distance=="":
                self.jump_distance=1
            self.nextImage(int(self.jump_distance))
            self.jump_distance=""
        elif e.key() == Qt.Key_K:
            if self.jump_distance=="":
                self.jump_distance=1
            self.prevImage(int(self.jump_distance))
            self.jump_distance=""
        for key in (
                Qt.Key_0,
                Qt.Key_1,
                Qt.Key_2,
                Qt.Key_3,
                Qt.Key_4,
                Qt.Key_5,
                Qt.Key_6,
                Qt.Key_7,
                Qt.Key_8,
                Qt.Key_9
                ):
            if e.key() == key:
                self.jump_distance=self.jump_distance+str(key-48)
 
class Manga_Gui():
    def __init__(self, myzip, imagepaths):
        app = QApplication(sys.argv)
        self.viewer = Image_Viewer(myzip, imagepaths)
        sys.exit(app.exec_())
