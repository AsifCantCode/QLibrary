import sys
import PyQt5
from PyQt5 import QtGui, QtWidgets , QtCore 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow 
from PyQt5.uic import loadUi

class Scene2(QtWidgets.QWidget):
    def __init__(self):
        super(Scene2 , self ).__init__()

        # Load the UI from the .ui file dynamically
        self.ui=loadUi('scene2.ui', self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

       
    
        
        
    
    def keyPressEvent(self,event):
        if event.key()==Qt.Key_Escape:
            self.close()