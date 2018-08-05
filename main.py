# -*- coding: utf-8 -*-
import sys
import random
from PyQt5 import QtWidgets, QtCore
from PyQt5.Qt import QCheckBox, QLineEdit, QSpinBox

def on_clicked():
    try:
        spi = spin.value()
        tekst.clear()
        tex = ""
        if checks.isChecked():
            tex += "abcdefghijklmnopqrstuvwxyz"
        if checkc.isChecked():
            tex += "0123456789"
        if checkp.isChecked():
            tex += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        passw = []
        for i in range(spi):
            passw.append(random.choice(tex))
        tekst.setText("".join(passw))
    except:
        pass    
def on_buff():
    clipboard = QtWidgets.QApplication.clipboard()
    clipboard.setText(tekst.text())
            
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()  # Создаем окно
window.setWindowTitle("Простой генератор паролей")  # Указываем заголовок

# Параметр окна запрещает изменять размеры
window.setWindowFlags(QtCore.Qt.Widget | QtCore.Qt.MSWindowsFixedSizeDialogHint)

# Флажок Строчные буквы
checks = QCheckBox('Строчные буквы', window)
checks.move(20, 20)

# Флажок Прописные буквы
checkp = QCheckBox('Прописные буквы', window)
checkp.move(220, 20)

# Флажок цифры
checkc = QCheckBox('Цифры', window)
checkc.move(20, 60)

# Поле для ввода целых чисел
label = QtWidgets.QLabel('Количество символов', window)
label.move(80, 102)
spin = QSpinBox(window)
spin.move(30, 100)
spin.setValue(6)

# Однострочное текстовое поле
tekst = QLineEdit(window)
tekst.resize(150, 25)
tekst.move(20, 160)

# Кнопка буфер обмена
buttonb = QtWidgets.QPushButton("В буфер", window)
buttonb.resize(80, 30)
buttonb.move(20, 210)
buttonb.clicked.connect(on_buff)

# Кнопка выход
buttone = QtWidgets.QPushButton("Выход", window)
buttone.resize(80, 30)
buttone.move(240, 210)
buttone.clicked.connect(app.quit)  # Выход из программы

# Старт
buttons = QtWidgets.QPushButton("Старт", window)
buttons.resize(80, 30)
buttons.move(240, 160)
buttons.clicked.connect(on_clicked)

window.resize(360, 260)  # Минимальные размеры
window.show()  # Отображаем окно
sys.exit(app.exec_())