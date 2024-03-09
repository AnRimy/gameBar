import sys
import configparser
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QWidget, QPushButton, QDesktopWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
import keyboard
import threading

from controlMusic import ControlMusic
from createBlockBar import BlockBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.screen = QDesktopWidget().availableGeometry()
        self.step = 0
        self.barBlocks = []
        self.sizeBlockBar = 55

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True )   
        self.setAttribute(Qt.WA_NoSystemBackground, False)      
        self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setWindowFlags(self.windowFlags() | Qt.Tool)
        self.setStyleSheet('background-color:rgba(0, 0, 0, 70)')
        self.resize(self.screen.width(), self.screen.height())
        
        self.moduls = {'controlMusic':{'open': False}}


    def threading(self):
        th_hide = threading.Thread(self.kea())
        th_hide1 = threading.Thread(window.show())
        th_hide.start()
        th_hide1.start()

        

    def kea(self):
        if self.show:
            keyboard.add_hotkey('Ctrl + d', lambda: self.hide())
        if self.hide:
            keyboard.add_hotkey('Ctrl + d', lambda: self.show())
        keyboard.add_hotkey('Ctrl + 3', lambda: self.close())


    def widget_music(self, block):        
        block.main_button.clicked.connect(lambda:self.onClicked('controlMusic', block,
                                                    [block.root.x() - 150 + self.sizeBlockBar//2, self.sizeBlockBar + 50, 300, 200]))
        

    def onClicked(self, widget, block, geometry):
        if widget == 'controlMusic':
            if self.moduls['controlMusic']['open'] == False:
                self.moduls['controlMusic']['open'] = True
                self.app = ControlMusic(block, geometry)
            else:
                self.moduls['controlMusic']['open'] = False
                self.app.close()
        

    def test_Button(self):
        def minusBlock():
            if len(self.barBlocks) > 0:
                last_block = self.barBlocks.pop()
                last_block.close()
                self.step -= self.sizeBlockBar
                center_x = self.screen.width() // 2

                for i, block in enumerate(self.barBlocks):
                    new_x = center_x - self.step // 2 + i * self.sizeBlockBar
                    block.move(new_x, block.y())
                if len(self.barBlocks) > 1:
                    for i in self.barBlocks[1:len(self.barBlocks)-1]:
                        i.setStyleSheet('background-color:white; border-radius:0px')
                    self.barBlocks[0].setStyleSheet("background-color:white;"
                                                    "border-top-left-radius:10px;"
                                                    "border-top-right-radius:0px;"
                                                    "border-bottom-left-radius:10px;"
                                                    "border-bottom-right-radius:0px")
                    self.barBlocks[-1].setStyleSheet("background-color:white;"
                                                    "border-top-left-radius:0px;"
                                                    "border-top-right-radius:10px;"
                                                    "border-bottom-left-radius:0px;"
                                                    "border-bottom-right-radius:10px")
                elif len(self.barBlocks) == 1:
                    self.barBlocks[0].setStyleSheet('background-color:white; border-radius:10px')
                    
                        
        def plusBlock():
            block = BlockBar(self, (self.screen.width()//2 - 27, 10, self.sizeBlockBar, self.sizeBlockBar), self.sizeBlockBar)          
            self.widget_music(block)
            block.root.show()
            self.barBlocks.append(block.root)
            self.step += self.sizeBlockBar
            
            center_x = self.screen.width() // 2
            for i, block in enumerate(self.barBlocks):
                new_x = center_x - self.step // 2 + i * self.sizeBlockBar
                block.move(new_x, block.y())
                if len(self.barBlocks) != 1:
                    for i in self.barBlocks[1:len(self.barBlocks)-1]:
                        i.setStyleSheet('background-color:white; border-radius:0px')
                    self.barBlocks[0].setStyleSheet("background-color:white;"               
                                                    "border-top-left-radius:10px;"
                                                    "border-top-right-radius:0px;"
                                                    "border-bottom-left-radius:10px;"
                                                    "border-bottom-right-radius:0px")
                    self.barBlocks[-1].setStyleSheet("background-color:white;"               
                                                    "border-top-left-radius:0px;"
                                                    "border-top-right-radius:10px;"
                                                    "border-bottom-left-radius:0px;"
                                                    "border-bottom-right-radius:10px")


        minus_button = QPushButton('-', self)
        minus_button.setGeometry(500, 500, 50, 50)
        minus_button.setStyleSheet('background-color:white')
        plus_button = QPushButton('+', self)
        plus_button.setGeometry(550, 500, 50, 50)
        plus_button.setStyleSheet('background-color:white')

        minus_button.clicked.connect(minusBlock)
        plus_button.clicked.connect(plusBlock)


    def run(self):
        self.test_Button()
        self.threading()
        window.show()
        



if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read("config.ini")
    app = QApplication(sys.argv)
    window = MainWindow()
    window.run()
    app.exec()
    print()
    