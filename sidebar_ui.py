# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Radib Bin Kabir\OneDrive\Desktop\RDBMS\Project\FrontendQLib\QLibrary\sidebar.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1105, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.icon_only_widget = QtWidgets.QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName("icon_only_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.logo_label_1 = QtWidgets.QLabel(self.icon_only_widget)
        self.logo_label_1.setMinimumSize(QtCore.QSize(50, 50))
        self.logo_label_1.setMaximumSize(QtCore.QSize(50, 50))
        self.logo_label_1.setText("")
        self.logo_label_1.setPixmap(QtGui.QPixmap("c:\\Users\\Radib Bin Kabir\\OneDrive\\Desktop\\RDBMS\\Project\\FrontendQLib\\QLibrary\\icon/online-library (1).png"))
        self.logo_label_1.setScaledContents(True)
        self.logo_label_1.setObjectName("logo_label_1")
        self.horizontalLayout_3.addWidget(self.logo_label_1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.home_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.home_btn_1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\Radib Bin Kabir\\OneDrive\\Desktop\\RDBMS\\Project\\FrontendQLib\\QLibrary\\icon/icons8-home-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\Radib Bin Kabir\\OneDrive\\Desktop\\RDBMS\\Project\\FrontendQLib\\QLibrary\\icon/icons8-home-50 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.home_btn_1.setIcon(icon)
        self.home_btn_1.setIconSize(QtCore.QSize(22, 28))
        self.home_btn_1.setCheckable(True)
        self.home_btn_1.setAutoExclusive(True)
        self.home_btn_1.setObjectName("home_btn_1")
        self.verticalLayout.addWidget(self.home_btn_1)
        self.dashborad_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.dashborad_btn_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\Radib Bin Kabir\\OneDrive\\Desktop\\RDBMS\\Project\\FrontendQLib\\QLibrary\\icon/icons8-qr-code-24 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\Radib Bin Kabir\\OneDrive\\Desktop\\RDBMS\\Project\\FrontendQLib\\QLibrary\\icon/icons8-qr-code-64 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.dashborad_btn_1.setIcon(icon1)
        self.dashborad_btn_1.setIconSize(QtCore.QSize(22, 28))
        self.dashborad_btn_1.setCheckable(True)
        self.dashborad_btn_1.setAutoExclusive(True)
        self.dashborad_btn_1.setObjectName("dashborad_btn_1")
        self.verticalLayout.addWidget(self.dashborad_btn_1)
        self.orders_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.orders_btn_1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\Radib Bin Kabir\\OneDrive\\Desktop\\RDBMS\\Project\\FrontendQLib\\QLibrary\\icon/icons8-upload-to-ftp-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\Radib Bin Kabir\\OneDrive\\Desktop\\RDBMS\\Project\\FrontendQLib\\QLibrary\\icon/icons8-upload-to-ftp-24 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.orders_btn_1.setIcon(icon2)
        self.orders_btn_1.setIconSize(QtCore.QSize(22, 28))
        self.orders_btn_1.setCheckable(True)
        self.orders_btn_1.setAutoExclusive(True)
        self.orders_btn_1.setObjectName("orders_btn_1")
        self.verticalLayout.addWidget(self.orders_btn_1)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.customers_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.customers_btn_1.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("c:\\Users\\Radib Bin Kabir\\OneDrive\\Desktop\\RDBMS\\Project\\FrontendQLib\\QLibrary\\icon/icons8-knowledge-sharing-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap("c:\\Users\\Radib Bin Kabir\\OneDrive\\Desktop\\RDBMS\\Project\\FrontendQLib\\QLibrary\\icon/icons8-knowledge-sharing-48 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.customers_btn_1.setIcon(icon3)
        self.customers_btn_1.setIconSize(QtCore.QSize(22, 28))
        self.customers_btn_1.setCheckable(True)
        self.customers_btn_1.setAutoExclusive(True)
        self.customers_btn_1.setObjectName("customers_btn_1")
        self.verticalLayout_3.addWidget(self.customers_btn_1)
        self.products_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.products_btn_1.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("c:\\Users\\Radib Bin Kabir\\OneDrive\\Desktop\\RDBMS\\Project\\FrontendQLib\\QLibrary\\icon/icons8-message-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap("c:\\Users\\Radib Bin Kabir\\OneDrive\\Desktop\\RDBMS\\Project\\FrontendQLib\\QLibrary\\icon/icons8-message-24 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.products_btn_1.setIcon(icon4)
        self.products_btn_1.setIconSize(QtCore.QSize(21, 28))
        self.products_btn_1.setCheckable(True)
        self.products_btn_1.setAutoExclusive(True)
        self.products_btn_1.setObjectName("products_btn_1")
        self.verticalLayout_3.addWidget(self.products_btn_1)
        spacerItem = QtWidgets.QSpacerItem(20, 375, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.exit_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.exit_btn_1.setStyleSheet("/* Style for QPushButton */\n"
"QPushButton {\n"
"    background-color: #FFA500; /* Orange background color */\n"
"    color: #000000; /* Black text color */\n"
"    border: 1px solid #000000; /* Black border */\n"
"    border-radius: 3px; /* Rounded corners */\n"
"}\n"
"\n"
"/* QPushButton when hovered */\n"
"QPushButton:hover {\n"
"    background-color: #FFD700; /* Lighter orange on hover */\n"
"}\n"
"")
        self.exit_btn_1.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("c:\\Users\\Radib Bin Kabir\\OneDrive\\Desktop\\RDBMS\\Project\\FrontendQLib\\QLibrary\\icon/icons8-imac-exit-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn_1.setIcon(icon5)
        self.exit_btn_1.setIconSize(QtCore.QSize(22, 24))
        self.exit_btn_1.setObjectName("exit_btn_1")
        self.verticalLayout_3.addWidget(self.exit_btn_1)
        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget = QtWidgets.QWidget(self.widget_3)
        self.widget.setMinimumSize(QtCore.QSize(0, 40))
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 9, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.change_btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.change_btn.setFont(font)
        self.change_btn.setStyleSheet("/* Style for QPushButton */\n"
"QPushButton {\n"
"    background-color: #FFA500; /* Orange background color */\n"
"    color: #000000; /* Black text color */\n"
"    border: 1px solid #000000; /* Black border */\n"
"    border-radius: 3px; /* Rounded corners */\n"
"    padding: 5px 10px; /* Padding around the button text */\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"/* QPushButton when hovered */\n"
"QPushButton:hover {\n"
"    background-color: #FFD700; /* Lighter orange on hover */\n"
"}\n"
"")
        self.change_btn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/icon/menu-4-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.change_btn.setIcon(icon6)
        self.change_btn.setIconSize(QtCore.QSize(16, 24))
        self.change_btn.setCheckable(True)
        self.change_btn.setChecked(False)
        self.change_btn.setObjectName("change_btn")
        self.horizontalLayout_4.addWidget(self.change_btn)
        spacerItem1 = QtWidgets.QSpacerItem(236, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search_input = QtWidgets.QLineEdit(self.widget)
        self.search_input.setStyleSheet("/* Style for QLineEdit */\n"
"QLineEdit {\n"
"    border: 1px solid #999999; /* Border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding: 5px; /* Padding inside the QLineEdit */\n"
"    font-family: Arial, sans-serif; /* Font family */\n"
"    font-size: 14px; /* Font size */\n"
"    color: #333333; /* Text color */\n"
"    background-color: #FFFFFF; /* Background color */\n"
"}\n"
"\n"
"/* Style for a focused QLineEdit */\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4A90E2; /* Border when focused */\n"
"}\n"
"\n"
"/* Style for a disabled QLineEdit */\n"
"QLineEdit:disabled {\n"
"    background-color: #dff2ff; /* Background color for disabled state */\n"
"    color: #999999; /* Text color for disabled state */\n"
"}\n"
"")
        self.search_input.setObjectName("search_input")
        self.horizontalLayout.addWidget(self.search_input)
        self.search_btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.search_btn.setFont(font)
        self.search_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search_btn.setStyleSheet("QPushButton:hover {\n"
"    background-color: #f0ffed; /* Teal color */\n"
"}\n"
"")
        self.search_btn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("c:\\Users\\Radib Bin Kabir\\OneDrive\\Desktop\\RDBMS\\Project\\FrontendQLib\\QLibrary\\icon/icons8-search-128 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_btn.setIcon(icon7)
        self.search_btn.setIconSize(QtCore.QSize(28, 29))
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout.addWidget(self.search_btn)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(236, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.user_btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.user_btn.setFont(font)
        self.user_btn.setStyleSheet("/* Style for QPushButton */\n"
"QPushButton {\n"
"    background-color: #FFA500; /* Orange background color */\n"
"    color: #000000; /* Black text color */\n"
"    border: 1px solid #000000; /* Black border */\n"
"    border-radius: 3px; /* Rounded corners */\n"
"    padding: 4px 8px; /* Padding around the button text */\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"/* QPushButton when hovered */\n"
"QPushButton:hover {\n"
"    background-color: #FFD700; /* Lighter orange on hover */\n"
"}\n"
"")
        self.user_btn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("c:\\Users\\Radib Bin Kabir\\OneDrive\\Desktop\\RDBMS\\Project\\FrontendQLib\\QLibrary\\icon/icons8-male-user-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.user_btn.setIcon(icon8)
        self.user_btn.setIconSize(QtCore.QSize(24, 29))
        self.user_btn.setObjectName("user_btn")
        self.horizontalLayout_4.addWidget(self.user_btn)
        self.verticalLayout_5.addWidget(self.widget)
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.page_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 120, 331, 411))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("/* Style for QLabel */\n"
"QLabel {\n"
"    color: #3700B3; /* Text color */\n"
"    font-family: Arial, sans-serif; /* Font family */\n"
"    font-size: 18px; /* Font size */\n"
"    border: 2px solid #CCCCCC; /* Border */\n"
"    padding: 8px; /* Padding around the content */\n"
"    background-color: #FFFFFF; /* Background color */\n"
"}\n"
"\n"
"/* QLabel when it\'s disabled */\n"
"QLabel:disabled {\n"
"    color: #999999; /* Text color for disabled state */\n"
"    background-color: #F5F5F5; /* Background color for disabled state */\n"
"}\n"
"\n"
"/* QLabel with hover effect */\n"
"QLabel:hover {\n"
"    background-color: #86fefff5; /* Background color on hover */\n"
"}\n"
"\n"
"/* QLabel when clicked (pressed) */\n"
"QLabel:pressed {\n"
"    background-color: #CCCCCC; /* Background color when clicked */\n"
"}\n"
"")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.booklist = QtWidgets.QListView(self.verticalLayoutWidget_2)
        self.booklist.setStyleSheet("    background-color: #f4fdff; /* Background color */\n"
"    border: 1px solid #000000; /* Border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding: 10px;\n"
"\n"
"/* Style for items (list items) within QListView */\n"
"QListView::item {\n"
"    background-color: #FFFFFF; /* Item background color */\n"
"    border: 1px solid #DDDDDD; /* Item border */\n"
"    border-radius: 2px; /* Rounded corners for items */\n"
"    padding: 5px; /* Padding around each item */\n"
"}\n"
"\n"
"/* Style for selected items within QListView */\n"
"QListView::item:selected {\n"
"    background-color: #4A90E2; /* Background color when selected */\n"
"    color: #FFFFFF; /* Text color when selected */\n"
"}\n"
"")
        self.booklist.setObjectName("booklist")
        self.verticalLayout_6.addWidget(self.booklist)
        self.borrowerlabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.borrowerlabel.setStyleSheet("/* Style for QLabel */\n"
"QLabel {\n"
"    color: #3700B3; /* Text color */\n"
"    font-family: Arial, sans-serif; /* Font family */\n"
"    font-size: 18px; /* Font size */\n"
"    border: 2px solid #CCCCCC; /* Border */\n"
"    padding: 8px; /* Padding around the content */\n"
"    background-color: #FFFFFF; /* Background color */\n"
"}\n"
"\n"
"/* QLabel when it\'s disabled */\n"
"QLabel:disabled {\n"
"    color: #999999; /* Text color for disabled state */\n"
"    background-color: #F5F5F5; /* Background color for disabled state */\n"
"}\n"
"\n"
"/* QLabel with hover effect */\n"
"QLabel:hover {\n"
"    background-color: #86fefff5; /* Background color on hover */\n"
"}\n"
"\n"
"/* QLabel when clicked (pressed) */\n"
"QLabel:pressed {\n"
"    background-color: #CCCCCC; /* Background color when clicked */\n"
"}\n"
"")
        self.borrowerlabel.setObjectName("borrowerlabel")
        self.verticalLayout_6.addWidget(self.borrowerlabel)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.serportclose = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.serportclose.setStyleSheet("/* Style for QPushButton */\n"
"QPushButton {\n"
"    background-color: #FFA500; /* Orange background color */\n"
"    color: #000000; /* Black text color */\n"
"    border: 1px solid #000000; /* Black border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding: 8px 10px; /* Padding around the button text */\n"
"    font-size: 15px;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"/* QPushButton when hovered */\n"
"QPushButton:hover {\n"
"    background-color: #FFD700; /* Lighter orange on hover */\n"
"}\n"
"")
        self.serportclose.setObjectName("serportclose")
        self.horizontalLayout_6.addWidget(self.serportclose)
        self.initborrow = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.initborrow.setStyleSheet("/* Style for QPushButton */\n"
"QPushButton {\n"
"    background-color: #FFA500; /* Orange background color */\n"
"    color: #000000; /* Black text color */\n"
"    border: 1px solid #000000; /* Black border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding: 8px 10px; /* Padding around the button text */\n"
"    font-size: 15px;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"/* QPushButton when hovered */\n"
"QPushButton:hover {\n"
"    background-color: #FFD700; /* Lighter orange on hover */\n"
"}\n"
"")
        self.initborrow.setFlat(False)
        self.initborrow.setObjectName("initborrow")
        self.horizontalLayout_6.addWidget(self.initborrow)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.image_label = QtWidgets.QLabel(self.page_2)
        self.image_label.setGeometry(QtCore.QRect(370, 120, 501, 411))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.image_label.setFont(font)
        self.image_label.setStyleSheet("border: 3px solid black;\n"
"padding: 2px;\n"
"border-radius: 5px;\n"
"")
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")
        self.scannedlabel = QtWidgets.QLabel(self.page_2)
        self.scannedlabel.setGeometry(QtCore.QRect(560, 530, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.scannedlabel.setFont(font)
        self.scannedlabel.setObjectName("scannedlabel")
        self.loadingLabel = QtWidgets.QLabel(self.page_2)
        self.loadingLabel.setGeometry(QtCore.QRect(570, 260, 101, 111))
        self.loadingLabel.setStyleSheet("image: url(:/icon/icon/loadingR.gif);")
        self.loadingLabel.setText("")
        self.loadingLabel.setObjectName("loadingLabel")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.page_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(300, 330, 391, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("/* Style for QLabel */\n"
"QLabel {\n"
"    color: #3700B3; /* Text color */\n"
"    font-family: Arial, sans-serif; /* Font family */\n"
"    font-size: 22px; /* Font size */\n"
"    border: 2px solid #CCCCCC; /* Border */\n"
"    padding: 5px; /* Padding around the content */\n"
"    background-color: #FFFFFF; /* Background color */\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"/* QLabel when it\'s disabled */\n"
"QLabel:disabled {\n"
"    color: #999999; /* Text color for disabled state */\n"
"    background-color: #F5F5F5; /* Background color for disabled state */\n"
"}\n"
"\n"
"/* QLabel with hover effect */\n"
"QLabel:hover {\n"
"    background-color: #86fefff5; /* Background color on hover */\n"
"}\n"
"\n"
"/* QLabel when clicked (pressed) */\n"
"QLabel:pressed {\n"
"    background-color: #CCCCCC; /* Background color when clicked */\n"
"}\n"
"")
        self.label.setObjectName("label")
        self.verticalLayout_8.addWidget(self.label)
        self.bookbtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bookbtn.setStyleSheet("/* Style for QPushButton */\n"
"QPushButton {\n"
"    background-color: #FFA500; /* Orange background color */\n"
"    color: #000000; /* Black text color */\n"
"    border: 1px solid #000000; /* Black border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding: 7px 10px; /* Padding around the button text */\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"/* QPushButton when hovered */\n"
"QPushButton:hover {\n"
"    background-color: #FFD700; /* Lighter orange on hover */\n"
"}\n"
"")
        self.bookbtn.setObjectName("bookbtn")
        self.verticalLayout_8.addWidget(self.bookbtn)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.page_3)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(300, 160, 391, 101))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_2.setStyleSheet("/* Style for QLabel */\n"
"QLabel {\n"
"    color: #3700B3; /* Text color */\n"
"    font-family: Arial, sans-serif; /* Font family */\n"
"    font-size: 22px; /* Font size */\n"
"    border: 2px solid #CCCCCC; /* Border */\n"
"    padding: 5px; /* Padding around the content */\n"
"    background-color: #FFFFFF; /* Background color */\n"
"    font-weight: 500;\n"
"\n"
"}\n"
"\n"
"/* QLabel when it\'s disabled */\n"
"QLabel:disabled {\n"
"    color: #999999; /* Text color for disabled state */\n"
"    background-color: #F5F5F5; /* Background color for disabled state */\n"
"}\n"
"\n"
"/* QLabel with hover effect */\n"
"QLabel:hover {\n"
"    background-color: #86fefff5; /* Background color on hover */\n"
"}\n"
"\n"
"/* QLabel when clicked (pressed) */\n"
"QLabel:pressed {\n"
"    background-color: #CCCCCC; /* Background color when clicked */\n"
"}\n"
"")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        self.authbtn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.authbtn.setStyleSheet("/* Style for QPushButton */\n"
"QPushButton {\n"
"    background-color: #FFA500; /* Orange background color */\n"
"    color: #000000; /* Black text color */\n"
"    border: 1px solid #000000; /* Black border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding: 7px 10px; /* Padding around the button text */\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"/* QPushButton when hovered */\n"
"QPushButton:hover {\n"
"    background-color: #FFD700; /* Lighter orange on hover */\n"
"}\n"
"")
        self.authbtn.setObjectName("authbtn")
        self.verticalLayout_7.addWidget(self.authbtn)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_7 = QtWidgets.QLabel(self.page_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_8 = QtWidgets.QLabel(self.page_5)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_9 = QtWidgets.QLabel(self.page_6)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_7.addWidget(self.label_9, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_7)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_10 = QtWidgets.QLabel(self.page_7)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_8.addWidget(self.label_10, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_7)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)
        self.full_menu_widget = QtWidgets.QWidget(self.centralwidget)
        self.full_menu_widget.setObjectName("full_menu_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.logo_label_2 = QtWidgets.QLabel(self.full_menu_widget)
        self.logo_label_2.setMinimumSize(QtCore.QSize(44, 44))
        self.logo_label_2.setMaximumSize(QtCore.QSize(40, 40))
        self.logo_label_2.setText("")
        self.logo_label_2.setPixmap(QtGui.QPixmap("c:\\Users\\Radib Bin Kabir\\OneDrive\\Desktop\\RDBMS\\Project\\FrontendQLib\\QLibrary\\icon/online-library (1).png"))
        self.logo_label_2.setScaledContents(True)
        self.logo_label_2.setObjectName("logo_label_2")
        self.horizontalLayout_2.addWidget(self.logo_label_2)
        self.logo_label_3 = QtWidgets.QLabel(self.full_menu_widget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.logo_label_3.setFont(font)
        self.logo_label_3.setObjectName("logo_label_3")
        self.horizontalLayout_2.addWidget(self.logo_label_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.home_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.home_btn_2.setFont(font)
        self.home_btn_2.setIcon(icon)
        self.home_btn_2.setIconSize(QtCore.QSize(18, 24))
        self.home_btn_2.setCheckable(True)
        self.home_btn_2.setAutoExclusive(True)
        self.home_btn_2.setObjectName("home_btn_2")
        self.verticalLayout_2.addWidget(self.home_btn_2)
        self.dashborad_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.dashborad_btn_2.setFont(font)
        self.dashborad_btn_2.setIcon(icon1)
        self.dashborad_btn_2.setIconSize(QtCore.QSize(18, 24))
        self.dashborad_btn_2.setCheckable(True)
        self.dashborad_btn_2.setAutoExclusive(True)
        self.dashborad_btn_2.setObjectName("dashborad_btn_2")
        self.verticalLayout_2.addWidget(self.dashborad_btn_2)
        self.orders_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.orders_btn_2.setFont(font)
        self.orders_btn_2.setIcon(icon2)
        self.orders_btn_2.setIconSize(QtCore.QSize(18, 24))
        self.orders_btn_2.setCheckable(True)
        self.orders_btn_2.setAutoExclusive(True)
        self.orders_btn_2.setObjectName("orders_btn_2")
        self.verticalLayout_2.addWidget(self.orders_btn_2)
        self.customers_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.customers_btn_2.setFont(font)
        self.customers_btn_2.setIcon(icon3)
        self.customers_btn_2.setIconSize(QtCore.QSize(18, 24))
        self.customers_btn_2.setCheckable(True)
        self.customers_btn_2.setAutoExclusive(True)
        self.customers_btn_2.setObjectName("customers_btn_2")
        self.verticalLayout_2.addWidget(self.customers_btn_2)
        self.products_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.products_btn_2.setFont(font)
        self.products_btn_2.setIcon(icon4)
        self.products_btn_2.setIconSize(QtCore.QSize(18, 24))
        self.products_btn_2.setCheckable(True)
        self.products_btn_2.setAutoExclusive(True)
        self.products_btn_2.setObjectName("products_btn_2")
        self.verticalLayout_2.addWidget(self.products_btn_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 373, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.exit_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.exit_btn_2.setStyleSheet("/* Style for QPushButton */\n"
"QPushButton {\n"
"    background-color: #FFA500; /* Orange background color */\n"
"    color: #000000; /* Black text color */\n"
"    border: 1px solid #000000; /* Black border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding: 5px 10px; /* Padding around the button text */\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"/* QPushButton when hovered */\n"
"QPushButton:hover {\n"
"    background-color: #FFD700; /* Lighter orange on hover */\n"
"}\n"
"")
        self.exit_btn_2.setIcon(icon5)
        self.exit_btn_2.setIconSize(QtCore.QSize(18, 24))
        self.exit_btn_2.setObjectName("exit_btn_2")
        self.verticalLayout_4.addWidget(self.exit_btn_2)
        self.gridLayout.addWidget(self.full_menu_widget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.change_btn.toggled['bool'].connect(self.icon_only_widget.setVisible) # type: ignore
        self.change_btn.toggled['bool'].connect(self.full_menu_widget.setHidden) # type: ignore
        self.home_btn_1.toggled['bool'].connect(self.home_btn_2.setChecked) # type: ignore
        self.dashborad_btn_1.toggled['bool'].connect(self.dashborad_btn_2.setChecked) # type: ignore
        self.orders_btn_1.toggled['bool'].connect(self.orders_btn_2.setChecked) # type: ignore
        self.products_btn_1.toggled['bool'].connect(self.products_btn_2.setChecked) # type: ignore
        self.customers_btn_1.toggled['bool'].connect(self.customers_btn_2.setChecked) # type: ignore
        self.home_btn_2.toggled['bool'].connect(self.home_btn_1.setChecked) # type: ignore
        self.dashborad_btn_2.toggled['bool'].connect(self.dashborad_btn_1.setChecked) # type: ignore
        self.orders_btn_2.toggled['bool'].connect(self.orders_btn_1.setChecked) # type: ignore
        self.products_btn_2.toggled['bool'].connect(self.products_btn_1.setChecked) # type: ignore
        self.customers_btn_2.toggled['bool'].connect(self.customers_btn_1.setChecked) # type: ignore
        self.exit_btn_2.clicked.connect(MainWindow.close) # type: ignore
        self.exit_btn_1.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.search_input.setPlaceholderText(_translate("MainWindow", "Search..."))
        self.label_4.setText(_translate("MainWindow", "Home Page"))
        self.label_3.setText(_translate("MainWindow", "                   BOOK  ITEMS"))
        self.borrowerlabel.setText(_translate("MainWindow", "Borrowed By :"))
        self.serportclose.setText(_translate("MainWindow", "Open Port"))
        self.initborrow.setText(_translate("MainWindow", "Register Borrow"))
        self.scannedlabel.setText(_translate("MainWindow", "scannedlabel"))
        self.label.setText(_translate("MainWindow", "          Upload List of Books"))
        self.bookbtn.setText(_translate("MainWindow", "SELECT CSV"))
        self.label_2.setText(_translate("MainWindow", "         Upload List of Authors"))
        self.authbtn.setText(_translate("MainWindow", "SELECT CSV"))
        self.label_7.setText(_translate("MainWindow", "Product Page"))
        self.label_8.setText(_translate("MainWindow", "Customers Page"))
        self.label_9.setText(_translate("MainWindow", "Search Page"))
        self.label_10.setText(_translate("MainWindow", "User Page"))
        self.logo_label_3.setText(_translate("MainWindow", "QLibrary"))
        self.home_btn_2.setText(_translate("MainWindow", "DASHBOARD"))
        self.dashborad_btn_2.setText(_translate("MainWindow", "SCANNER"))
        self.orders_btn_2.setText(_translate("MainWindow", "UPLOADS"))
        self.customers_btn_2.setText(_translate("MainWindow", "BORROW"))
        self.products_btn_2.setText(_translate("MainWindow", "MESSAGES"))
        self.exit_btn_2.setText(_translate("MainWindow", "EXIT"))
import resource_rc
