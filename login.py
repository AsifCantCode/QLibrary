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
import serial.tools.list_ports


class ProfilePictureUpdater(QWidget):
    def __init__(self):
        super().__init__()

    def update_profile_picture(self, image_path: str) -> None:
        new_pixmap = QPixmap(image_path)

        if new_pixmap.isNull():
            print(f"Error loading image: {image_path}")
            return

        self.profile_picture_label.setPixmap(new_pixmap)
        self.profile_picture_label.setScaledContents(True)

    def choose_profile_picture(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_dialog = QFileDialog()
        file_dialog.setOptions(options)
        file_dialog.setNameFilter("Images (*.png *.jpg *.bmp)")
        file_dialog.setWindowTitle("Select Profile Picture")

        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                selected_file = selected_files[0]
                # self.update_profile_picture(selected_file)
                return selected_file

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
        self.profile_picture_updater = ProfilePictureUpdater()

        #variables for the author and book csv upload section

        #constructor execution
        self.ui=loadUi('sidebar.ui', self)

        # self.ui.icon_only_widget.hide()
        self.selected_files = []
        self.ui.full_menu_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.home_btn_2.setChecked(True)
        self.ui.profile_picture_label = self.ui.findChild(QLabel, 'profile_picture_label')
        self.ui.changeDpButton = self.ui.findChild(QPushButton, 'changeDp')
        self.ui.changeDpButton.clicked.connect(self.update_profile_picture)

        #construction script for the borrow part

        #construction script for the other parts

    def update_profile_picture(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_dialog = QFileDialog()
        file_dialog.setOptions(options)
        file_dialog.setNameFilter("Images (*.png *.jpg *.bmp)")
        file_dialog.setWindowTitle("Select Profile Picture")

        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                selected_file = selected_files[0]
                self.load_profile_picture(selected_file)

    def load_profile_picture(self, image_path: str):
        new_pixmap = QPixmap(image_path)

        if new_pixmap.isNull():
            print(f"Error loading image: {image_path}")
            return

        # Set the new pixmap to the QLabel
        self.ui.profile_picture_label.setPixmap(new_pixmap)

        # Optionally, you can adjust the size to fit the QLabel
        self.ui.profile_picture_label.setScaledContents(True)
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
        file = self.ui.changeDp.clicked.connect(self.profile_picture_updater.choose_profile_picture)

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


        self.ui.stackedWidget.setCurrentIndex(1)
        loading_label = self.ui.loadingLabel
        loading_label.show()

        self.ui.camerabutton.clicked.connect(self.openCamera)


        print('borrow menu')
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateFrame)


        self.ser = None

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

    def on_products_btn_2_toggled(self):
        self.closeCamera()
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_memberRegSection_btn_1_toggled(self):
        self.closeCamera()
        print('reg Section')
        self.ui.stackedWidget.setCurrentIndex(4)
        self.regMemberBtn.clicked.connect(self.registerMember)


    def on_on_memberRegSection_btn_2_toggled(self):
        self.closeCamera()
        self.ui.stackedWidget.setCurrentIndex(4)



    #author and book upload functions


    def uploadBooks(self):
            options = QFileDialog.Options()
            # Show the file dialog and get the selected file path
            filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files ();;Text Files (.txt)", options=options)

            if filePath:
                print(f'Selected File: {filePath}')
                with open(filePath, mode='r')as file:

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

        available_ports = list(serial.tools.list_ports.comports())

        if len(available_ports) > 0:
            print("Available serial ports:")
            for port in available_ports:
                print(port.device)

        if self.ser is None and len(available_ports) == 2:
            self.ser = serial.Serial(available_ports[1].device, 115200, timeout=1)
            self.ui.serportclose.setText('Port Open !')
            self.timer2.start(200)
        elif self.ser.is_open:
            print('closing')
            print(self.ser)
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



        librarianApi.bookborrow(self.memberid, self.items_set, entered_username, entered_password)

    def openCamera(self):
        if self.camera is None:
           self.camera = cv2.VideoCapture(0)
           self.timer.start(50)
        else:
           self.camera.release()
           self.timer.stop()
           self.camera = None

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


    def registerMember(self):
        name = self.regName_2.text()
        studentId = self.regID.text()
        email = self.regEmail_2.text()
        phoneNo = self.regPhone.text()
        memUsername = self.regUsername.text()
        librarianApi.insert_member(name, studentId, email, phoneNo, memUsername, entered_username, entered_password)
        QtWidgets.QMessageBox.information(self, "Member Registration", "Member registered successfully.")




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







