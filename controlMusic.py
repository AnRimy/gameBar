import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
import keyboard

from createSubWindow import CreateWin

class ControlMusic:                             
    def __init__(self, args, parent): 
        # self.x, self.y, self.w, self.h = args   
        self.root = CreateWin(parent, args)
        self.widgets()
        self.root.show()

    def widgets(self):
        self.mainFrame = QFrame(self.root)
        self.mainFrame.setGeometry(0, 0, 300, 200)
        self.mainFrame.setStyleSheet('background-color:rgb(40, 36, 36); border-radius: 0px')

        self.backSoundButton = QPushButton(self.mainFrame)
        self.backSoundButton.setGeometry(10, 75, 50, 50)
        self.backSoundButton.setStyleSheet('background-color:blue; border-radius: 25px')

        self.nextSoundButton = QPushButton(self.mainFrame)
        self.nextSoundButton.setGeometry(240, 75, 50, 50)
        self.nextSoundButton.setStyleSheet('background-color:blue; border-radius: 25px')

        self.stopStartButton = QPushButton(self.mainFrame)
        self.stopStartButton.setGeometry(125, 75, 50, 50)
        self.stopStartButton.setStyleSheet('background-color:blue; border-radius: 25px')
        
        self.backSoundButton.clicked.connect(lambda:self.changeSound('back'))
        self.nextSoundButton.clicked.connect(lambda:self.changeSound('next'))
        self.stopStartButton.clicked.connect(lambda:self.changeSound('stop/start'))

    def changeSound(self, action):
        if action == 'back':
            keyboard.send('back track')
        if action == 'next':
            keyboard.send('next track')
        if action == 'stop/start':
            keyboard.send('play-pause')


    def close(self):
        self.root.close()
    
