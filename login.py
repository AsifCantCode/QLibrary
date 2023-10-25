import sys
import PyQt5
import cv2
from PyQt5 import QtGui, QtWidgets , QtCore 
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt , QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog ,QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.uic import loadUi
from scene2 import Scene2
import login_api
from sidebar_ui import Ui_MainWindow
import csv
from librarian_api import librarianApi
from pyzbar.pyzbar import decode
import qr




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
        self.camera = cv2.VideoCapture(0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateFrame)
        self.timer.start(50)
        self.ui.qrbtn.clicked.connect(self.scanQRCode)

    def on_dashborad_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_orders_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.bookbtn.clicked.connect(self.uploadBooks)
        self.ui.authbtn.clicked.connect(self.uploadAuthors)
        
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
        
    def uploadBooks(self):
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
                            librarianApi.insert_book(lines[0], lines[1], lines[2], lines[3], lines[4], lines[5], lines[6], lines[7], lines[8], lines[9]
                                                    ,entered_username, entered_password)
                            qr.createQR(lines[0] ,lines[1] )
    def uploadAuthors(self):
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

    def updateFrame(self):
        ret, frame = self.camera.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channel = frame.shape
            bytesPerLine = 3 * width
            qImg = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qImg)
            self.image_label.setPixmap(pixmap)

    def scanQRCode(self):
        ret, frame = self.camera.read()

        if ret:
            codes = decode(frame)
            if codes:
                for code in codes:
                    qr_data = code.data.decode('utf-8')
                    print(f"Scanned QR Code: {qr_data}")
    





class MyMainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MyMainWindow , self ).__init__()

        # Load the UI from the .ui file dynamically
        self.ui=loadUi('login.ui', self)
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






