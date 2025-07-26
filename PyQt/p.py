from PyQt5.QtCore import Qt
from random import randint
import json
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
app = QApplication([]) # CREATE APP
window = QWidget() # CREATE WINDOW
window.show() # show window
window.setWindowTitle("MyWindow")
window.resize(900,400)
winner = QLabel("Дызнатися переможця") # НАДПИСЬ
button = QPushButton("Generate")

with open ("generate.json", "r") as file:
    o = json.load(file)


i = QLabel("?")

box = QVBoxLayout() # СТВОРЕННЯ ВЕРТИКАЛЬНОХ ЛЫНЫЙЙ

box.addWidget(winner, alignment=Qt.AlignCenter) # ДОДАВАННЯ ДО ЛЫНЫЫ ВЫДЖЕТА
box.addWidget(button,alignment= Qt.AlignCenter)
box.addWidget(i, alignment= Qt.AlignCenter)
window.setLayout(box)

def button_start():
    a = randint(0, 10)
    o.append(a)

    with open ("generate.json", "w") as file:
        o = json.dump(o,file)
    i.setText(str(a))

button.clicked.connect

app.exec_()
