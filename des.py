# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_fon(object):
    def setupUi(self, fon):
        fon.setObjectName("fon")
        fon.resize(521, 470)
        fon.setMinimumSize(QtCore.QSize(521, 470))
        fon.setMaximumSize(QtCore.QSize(521, 470))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("YouTube_23392.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        fon.setWindowIcon(icon)
        fon.setStyleSheet("background:#1a1a1a")
        self.centralwidget = QtWidgets.QWidget(fon)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 385, 241, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"border: 2px solid #666;\n"
"background-color: #404040;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid #666;\n"
"background-color: #3b3b3b;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border: 2px solid white;\n"
"background-color: #444444;\n"
"color: white;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("downloads_folder_20356.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 385, 251, 31))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"border: 2px solid #666;\n"
"background-color: #404040;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid #666;\n"
"background-color: #3b3b3b;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border: 2px solid white;\n"
"background-color: #444444;\n"
"color: white;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("1486485559-118arrow-down-download-downloads-downloading-save_81191.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 345, 501, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border: 2px solid #666;\n"
"        background-color: #3b3b3b;\n"
"        color: white;")
        self.lineEdit.setObjectName("lineEdit")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 315, 501, 23))
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    background-color: #404040;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #292929;\n"
"    width: 20px;\n"
"}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.title1 = QtWidgets.QLabel(self.centralwidget)
        self.title1.setGeometry(QtCore.QRect(10, 291, 501, 20))
        self.title1.setStyleSheet("color: #fff;")
        self.title1.setObjectName("title1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 501, 281))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("loading.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 420, 241, 31))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"border: 2px solid #666;\n"
"background-color: #404040;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid #666;\n"
"background-color: #3b3b3b;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border: 2px solid white;\n"
"background-color: #444444;\n"
"color: white;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("sunrise_sun_sunny_shower_showers_sunny_cloudy_fog_day_time_1458.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(260, 420, 251, 31))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"border: 2px solid #666;\n"
"background-color: #404040;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid #666;\n"
"background-color: #3b3b3b;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border: 2px solid white;\n"
"background-color: #444444;\n"
"color: white;\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("640crescentmoon_100402.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setObjectName("pushButton_4")
        self.title1_2 = QtWidgets.QLabel(self.centralwidget)
        self.title1_2.setGeometry(QtCore.QRect(10, 450, 501, 20))
        self.title1_2.setStyleSheet("color: #fff;")
        self.title1_2.setObjectName("title1_2")
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.lineEdit.raise_()
        self.progressBar.raise_()
        self.title1.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.label_2.raise_()
        self.title1_2.raise_()
        fon.setCentralWidget(self.centralwidget)

        self.retranslateUi(fon)
        QtCore.QMetaObject.connectSlotsByName(fon)

    def retranslateUi(self, fon):
        _translate = QtCore.QCoreApplication.translate
        fon.setWindowTitle(_translate("fon", "YouTube Downloader from Timur =)"))
        self.pushButton.setText(_translate("fon", "Выбрать папку для сохранения"))
        self.pushButton_2.setText(_translate("fon", "Скачать!"))
        self.lineEdit.setPlaceholderText(_translate("fon", "https://youtube.com/VideoID"))
        self.title1.setText(_translate("fon", "Название видео:"))
        self.pushButton_3.setText(_translate("fon", "Светлый режим"))
        self.pushButton_4.setText(_translate("fon", "Ночной режим"))
        self.title1_2.setText(_translate("fon", "Статус загрузки: Ожидание действий пользователя"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fon = QtWidgets.QMainWindow()
    ui = Ui_fon()
    ui.setupUi(fon)
    fon.show()
    sys.exit(app.exec_())