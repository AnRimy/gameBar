import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QWidget, QPushButton, QDesktopWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *


class BlockBar(QWidget):
    def __init__(self, parent, args):
        super().__init__(parent)
        self.root = QLabel(parent)
        self.root.setGeometry(*args)
        self.root.setStyleSheet('background-color:white; border-radius:10px')

        