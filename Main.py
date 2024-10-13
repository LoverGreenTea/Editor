from PyQt5.QtWidgets import *




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
            border=radius: 7px;
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
window.setLayout(main_line)
window.show()
app.exec_()