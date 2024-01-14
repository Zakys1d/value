from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,
                             QPushButton, QListWidget, QVBoxLayout,QLineEdit,QComboBox)
from PyQt5.QtCore import Qt
from random import randint

app = QApplication([])
window = QWidget()
window.resize(250,250) # розміри
window.move(250,250)

line = QLineEdit()

line1 = QLabel(' ')


v = QVBoxLayout()

text1 = QLabel("Сума:")
text2 = QLabel("У валюту:")
text3 = QLabel("Результат:")
button = QPushButton('Конвертувати')

combo = QComboBox()
list1 = ['eur','usd','dirham']
combo.addItems(list1)


result = []
def add_task():
    t = line.text()
    c = combo.currentText()
    if c == 'eur':
        result = int(t) * 40
        line1.setText(str(result))
    elif c == 'usd':
        result = int(t) * 37
        line1.setText(str(result))
    elif c == 'dirham':
        result = int(t) * 10
        line1.setText(str(result))    
        
button.clicked.connect(add_task)

v.addWidget(text1)
v.addWidget(line)
v.addWidget(text2)
v.addWidget(combo)
v.addWidget(text3)
v.addWidget(line1)
v.addWidget(button)

window.setLayout(v)
window.show()
app.exec_()

