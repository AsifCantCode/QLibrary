import sys
import PyQt5
from PyQt5 import QtGui, QtWidgets , QtCore 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog 
from PyQt5.uic import loadUi
from scene2 import Scene2
import login_api
from sidebar_ui import Ui_MainWindow
import csv
from librarian_api import librarianApi

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui=loadUi('sidebar.ui', self)

        # self.ui.icon_only_widget.hide()
        self.selected_files = []
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
        #self.ui.bookbtn.clicked.connect(self.openFileDialog)
        self.ui.authbtn.clicked.connect(self.openFileDialog)
        #self.ui.submitbtn.clicked.connect(self.submitFiles)
        

    def on_orders_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        #self.ui.bookbtn.clicked.connect(self.openFileDialog)
        self.ui.authbtn.clicked.connect(self.openFileDialog)
        #self.ui.submitbtn.clicked.connect(self.submitFiles)

    def on_products_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_products_btn_2_toggled(self, ):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_customers_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_customers_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        
    def openFileDialog(self):
            options = QFileDialog.Options()
            # Show the file dialog and get the selected file path
            filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files ();;Text Files (.txt)", options=options)
            
            if filePath:
                print(f'Selected File: {filePath}')   
                with open(filePath, mode ='r')as file:

                    # reading the CSV file
                    csvFile = csv.reader(file)
                    # displaying the contents of the CSV file
                    for lines in csvFile:
                            librarianApi.insert_author(lines[0], lines[1], lines[2], entered_username, entered_password)
    # def openFileDialog(self):
    #     options = QFileDialog.Options()
    #     file_paths, _ = QFileDialog.getOpenFileNames(self, "Open File", "", "CSV Files (*.csv);;All Files (*)", options=options)

    #     if file_paths:
    #         for file_path in file_paths:
    #             print(f'Selected File: {file_path}')
    #             # You can store the file paths in a list here
    #             self.selected_files.append(file_path)
                
    
    # def submitFiles(self):
    #     # Handle the submission of selected files
    #     if self.selected_files:
    #         # Send the selected files to the backend for processing
    #         for file_path in self.selected_files:
    #             with open(file_path, mode='r') as file:
    #                 csvFile = csv.reader(file)
    #                 for lines in csvFile:
    #                     print(lines)
    #                 # Process the CSV file, e.g., send data to the backend



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
        global entered_username
        entered_username = self.ui.lineEdit.text()
        global entered_password 
        entered_password = self.ui.lineEdit_2.text()
        state=login_api.loginController.librarian_login(entered_username, entered_password)
        if(state):
            self.close()
            window=MainWindow()
            window.show()



        
    
    def keyPressEvent(self,event):
        if event.key()==Qt.Key_Escape:
            self.close()






