from PyQt5.QtCore import Qt
from random import randint
import json
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
app = QApplication([])
window = QWidget()
window.show()
window.setWindowTitle("ЛОТОРЕЯ")
window.resize(400, 400)
winner = QLabel("Натисни щоб узяти участь")

button = QPushButton("Грати")
with open("loto.json", "r") as file:
    o = json.load(file)
i = QLabel("?")
i2 = QLabel("Результати:")

box = QVBoxLayout()
box.addWidget(winner, alignment=Qt.AlignCenter)
box.addWidget(button, alignment=Qt.AlignCenter)
box.addWidget(i, alignment=Qt.AlignCenter)
box.addWidget(i2, alignment=Qt.AlignCenter)
window.setLayout(box)
def button_start():
    a = randint(0, 10)
    u = randint(0, 10)
    o.append(a)
    o.append(u)
    with open("loto.json", "w") as file:
        json.dump(o, file)
    i.setText(str(a))
    i2.setText(str(o))
    if a == u:
        winner.setText("Ви виграли!")
    else:
        winner.setText("ви програли!")
 
   
button.clicked.connect(button_start)
app.exec_()
