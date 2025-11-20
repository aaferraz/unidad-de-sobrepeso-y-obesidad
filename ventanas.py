from pygame import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from random import *

app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle('App')
main_win.move(900, 70)
main_win.resize(700, 700)

main_win.show()

app.exec_()