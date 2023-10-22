import sys
import PyQt5
from PyQt5 import QtGui, QtWidgets , QtCore 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.uic import loadUi
from scene2 import Scene2
import login_api
from sidebar_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui=loadUi('sidebar.ui', self)

        # self.ui.icon_only_widget.hide()
        self.ui.full_menu_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.home_btn_2.setChecked(True)
    ## Function for searching
    def on_search_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        search_text = self.ui.search_input.text().strip()
        if search_text:
            self.ui.label_9.setText(search_text)

    ## Function for changing page to user page
    def on_user_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(6)

    ## Change QPushButton Checkable status when stackedWidget index changed
    def on_stackedWidget_currentChanged(self, index):
        btn_list = self.ui.icon_only_widget.findChildren(QPushButton) \
                    + self.ui.full_menu_widget.findChildren(QPushButton)
        
        for btn in btn_list:
            if index in [5, 6]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
            else:
                btn.setAutoExclusive(True)
            
    ## functions for changing menu page
    def on_home_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def on_home_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_dashborad_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_dashborad_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_orders_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_orders_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_products_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_products_btn_2_toggled(self, ):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_customers_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_customers_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)


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
        state=login_api.loginController.librarian_login(entered_username, entered_password)
        if(state):
            self.close()
            window=MainWindow()
            window.show()



        
    
    def keyPressEvent(self,event):
        if event.key()==Qt.Key_Escape:
            self.close()






