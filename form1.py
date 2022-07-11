# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
import json
import requests


class Ui_MainWindow(object):
    # def __init__(self):
    #     self.date
    #     self.movieText

    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(796, 404)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.button1 = QPushButton(self.centralwidget)
        self.button1.setObjectName(u"button1")
        self.button1.setGeometry(QRect(670, 240, 111, 31))
        self.calendarWidget = QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(480, 20, 301, 211))
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(10, 20, 461, 211))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(480, 0, 101, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 0, 121, 16))
        self.absoluteCheckBox = QCheckBox(self.centralwidget)
        self.absoluteCheckBox.setObjectName(u"absoluteCheckBox")
        self.absoluteCheckBox.setGeometry(QRect(10, 230, 70, 17))
        self.button2 = QPushButton(self.centralwidget)
        self.button2.setObjectName(u"button2")
        self.button2.setGeometry(QRect(670, 270, 111, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 796, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Movie Creater", None))
        self.button1.setText(QCoreApplication.translate("MainWindow", u"Add New Movie", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"View Date", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Movie Info Text", None))
        self.absoluteCheckBox.setText(QCoreApplication.translate("MainWindow", u"Absolute", None))
        self.button2.setText(QCoreApplication.translate("MainWindow", u"Collection Add", None))
    # retranslateUi


    def button1Clicked(self):
        put_uri = "http://localhost:8080/rest/createamoviefromtext"
        date_str = self.calendarWidget.selectedDate().toString(Qt.ISODate)
        absolute_checked = self.absoluteCheckBox.isChecked()
        if absolute_checked == True:
            date_str = "NONE"

        movie_info = {
            "info": self.plainTextEdit.toPlainText(),
            "viewDate": date_str,
            "absolute": absolute_checked
        }
        response = requests.put(put_uri, json=movie_info)
        if response.status_code == 200:
            print("Movie created.")
        else:
            print("There was a problem.")

    def button2Clicked(self):
        print("Hi!")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
