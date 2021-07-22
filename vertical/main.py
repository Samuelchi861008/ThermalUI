# -*- coding: utf-8 -*-
import sys
import cv2
import time
import datetime
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread

# 狀態文字自動清除執行緒
class clearThread(QThread):
    clearStatus = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        while self._run_flag:
            time.sleep(3)
            self.clearStatus.emit("Clear", "")
    
    def stop(self):
        self._run_flag = False
        self.wait()

# 鏡頭執行緒
class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        # 開鏡頭
        cap = cv2.VideoCapture(0)
        while self._run_flag:
            ret, cv_img = cap.read()
            if ret:
                self.change_pixmap_signal.emit(cv_img)
        cap.release()
    
    def stop(self):
        self._run_flag = False
        self.wait()

# 時間跳轉執行緒
class TimeThread(QThread):
    show_time = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self._run_flag = True
    
    # 取得現在日期
    def getNowDate(self):
        date = datetime.datetime.now().date()
        return "{} 年 {} 月 {} 日".format(date.year, date.month, date.day)
    
    # 取得現在時間
    def getNowTime(self):
        time = datetime.datetime.now().time()
        return "{} : {} : {}".format("0"+str(time.hour) if time.hour < 10 else time.hour, "0"+str(time.minute) if time.minute < 10 else time.minute, "0"+str(time.second) if time.second < 10 else time.second)
    
    def run(self):
        while self._run_flag:
            self.show_time.emit(self.getNowDate(), self.getNowTime())
            time.sleep(1)
    
    def stop(self):
        self._run_flag = False
        self.wait()

# 介面
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.disply_width = 480 # 視窗寬
        self.display_height = 800 # 視窗高
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(self.disply_width, self.display_height) # 設定視窗大小
        MainWindow.setStyleSheet("background-color: rgb(129, 50, 52);") # 設定背景顏色
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(9, 10, 480, 51))
        font = QtGui.QFont()
        font.setFamily("Hannotate TC")
        font.setPointSize(36) # 設定標題大小
        font.setBold(True)
        font.setWeight(60) # 設定標題粗細
        self.Title.setFont(font)
        self.Title.setAutoFillBackground(False)
        self.Title.setStyleSheet("color: rgb(255, 255, 255)") # 設定標題顏色
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")

        self.NTNULogo = QtWidgets.QLabel(self.centralwidget)
        self.NTNULogo.setGeometry(QtCore.QRect(10, 740, 261, 51))
        self.NTNULogo.setPixmap(QtGui.QPixmap("img/NB_NTNU_logo.png")) # 設定引入師大 logo 圖片
        self.NTNULogo.setObjectName("NTNULogo")

        self.Video = QtWidgets.QLabel(self.centralwidget)
        self.Video.setGeometry(QtCore.QRect(10, 70, 460, 661))
        self.Video.setObjectName("Video")
        self.Video.setAlignment(QtCore.Qt.AlignCenter)

        self.Status = QtWidgets.QLabel(self.centralwidget)
        self.Status.setGeometry(QtCore.QRect(220, 670, 250, 51))
        self.Status.setStyleSheet("background-color: transparent;")
        self.Status.setObjectName("Status")
        
        self.StatusText = QtWidgets.QLabel(self.centralwidget)
        self.StatusText.setGeometry(QtCore.QRect(280, 685, 156, 20))
        font = QtGui.QFont()
        font.setPointSize(14) # 設定狀態框文字大小
        font.setBold(True)
        font.setWeight(70) # 設定狀態框文字粗細
        self.StatusText.setFont(font)
        self.StatusText.setStyleSheet("background-color:transparent;")
        self.StatusText.setAlignment(QtCore.Qt.AlignCenter)
        self.StatusText.setObjectName("StatusText")

        self.DateTimeArea = QtWidgets.QLabel(self.centralwidget)
        self.DateTimeArea.setGeometry(QtCore.QRect(20, 100, 201, 121))
        self.DateTimeArea.setStyleSheet("background-color: transparent;")
        self.DateTimeArea.setPixmap(QtGui.QPixmap("img/area.png")) # 設定引入日期時間底框圖片
        self.DateTimeArea.setObjectName("DateTimeArea")

        self.DateText = QtWidgets.QLabel(self.centralwidget)
        self.DateText.setGeometry(QtCore.QRect(0, 135, 201, 20))
        font = QtGui.QFont()
        font.setFamily("Hannotate TC")
        font.setPointSize(16) # 設定日期文字大小
        font.setBold(True)
        font.setWeight(70) # 設定日期文字粗細
        self.DateText.setFont(font)
        self.DateText.setStyleSheet("background-color: transparent; color:white;")
        self.DateText.setAlignment(QtCore.Qt.AlignCenter)
        self.DateText.setObjectName("DateText")

        self.TimeText = QtWidgets.QLabel(self.centralwidget)
        self.TimeText.setGeometry(QtCore.QRect(0, 165, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Hannotate TC")
        font.setPointSize(16) # 設定時間文字大小
        font.setBold(True)
        font.setWeight(70) # 設定時間文字粗細
        self.TimeText.setFont(font)
        self.TimeText.setStyleSheet("background-color: transparent; color:white;")
        self.TimeText.setAlignment(QtCore.Qt.AlignCenter)
        self.TimeText.setObjectName("TimeText")

        self.Location = QtWidgets.QLabel(self.centralwidget)
        self.Location.setGeometry(QtCore.QRect(420, 770, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Hannotate TC")
        font.setPointSize(12) # 設定地點文字大小
        font.setBold(True)
        font.setWeight(70) # 設定地點文字粗細
        self.Location.setFont(font)
        self.Location.setStyleSheet("color:white") # 設定地點文字顏色
        self.Location.setObjectName("Location")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DayPass"))
        self.Title.setText(_translate("MainWindow", "智慧額溫 2.0")) # 設定標題文字

        # 設定地點文字
        self.Location.setText(_translate("MainWindow", "公館校區"))

        # 設定即時影像
        self.thread_1 = VideoThread()
        self.thread_1.change_pixmap_signal.connect(self.update_image)
        self.thread_1.start()

        # 設定日期與時間
        self.thread_2 = TimeThread()
        self.thread_2.show_time.connect(self.update_time)
        self.thread_2.start()

        # 設定時間清除文字
        self.thread_3 = clearThread()
        self.thread_3.clearStatus.connect(self.update_status)
        self.thread_3.start()
    
    def update_image(self, cv_img):
        qt_img = self.convert_cv_qt(cv_img)
        self.Video.setPixmap(qt_img)
    
    def update_time(self, date, time):
        self.DateText.setText(date)
        self.TimeText.setText(time)

    def update_status(self, status, text):
        if status == "Error": # Error Status
            self.Status.setPixmap(QtGui.QPixmap("img/NB_QRC_Error.png"))
        elif status == "Clear": # Clear Status
            self.Status.setPixmap(QtGui.QPixmap(""))
        else: # OK Status
            self.Status.setPixmap(QtGui.QPixmap("img/NB_QRC_OK.png"))
        self.StatusText.setText(text) # Status Text
    
    def convert_cv_qt(self, cv_img):
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(600, 600, Qt.KeepAspectRatioByExpanding) # 設定影像大小
        return QtGui.QPixmap.fromImage(p)
    
    def closeEvent(self, event):
        self.thread_1.stop()
        self.thread_2.stop()
        self.thread_3.stop()
        event.accept()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()

    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())