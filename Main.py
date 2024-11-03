import os
from PIL import Image, ImageFilter, ImageEnhance
import folder

from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import *


def pil2pixmap(im):
    if im.mode == "RGB":
        r, g, b = im.split()
        im = Image.merge("RGB", (b, g, r))
    elif im.mode == "RGBA":
        r, g, b, a = im.split()
        im = Image.merge("RGBA", (b, g, r, a))
    elif im.mode == "L":
        im = im.convert("RGBA")
    im2 = im.convert("RGBA")
    data = im2.tobytes("raw", "RGBA")
    qim = QImage(data, im.size[0], im.size[1], QImage.Format_ARGB32)
    pixmap = QPixmap.fromImage(qim)
    return pixmap


class PhotoManager:
    def __init__(self):
        self.WhiteBlack = None
        self.photo = None
        self.folder = None
        self.filename = None
        self.image_lbl = None

    def Downloader_photo(self):
        image_path = os.path.join(self.folder, self.filename)
        self.photo = Image.open(image_path)

    def show_photo(self, image_lbl):
        pixels = pil2pixmap(self.photo)
        pixels = pixels.scaledToWidth(500)
        image_lbl.setPixmap(pixels)

    def Black_White(self, ):
        self.photo = self.photo.convert("L")
        self.show_photo(self.image_lbl)

    def Left_side(self, ):
        self.photo = self.photo.transpose(Image.ROTATE_90)
        self.show_photo(self.image_lbl)

    def Right_side(self, ):
        self.photo = self.photo.transpose(Image.ROTATE_270)
        self.show_photo(self.image_lbl)

    def Mirror(self, ):
        self.photo = self.photo.transpose(Image.FLIP_LEFT_RIGHT)
        self.show_photo(self.image_lbl)

    def light(self, ):
        self.photo = ImageEnhance.Brightness(self.photo).enhance(1.5)
        self.show_photo(self.image_lbl)

    def idk(self, ):
        self.photo = ImageEnhance.Contrast(self.photo).enhance(1.5)
        self.show_photo(self.image_lbl)

    def Filter(self, ):
        self.photo = self.photo.filter(ImageFilter.EMBOSS)
        self.show_photo(self.image_lbl)

    def Blur(self, ):
        self.photo = self.photo.filter(ImageFilter.BLUR)
        self.show_photo(self.image_lbl)

    def White_Black(self, ):
        self.photo = self.photo.convert("L")
        edges = self.photo.filter(ImageFilter.FIND_EDGES)
        self.show_photo(self.image_lbl)

    def White(self, ):
        self.photo = self.photo.filter(ImageFilter.CONTOUR)
        self.show_photo(self.image_lbl)

app = QApplication([])
window = QWidget()

app.setStyleSheet("""
        QWidget {
            background: #40534C;
        }
        
        QPushButton
        {
            background: #677D6A;
            border-style: groove;
            border-color: #1A3636;
            border-width: 1px;
            border-radius: 5px;
            min-height: 30px;
            min-width: 100;
            color: #181C14;
            font-size: 15px;

        }
        
        QListWidget
        {
            background: #677D6A;
            border-radius: 5px;
            border-color: #1A3636;
            border-width: 1px;
            border-radius: 7px;
            color: #181C14;
            
        }

    """)

v1 = QVBoxLayout()
v2 = QVBoxLayout()
h3 = QHBoxLayout()
h4 = QHBoxLayout()
main_line = QHBoxLayout()

window.resize(700, 700)

#пепший
left = QPushButton("Вліво")
right = QPushButton("Вправо")
mirror = QPushButton("Дзеркало")
light = QPushButton("Різкість")
idk = QPushButton("Ч/Б")
picture = QLabel("картинка")
#другій
test1 = QPushButton("Контрастність")
test2 = QPushButton("Філтер")
test3 = QPushButton("блюр")
test4 = QPushButton("Б/Ч")
test5 = QPushButton("Накладення контурів")

failbut = QPushButton("Папка")
piclist = QListWidget()

v1.addWidget(failbut)
v1.addWidget(piclist)
main_line.addLayout(v1)
v2.addWidget(picture)
h3.addWidget(left)
h3.addWidget(right)
h3.addWidget(mirror)
h3.addWidget(light)
h3.addWidget(idk)

v2.addLayout(h3)
main_line.addLayout(v2)
v2.addLayout(h4)

h4.addWidget(test1)
h4.addWidget(test2)
h4.addWidget(test3)
h4.addWidget(test4)
h4.addWidget(test5)

photo_manager = PhotoManager()
photo_manager.image_lbl = picture


def open_folder():
    photo_manager.folder = QFileDialog.getExistingDirectory()
    files = os.listdir(photo_manager.folder)
    piclist.clear()
    piclist.addItems(files)


def show_chosen_image():
    photo_manager.filename = piclist.currentItem().text()
    photo_manager.Downloader_photo()
    photo_manager.show_photo(picture)



piclist.currentRowChanged.connect(show_chosen_image)

idk.clicked.connect(photo_manager.Black_White)
left.clicked.connect(photo_manager.Left_side)
right.clicked.connect(photo_manager.Right_side)
mirror.clicked.connect(photo_manager.Mirror)


test1.clicked.connect(photo_manager.idk)
test2.clicked.connect(photo_manager.Filter)
test3.clicked.connect(photo_manager.Blur)
test4.clicked.connect(photo_manager.White_Black)
test5.clicked.connect(photo_manager.White)

failbut.clicked.connect(open_folder)
window.setLayout(main_line)
window.show()
app.exec_()
