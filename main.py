# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.Qt import QCheckBox, QLineEdit, QSpinBox

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()                           # Создаем окно
window.setWindowTitle("Простой генератор паролей")     # Указываем заголовок

#Параметры окна запрещает изменять размеры
window.setWindowFlags(QtCore.Qt.Widget | QtCore.Qt.MSWindowsFixedSizeDialogHint)

#Флажок Строчные буквы
checkb = QCheckBox('Строчные буквы', window)
checkb.move(20, 20)

#Флажок Прописные буквы
checkb = QCheckBox('Прописные буквы', window)
checkb.move(220, 20)

#Флажок цифры
checkb = QCheckBox('Цифры', window)
checkb.move(20, 60)

#Поле для ввода целых чисел
label = QtWidgets.QLabel('Количество символов', window)
label.move(80, 102)
spin = QSpinBox( window)
spin.move(30, 100)
spin.setValue(6)

#Однострочное текстовое поле
tekst = QLineEdit(window)
tekst.resize(150, 25)
tekst.move(20, 160)

#Кнопка буфер обмена
button = QtWidgets.QPushButton("В буфер", window)
button.resize(80, 30)
button.move(20, 210)

#Кнопка выход
button = QtWidgets.QPushButton("Выход", window)
button.resize(80, 30)
button.move(240, 210)

#Старт
button = QtWidgets.QPushButton("Старт", window)
button.resize(80, 30)
button.move(240, 160)

window.resize(360, 260)                                         # Минимальные размеры
window.show()                                                       # Отображаем окно
sys.exit(app.exec_())