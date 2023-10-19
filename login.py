import sys
import PyQt5
from PyQt5 import QtGui, QtWidgets , QtCore 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow 
from PyQt5.uic import loadUi
from scene2 import Scene2
import login_api



class MyMainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MyMainWindow , self ).__init__()

        # Load the UI from the .ui file dynamically
        self.ui=loadUi('login.ui', self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.pushButton.clicked.connect(self.login)
    def login(self):
        # Get the entered username and password
        entered_username = self.ui.lineEdit.text()
        entered_password = self.ui.lineEdit_2.text()
        window = Scene2()
        window.show()
        login_api.loginController.librarian_login(entered_username, entered_password)

        
    
    def keyPressEvent(self,event):
        if event.key()==Qt.Key_Escape:
            self.close()






