# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import PyQt5
from PyQt5 import QtGui, QtWidgets , QtCore 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow 
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream

from login import MyMainWindow



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    
    style_file = QFile("style.qss")
    style_file.open(QFile.ReadOnly | QFile.Text)
    style_stream = QTextStream(style_file)
    app.setStyleSheet(style_stream.readAll())   
    window = MyMainWindow()
    window.setWindowFlags(Qt.FramelessWindowHint)
    window.setAttribute(Qt.WA_TranslucentBackground)
    window.show()    
    sys.exit(app.exec_())
