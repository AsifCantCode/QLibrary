import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the UI from the .ui file dynamically
        loadUi('login.ui', self)

        # Connect the button click event to a function
        self.pushButton.clicked.connect(self.update_label_text)

    def update_label_text(self):
        # Dynamically update the text of the label
        new_text = "Dynamic Update Successful!"
        self.label.setText(new_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
