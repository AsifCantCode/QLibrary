import sys
import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt, QTimer
from pyzbar.pyzbar import decode

class QRCodeScannerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('QR Code Scanner')
        self.setGeometry(100, 100, 640, 480)

        self.camera = cv2.VideoCapture(0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateFrame)
        self.timer.start(50)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)

        self.button = QPushButton('Scan QR Code', self)
        self.button.clicked.connect(self.scanQRCode)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.button)

        self.setLayout(layout)

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    scanner = QRCodeScannerApp()
    scanner.show()
    sys.exit(app.exec_())
