# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(637, 537)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 20, 590, 420))
        self.widget.setStyleSheet("QPushButton#pushButton{\n"
"background-color: rgba(85,98,112,255);\n"
"color: rgba(255,255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"padding-left: 5px;\n"
"padding-top:5px;\n"
"background-color: rgba(255,107,107,255);\n"
"background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"background-color:rgba(255,107,107,255);\n"
"}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(300, 50, 260, 330))
        self.label.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-radius:10px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(40, 25, 270, 360))
        self.label_2.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 98, 112, 255), stop:1 rgba(255, 107, 107, 255));\n"
"border-radius:10px;\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(330, 80, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgba(0,0,0,200);\n"
"")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(330, 140, 190, 40))
        self.lineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46, 82, 101, 200);\n"
"color:rgba(0,0,0);\n"
"padding-bottom:7px;")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 190, 190, 40))
        self.lineEdit_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46, 82, 101, 200);\n"
"color:rgba(0,0,0);\n"
"padding-bottom:7px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(370, 280, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(70, 50, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("text-align:center;\n"
"color:rgba(255,255,255,220);\n"
"margin-left:center;\n"
"margin-right:center;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(60, 160, 231, 201))
        self.label_5.setStyleSheet("background-color: transparent;\n"
"border-radius:10px;")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("icon.jpg"))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Log In"))
        self.lineEdit.setPlaceholderText(_translate("Form", "UserName"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "password"))
        self.pushButton.setText(_translate("Form", "Log In"))
        self.label_4.setText(_translate("Form", "QLIBRARY"))


class LoginApp(QtWidgets.QWidget):
    def __init__(self):
        super(LoginApp, self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Connect the login button to the login function
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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_app = LoginApp()
    login_app.show()
    sys.exit(app.exec_())