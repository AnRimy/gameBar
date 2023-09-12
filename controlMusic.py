import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QWidget, QPushButton, QDesktopWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *

from createSubWindow import CreateWin

class ControlMusic(CreateWin):                             
    def __init__(self, parent=None, *args):                       
        self.root = CreateWin(parent, *args)
        self.widgets()


    def widgets(self):
        self.main_frame = QPushButton(self.root, text='121')
        self.main_frame.setGeometry(0, 0, 200, 215)
        self.main_frame.setStyleSheet('background-color:red')
        self.root.show()
