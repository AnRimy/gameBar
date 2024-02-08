from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QWidget, QPushButton, QDesktopWidget, QHBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *

class CreateWin(QMainWindow):
    def __init__(self, args, parent):
        super().__init__(parent)
        self.setGeometry(*args)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet('border-radius: 100px; background-color: rgb(100, 100, 100)')
        


