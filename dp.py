import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap

class ProfilePictureUpdater(QWidget):
    def __init__(self):
        super().__init__()

        self.profile_picture_label = QLabel()
        self.select_picture_button = QPushButton("Select Profile Picture")

        layout = QVBoxLayout(self)
        layout.addWidget(self.profile_picture_label)
        layout.addWidget(self.select_picture_button)

        self.select_picture_button.clicked.connect(self.choose_profile_picture)

    def update_profile_picture(self, image_path: str) -> None:
        # Load the new pixmap
        new_pixmap = QPixmap(image_path)

        # Check if the pixmap is valid
        if new_pixmap.isNull():
            # Handle the case where the image could not be loaded
            print(f"Error loading image: {image_path}")
            return

        # Set the new pixmap to the QLabel
        self.profile_picture_label.setPixmap(new_pixmap)

        # Optionally, you can adjust the size to fit the QLabel
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
                self.update_profile_picture(selected_file)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProfilePictureUpdater()
    window.show()
    sys.exit(app.exec_())
