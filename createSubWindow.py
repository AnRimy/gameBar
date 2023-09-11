import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QWidget, QPushButton, QDesktopWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *

class CreateWin(QMainWindow):                             
    def __init__(self, parent=None):
        super().__init__(parent)                         
        self.resize(200, 200)
        self.screen = QDesktopWidget().availableGeometry()
        self.setWindowFlag(Qt.FramelessWindowHint)

