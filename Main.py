from PyQt5.QtWidgets import *


app = QApplication([])
window = QWidget()


v1 = QVBoxLayout()
v2 = QVBoxLayout()
v3 = QHBoxLayout()
v4 = QHBoxLayout()
main_line = QHBoxLayout()

main_line.addLayout(v1)
v1.addLayout(v3)
v3.addLayout(v2)
v2.addLayout(v4)

window.resize(700,700)

left = QPushButton("Вліво")
right = QPushButton("Вправо")
mirror = QPushButton("Дзеркало")
light = QPushButton("Різкість")
idk = QPushButton("Ч/Б")


failbut = QPushButton("Папка")
text = QListWidget()

v1.addWidget(failbut)
v1.addWidget(text)

v4.addWidget(left)
v4.addWidget(right)
v4.addWidget(mirror)
v4.addWidget(light)
v4.addWidget(idk)

window.setLayout(main_line)
window.show()
app.exec_()