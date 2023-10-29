import sys
import PyQt5
import time
import cv2
from PyQt5 import QtGui, QtWidgets , QtCore 
from PyQt5.QtGui import QImage, QPixmap ,QStandardItemModel , QStandardItem
from PyQt5.QtCore import Qt , QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog ,QWidget, QVBoxLayout, QPushButton, QLabel ,QListView 
from PyQt5.uic import loadUi
from scene2 import Scene2
import login_api
from sidebar_ui import Ui_MainWindow
import csv
from librarian_api import librarianApi
from pyzbar.pyzbar import decode
import qr
import serial
from serialreader import read_number_from_serial
import threading




class CameraInitializer(threading.Thread):
    def __init__(self, camera_index):
        threading.Thread.__init__(self)
        self.camera_index = camera_index
        self.camera = None

    def run(self):
        print("Initializing camera...")
        self.camera = cv2.VideoCapture(self.camera_index)
        if not self.camera.isOpened():
            print("Failed to initialize camera!")
        else:
            print("Camera initialized successfully.")

    def get_camera(self):
        return self.camera




class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.camera = None
        self.timer = None
        
        #variables for the book borrow section
        self.booklistmodel = QStandardItemModel()
        self.items_set = set()
        self.bookitem_names = []

        #Variables for the homepage

        #variables for the author and book csv upload section

        #constructor execution
        self.ui=loadUi('sidebar.ui', self)

        # self.ui.icon_only_widget.hide()
        self.selected_files = []
        self.ui.full_menu_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.home_btn_2.setChecked(True)


        #construction script for the borrow part
        
        #construction script for the other parts

    def closeCamera(self):
        if self.camera is not None:
            self.timer.stop()
            self.camera.release()
            self.camera = None

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
        self.closeCamera()
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def on_home_btn_2_toggled(self):
        self.closeCamera()
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_dashborad_btn_1_toggled(self):
        self.closeCamera()
        self.ui.stackedWidget.setCurrentIndex(1)
        loading_label = self.ui.loadingLabel
        loading_label.show()
        self.camera = cv2.VideoCapture(0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateFrame)
        self.timer.start(50)
        
        self.ser = None
        print('borrow menu')
        self.timer2 = QTimer(self)
        self.timer2.timeout.connect(self.getMemberID)
        


        self.ui.booklist.setModel(self.booklistmodel)
        self.ui.serportclose.clicked.connect(self.closeCardReader)
        self.ui.initborrow.clicked.connect(self.registerBorrow)
        self.refreshBookList()
        self.timer.timeout.connect(lambda: loading_label.hide())

    def on_dashborad_btn_2_toggled(self):
        self.closeCamera()
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_orders_btn_1_toggled(self):
        self.closeCamera()
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.bookbtn.clicked.connect(self.uploadBooks)
        self.ui.authbtn.clicked.connect(self.uploadAuthors)
        
    def on_orders_btn_2_toggled(self):
        self.closeCamera()
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_products_btn_1_toggled(self):
        self.closeCamera()
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_products_btn_2_toggled(self, ):
        self.closeCamera()
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_customers_btn_1_toggled(self):
        self.closeCamera()
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_customers_btn_2_toggled(self):
        self.closeCamera()
        self.ui.stackedWidget.setCurrentIndex(4)
        
            
    #author and book upload functions
    
    
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


    #qr scanning and book borrow functions
    
    
    def updateFrame(self):
        ret, frame = self.camera.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channel = frame.shape
            bytesPerLine = 3 * width
            qImg = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qImg)
            self.image_label.setPixmap(pixmap)
            self.scannedlabel.setText('Scanning...')
            self.scanQRCode(ret , frame)
    def scanQRCode(self , ret , frame):
        # ret, frame = self.camera.read()

        if ret:
            codes = decode(frame)
            if codes:
                for code in codes:
                    qr_data = code.data.decode('utf-8')
                    print(f"Scanned QR Code: {qr_data}")
                    self.items_set.add(qr_data)
                self.scannedlabel.setText('Scanned')
                self.refreshBookList()
                
                # time.sleep(2)
    def closeCardReader(self):
        
        if self.ser == None : 
            self.ser = serial.Serial('COM3', 115200, timeout=1)
            self.ui.serportclose.setText('Port Open !')
            self.timer2.start(200)
        elif self.ser.is_open:
            self.timer2.stop()
            self.ser.close()
            self.ui.serportclose.setText('Port Closed !')
            time.sleep(2)
            self.ser=None
        
    def registerBorrow(self):
        print('book and member data sent to backend:\n')
        print(self.items_set)
        print(" borrowed by ")
        print(self.memberid)


    def getMemberID(self):
        readdata=read_number_from_serial( self.ser) 
        if readdata > 0 :
            self.memberid=readdata
            self.borrowerlabel.setText('Borrowed By: ' + str(self.memberid))            
                    
        

    def refreshBookList(self):
        items = list(self.items_set)
        self.booklistmodel.clear()
        for book in  items :
            boiInfo=librarianApi.book_info(book , entered_username , entered_password)
            self.booklistmodel.appendRow(QStandardItem(boiInfo['title']+'-'+boiInfo['publishedon']))

        





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
    






