import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QWidget, QPushButton, QDesktopWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *


class BlockBar(QWidget):
    def __init__(self, parent, args, sizeBlockBar):
        super().__init__(parent)
        self.sizeBlockBar = sizeBlockBar
        
        self.root = QLabel(parent)
        self.root.setGeometry(*args)
        self.root.setStyleSheet('background-color:white; border-radius:10px')
        
        self.main_button = QPushButton(self.root)
        self.main_button.setStyleSheet('background-color: rgb(255, 255, 255); border-radius:25px')
        self.main_button.setGeometry(2, 2, self.sizeBlockBar - 4, self.sizeBlockBar - 4)
        self.main_button.setIcon(QIcon('icon/music.png'))
        self.main_button.setIconSize(QSize(self.sizeBlockBar - 4, self.sizeBlockBar - 4))

        