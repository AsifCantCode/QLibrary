import sys
import PyQt5
from PyQt5 import QtGui, QtWidgets , QtCore 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog 
from PyQt5.uic import loadUi
import csv




class Scene2(QtWidgets.QWidget):
    def __init__(self):
        super(Scene2 , self ).__init__()

        # Load the UI from the .ui file dynamically
        self.ui=loadUi('scene2.ui', self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.filepathbtn.clicked.connect(self.openFileDialog)
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
                        print(lines)
        
    def keyPressEvent(self,event):
        if event.key()==Qt.Key_Escape:
            self.close()