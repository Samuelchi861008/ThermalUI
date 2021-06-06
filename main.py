# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setStyleSheet("background-color: rgb(129, 50, 52);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(19, 10, 761, 51))
        font = QtGui.QFont()
        font.setFamily("Hannotate TC")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(60)
        self.Title.setFont(font)
        self.Title.setAutoFillBackground(False)
        self.Title.setStyleSheet("color: rgb(255, 255, 255)")
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")

        self.NTNULogo = QtWidgets.QLabel(self.centralwidget)
        self.NTNULogo.setGeometry(QtCore.QRect(10, 420, 261, 51))
        self.NTNULogo.setText("")
        self.NTNULogo.setPixmap(QtGui.QPixmap("img/NB_NTNU_logo.png"))
        self.NTNULogo.setObjectName("NTNULogo")

        self.Video = QtWidgets.QLabel(self.centralwidget)
        self.Video.setGeometry(QtCore.QRect(10, 80, 771, 331))
        self.Video.setText("")
        self.Video.setPixmap(QtGui.QPixmap("img/QRCodeDemo.png"))
        self.Video.setObjectName("Video")

        self.Status = QtWidgets.QLabel(self.centralwidget)
        self.Status.setGeometry(QtCore.QRect(570, 360, 211, 51))
        self.Status.setStyleSheet("background-color: transparent;")
        self.Status.setText("")
        self.Status.setObjectName("Status")
        self.StatusText = QtWidgets.QLabel(self.centralwidget)
        self.StatusText.setGeometry(QtCore.QRect(610, 375, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.StatusText.setFont(font)
        self.StatusText.setStyleSheet("background-color:transparent;")
        self.StatusText.setAlignment(QtCore.Qt.AlignCenter)
        self.StatusText.setObjectName("StatusText")

        self.DateTimeArea = QtWidgets.QLabel(self.centralwidget)
        self.DateTimeArea.setGeometry(QtCore.QRect(20, 80, 201, 121))
        self.DateTimeArea.setStyleSheet("background-color: transparent;")
        self.DateTimeArea.setText("")
        self.DateTimeArea.setPixmap(QtGui.QPixmap("img/area.png"))
        self.DateTimeArea.setObjectName("DateTimeArea")
        self.DateText = QtWidgets.QLabel(self.centralwidget)
        self.DateText.setGeometry(QtCore.QRect(20, 110, 201, 20))
        font = QtGui.QFont()
        font.setFamily("Hannotate TC")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.DateText.setFont(font)
        self.DateText.setStyleSheet("background-color: transparent; color:white;")
        self.DateText.setAlignment(QtCore.Qt.AlignCenter)
        self.DateText.setObjectName("DateText")

        self.TimeText = QtWidgets.QLabel(self.centralwidget)
        self.TimeText.setGeometry(QtCore.QRect(20, 150, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Hannotate TC")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.TimeText.setFont(font)
        self.TimeText.setStyleSheet("background-color: transparent; color:white;")
        self.TimeText.setAlignment(QtCore.Qt.AlignCenter)
        self.TimeText.setObjectName("label")

        self.location = QtWidgets.QLabel(self.centralwidget)
        self.location.setGeometry(QtCore.QRect(710, 440, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Hannotate TC")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(70)
        self.location.setFont(font)
        self.location.setStyleSheet("color:white")
        self.location.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title.setText(_translate("MainWindow", "智慧額溫 2.0"))

        # self.Status.setPixmap(QtGui.QPixmap("img/NB_QRC_OK.png")) # OK Status
        self.Status.setPixmap(QtGui.QPixmap("img/NB_QRC_Error.png")) # Error Status
        self.StatusText.setText(_translate("MainWindow", "無效 QR Code")) # Status Text

        date = datetime.datetime.now().date()
        time = datetime.datetime.now().time()
        self.DateText.setText(_translate("MainWindow", "{} 年 {} 月 {} 日".format(date.year, date.month, date.day)))
        self.TimeText.setText(_translate("MainWindow", "{} : {}".format("0"+str(time.hour) if time.hour < 10 else time.hour, "0"+str(time.minute) if time.minute < 10 else time.minute)))

        self.location.setText(_translate("MainWindow", "公館校區"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())