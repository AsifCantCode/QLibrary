import sys
import PyQt5
import PyPDF2
import time
from PyPDF2 import PdfReader
import cv2
from PyQt5 import QtGui, QtWidgets , QtCore
from PyQt5.QtGui import QImage, QPixmap ,QStandardItemModel , QStandardItem
from PyQt5.QtCore import Qt, QTimer, QDate
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
        self.ui.SearchButton.clicked.connect(self.SearchOrder)
        self.ui.orderData.clicked.connect(self.on_orderData_clicked)

        #construction script for the search order part

        self.ui.SearchDate.setCalendarPopup(True)  # Enables the calendar popup
        self.ui.SearchDate.setDate(QDate.currentDate())
        self.ui.ReturnBtn.clicked.connect(self.ReturnOrder)

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

        self.ui.genreComboBox.clear()
        self.genres = librarianApi.get_genres(entered_username,entered_password)
        self.ui.genreComboBox.addItems(self.genres)

        self.ui.genreComboBox.currentIndexChanged.connect(self.on_genreComboBoxClicked)
        self.ui.authorComboBox.currentIndexChanged.connect(self.on_authorComboBoxClicked)
        self.ui.foundBooks.clicked.connect(self.on_foundBooksClicked)


        self.ui.stackedWidget.setCurrentIndex(0)

    def on_home_btn_2_toggled(self):

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


        portListModel=QStandardItemModel()
        self.ui.portListView.setModel(portListModel)


        available_ports = list(serial.tools.list_ports.comports())
        self.ports = available_ports
        if len(available_ports) > 0:
            print("Available serial ports:")
            for port in available_ports:
                print(port.device)
                portListModel.appendRow(QStandardItem(str(port.device)))
    def on_dashborad_btn_2_toggled(self):

        self.ui.stackedWidget.setCurrentIndex(1)

    def on_orders_btn_1_toggled(self):

        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.bookbtn.clicked.connect(self.uploadBooks)
        self.ui.authbtn.clicked.connect(self.uploadAuthors)
        self.ui.pdf_btn.clicked.connect(self.uploadPDFs)

    def on_orders_btn_2_toggled(self):

        self.ui.stackedWidget.setCurrentIndex(2)

    def on_products_btn_1_toggled(self):

        self.ui.stackedWidget.setCurrentIndex(3)

    def on_products_btn_2_toggled(self):

        self.ui.stackedWidget.setCurrentIndex(3)

    def on_memberRegSection_btn_1_toggled(self):

        print('reg Section')
        self.ui.stackedWidget.setCurrentIndex(4)
        self.regMemberBtn.clicked.connect(self.registerMember)


    def on_memberRegSection_btn_2_toggled(self):

        self.ui.stackedWidget.setCurrentIndex(4)

    def on_ebook_button_s(self):
        self.ui.stackedWidget.setCurrentIndex(5)


    #booklist functions


    def on_authorComboBoxClicked(self , index):
        self.current_author_index=index

        foundBookModel=QStandardItemModel()
        self.ui.foundBooks.setModel(foundBookModel)
        self.foundBooksList = librarianApi.get_books(self.genres[self.current_genre_indx],self.authorIds[index],entered_username,entered_password)

        for stuff in self.foundBooksList:
            foundBookModel.appendRow(QStandardItem(stuff['title']))


        return

    def on_genreComboBoxClicked(self,index):
        print(index)
        self.current_genre_indx=index

        self.authors=librarianApi.get_authors(self.genres[index],entered_username,entered_password)
        authorNames =[]
        self.authorIds=[]
        for author in self.authors:
            authorNames.append(author['name'])
            self.authorIds.append(author['id'])
        self.ui.authorComboBox.clear()
        self.ui.authorComboBox.addItems(authorNames)
        return

    def on_foundBooksClicked(self,index):

        self.ui.AvailableCopiesValue.setText(str(self.foundBooksList[index.row()]['availablecopies']))
        self.ui.ISBNValue.setText(str(self.foundBooksList[index.row()]['isbn']))
        self.ui.TitleValue.setText(str(self.foundBooksList[index.row()]['title']))
        self.ui.TotalCopiesValue.setText(str(self.foundBooksList[index.row()]['totalcopies']))

        return
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
                            librarianApi.insert_book(lines[0], lines[1], lines[2], lines[3], lines[4], lines[5], lines[6], lines[7], lines[8], lines[9],
                                                    lines[10] , lines[11],entered_username, entered_password)
                            qr.createQR(lines[0] ,lines[1] )

    def uploadPDFs(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        # Show the file dialog and get the selected file paths
        file_paths, _ = QFileDialog.getOpenFileNames(self, "Open Files", "", "PDF Files (*.pdf);;All Files (*)",
                                                     options=options)

        if file_paths:
            print(f'Selected Files: {file_paths}')
            for file_path in file_paths:
                # Check if the file has a PDF extension
                if file_path.lower().endswith('.pdf'):
                    # Perform your desired actions with each selected PDF file
                    with open(file_path, mode='rb') as file:
                        pdf_reader = PdfReader(file)

                        # Read the first two lines from each PDF
                        first_two_lines = ""
                        for page_num in range(min(len(pdf_reader.pages), 2)):
                            page = pdf_reader.pages[page_num]
                            first_two_lines += page.extract_text()

                        # Your logic with the first two lines of the PDF
                        print(f'First two lines of {file_path}: {first_two_lines}')
                else:
                    print(f'Error: {file_path} is not a PDF file and will be skipped.')

        else:
            print('No files selected.')

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
        self.ports=available_ports
        if len(available_ports) > 0:
            print("Available serial ports:")
            for port in available_ports:
                print(port.device)

        if self.ser is None and len(available_ports) == 2:
            self.ser = serial.Serial(available_ports[1].device, 115200, timeout=1)
            self.ui.serportclose.setText('Port Open !')
            self.timer2.start(200)
        elif self.ser is not None:
            if self.ser.is_open:
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
           self.camera = cv2.VideoCapture(2)
           self.timer.start(50)
           self.scannedlabel.setVisible(True)
        else:
           self.camera.release()
           self.timer.stop()
           self.camera = None
           self.scannedlabel.setVisible(False)

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


    #member register function
    def registerMember(self):
        name = self.regName_2.text()
        studentId = self.regID.text()
        email = self.regEmail_2.text()
        phoneNo = self.regPhone.text()
        memUsername = self.regUsername.text()
        librarianApi.insert_member(name, studentId, email, phoneNo, memUsername, entered_username, entered_password)
        QtWidgets.QMessageBox.information(self, "Member Registration", "Member registered successfully.")

    #functions for the order deets

    def on_orderData_clicked(self,index):
        print("something clicked")
        details=self.orderDetails[index.row()]

        orderid=str(details['id'])
        bookid=str(details['bookId'])
        bookinfo=librarianApi.book_info(bookid,entered_username,entered_password)
        bookname=bookinfo['title']

        self.ui.OrderIdValue.setText(orderid)
        self.ui.BookNameVal.setText(bookname)

        fine=librarianApi.fineDeets(orderid,entered_username,entered_password)

        self.ui.FineDueValue.setText(fine)
        self.returnID=orderid;

    def SearchOrder(self):

        self.ui.OrderIdValue.setText("")
        self.ui.FineDueValue.setText("N/A")
        self.ui.BookNameVal.setText("N/A")

        self.orderDataModel = QStandardItemModel()
        self.ui.orderData.setModel(self.orderDataModel)
        id=self.ui.SearchId.text()

        if (id==""):
            return "ajara"

        orders=librarianApi.bookBorrowDeets(id ,entered_username , entered_password)
        self.orderDetails=orders

        for order in orders:
            item=QStandardItem(f"Order ID: {order['id']}UserId: {order['userId']}")
            self.orderDataModel.appendRow(item)

    def ReturnOrder(self):
        librarianApi.bookreturn(self.returnID,entered_username,entered_password)






class MyMainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MyMainWindow , self ).__init__()

        # Load the UI from the .ui file dynamically
        self.ui=loadUi('login.ui', self)
        self.ui.pushButton.clicked.connect(self.login)
        self.invalid_credentials_label = self.ui.invalidLabel
        self.invalid_credentials_label.setVisible(False)
        self.invalid_credentials_label.setAlignment(QtCore.Qt.AlignCenter)



    def login(self):
        # Get the entered username and password
        global entered_username
        entered_username = self.ui.lineEdit.text()
        global entered_password
        entered_password = self.ui.lineEdit_2.text()
        state=login_api.loginController.librarian_login(entered_username, entered_password)
        if state:
            self.close()
            window = MainWindow()
            window.show()
        else:
            # Invalid credentials, show an error message
            self.invalid_credentials_label.setText("Invalid Credentials")
            self.invalid_credentials_label.setVisible(True)  # Show the label

    def keyPressEvent(self,event):
        if event.key()==Qt.Key_Escape:
            self.close()







