import os
from PIL import Image
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
        self.photo = None
        self.folder = None
        self.filename = None

    def Downloader_photo(self):
        image_path = os.path.join(self.folder, self.filename)
        self.photo = Image.open(image_path)

    def show_photo(self, image_lbl):
        pixels = pil2pixmap(self.photo)
        pixels = pixels.scaledToWidth(500)
        image_lbl.setPixmap(pixels)



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


window.resize(700,700)

left = QPushButton("Вліво")
right = QPushButton("Вправо")
mirror = QPushButton("Дзеркало")
light = QPushButton("Різкість")
idk = QPushButton("Ч/Б")
picture = QLabel("картинка")

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

photo_manager = PhotoManager()
def open_folder():
    photo_manager.folder = QFileDialog.getExistingDirectory()
    files = os.listdir(photo_manager.folder)
    piclist.clear()
    piclist.addItems(files)

def show_chosen_image():
    photo_manager.filename = piclist.currentItem().text()
    photo_manager.load()
    photo_manager.show_photo(piclist)

piclist.currentRowChanged.connect(show_chosen_image)
failbut.clicked.connect(open_folder)
window.setLayout(main_line)
window.show()
app.exec_()