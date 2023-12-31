import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QWidget, QPushButton, QDesktopWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *

from controlMusic import ControlMusic


class MainWindow(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.screen = QDesktopWidget().availableGeometry()
        self.widthBar = 0
        self.step = 55

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True )   
        self.setAttribute(Qt.WA_NoSystemBackground, False)      
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet('background-color:rgba(0, 0, 0, 70)')
        self.resize(self.screen.width(), 1080)
        
        self.moduls = {'controlMusic':{'open': False}}

    def topBar(self):
        self.bar_label = QPushButton(self)
        self.bar_label.setStyleSheet('background-color:white; border-radius:10px')
        self.bar_label.setGeometry(self.screen.width()//2, 10, 54, 54)
        self.widget_vk()

    def widget_vk(self):
        self.controlMusic_label = QPushButton(self.bar_label)
        self.controlMusic_label.setStyleSheet('background-color: rgb(255, 255, 255); border-radius:25px')
        self.controlMusic_label.setGeometry(2, 2, 50, 50)
        self.controlMusic_label.setIcon(QIcon('icon/music.png'))
        self.controlMusic_label.setIconSize(QSize(50, 50))
        self.controlMusic_label.clicked.connect(lambda:self.onClicked('controlMusic', 
                                                                       [840, 100, 300, 200])) 
    
    def onClicked(self, widget, geometry):
        if widget == 'controlMusic':
            if self.moduls['controlMusic']['open'] == False:
                self.moduls['controlMusic']['open'] = True
                self.app = ControlMusic(self, geometry)
            else:
                self.moduls['controlMusic']['open'] = False
                self.app.close()
        

    def test_f(self):
        def m():
            if not self.widthBar <= 0:
                self.widthBar-=self.step
                self.bar_label.setGeometry(self.screen.width()//2 - self.widthBar//2, 10, self.step+self.widthBar, 55)
        def p():
            self.widthBar+=self.step
            self.bar_label.setGeometry(self.screen.width()//2 - self.widthBar//2, 10, self.step+self.widthBar, 55)
        minus_button = QPushButton('-', self)
        minus_button.setGeometry(500, 500, 50, 50)
        minus_button.setStyleSheet('background-color:white')
        plus_button = QPushButton('+', self)
        plus_button.setGeometry(550, 500, 50, 50)
        plus_button.setStyleSheet('background-color:white')

        minus_button.clicked.connect(m)
        plus_button.clicked.connect(p)

    def run(self):
        self.test_f()
        self.topBar()
        window.show()




app = QApplication(sys.argv)
window = MainWindow()
window.run()
app.exec()