import sys
import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt, QTimer
from pyzbar.pyzbar import decode
from PIL import Image, ImageDraw, ImageFont
import qrcode
import os





class QRCodeScannerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.loaded=False
        self.initUI()

    def initUI(self):
        print('initui')
        self.setWindowTitle('QR Code Scanner')
        self.setGeometry(100, 100, 640, 480)

        self.camera = cv2.VideoCapture(0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateFrame)
        self.timer.start(200)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)

        self.button = QPushButton('Scan QR Code', self)
        self.button.clicked.connect(self.scanQRCode)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.button)

        self.setLayout(layout)
        print('initui end')
        self.loaded=True

    def updateFrame(self):
        ret, frame = self.camera.read()
        print('updateframe')
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

    
def createQR(data , text_to_add):
        
        

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        
        qr_image = qr.make_image(fill_color="black", back_color="white")
        
        draw = ImageDraw.Draw(qr_image)
        font = ImageFont.truetype("arial.ttf", 18)  
        x1 , y1, x2 ,y2 =  draw.textbbox((0, 0), text=text_to_add, font=font)
        text_width=x2-x1
        text_height=y2-y1
        text_position = (0, qr_image.height - text_height - 10)
        draw.text(text_position, text_to_add, fill="black", font=font)
        
        folder_path='Qr'
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        qr_image.save(folder_path+"/qrcode"+data+".png")
        
        #qr_image.show()

        return 0



# if __name__== '__main__':
#     app = QApplication(sys.argv)
#     scanner = QRCodeScannerApp()
#     createQR('1234' , 'myqr')
#     scanner.show()

#     sys.exit(app.exec_())

import sys
import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt, QTimer
from pyzbar.pyzbar import decode
from PIL import Image, ImageDraw, ImageFont
import qrcode
import os





class QRCodeScannerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.loaded=False
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QR Code Scanner')
        self.setGeometry(100, 100, 640, 480)

        self.camera = cv2.VideoCapture(0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateFrame)
        self.timer.start(200)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)

        self.button = QPushButton('Scan QR Code', self)
        self.button.clicked.connect(self.scanQRCode)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.button)

        self.setLayout(layout)

        self.loaded=True

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

    
def createQR(data , text_to_add):
        
        

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        
        qr_image = qr.make_image(fill_color="black", back_color="white")
        
        draw = ImageDraw.Draw(qr_image)
        font = ImageFont.truetype("arial.ttf", 18)  
        x1 , y1, x2 ,y2 =  draw.textbbox((0, 0), text=text_to_add, font=font)
        text_width=x2-x1
        text_height=y2-y1
        text_position = (0, qr_image.height - text_height - 10)
        draw.text(text_position, text_to_add, fill="black", font=font)
        
        folder_path='Qr'
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        qr_image.save(folder_path+"/qrcode"+data+".png")
        
        #qr_image.show()

        return 0



if __name__== '__main__':
    app = QApplication(sys.argv)
    scanner = QRCodeScannerApp()
    createQR('1234' , 'myqr')
    scanner.show()

    sys.exit(app.exec_())
