import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *

from createSubWindow import CreateWin

class ControlMusic(CreateWin):                             
    def __init__(self, parent=None, *args): 
        self.geometry = args      
        self.root = CreateWin(parent, *args)
        # self.widgets()
        self.root.show()

    def widgets(self):
        self.main_frame = QFrame(self.root)
        self.main_frame.setGeometry(0, 0, self.geometry[0][2], self.geometry[0][3])
        self.main_frame.setStyleSheet('background-color:red')

    def close(self):
        self.root.close()
    
