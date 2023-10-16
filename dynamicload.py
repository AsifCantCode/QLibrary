import sys
import PyQt5
from PyQt5 import QtGui, QtWidgets , QtCore 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow 
from PyQt5.uic import loadUi

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

        # Replace these values with your actual valid username and password
        valid_username = "Asif"
        valid_password = "1234"

        # Check if entered credentials match the valid ones
        if entered_username == valid_username and entered_password == valid_password:
            QtWidgets.QMessageBox.information(self, 'Login Successful', 'Welcome, {}'.format(entered_username))
        else:
            QtWidgets.QMessageBox.warning(self, 'Login Failed', 'Invalid username or password')
        
        
    
    def keyPressEvent(self,event):
        if event.key()==Qt.Key_Escape:
            self.close()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
