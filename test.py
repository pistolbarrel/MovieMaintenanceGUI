# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\NextGen.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


def print_result(status_code, good_description):
    if status_code == 200:
        print(good_description)
    else:
        print("There was a problem.")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(488, 457)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(1, 1, 801, 471))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 20, 477, 237))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.dateEdit = QtWidgets.QDateEdit(self.tab)
        self.dateEdit.setGeometry(QtCore.QRect(1, 260, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setGeometry(QtCore.QRect(402, 264, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(205, 274, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(2, 0, 61, 16))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab, "")
        # tab 2
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(2, 19, 464, 26))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(3, 3, 67, 16))
        self.label_2.setObjectName("label_2")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(3, 71, 467, 101))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(5, 55, 93, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(2, 180, 115, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab_2, "")
        # tab 3
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.tab_3)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setGeometry(QtCore.QRect(2, 17, 376, 26))
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QtCore.QRect(5, 0, 88, 16))
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QtCore.QRect(2, 47, 75, 23))
        self.tabWidget.addTab(self.tab_3, "")


        # ########################################################
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.tab1ButtonClicked)
        self.dateEdit.setDate(QtCore.QDate.currentDate())

        self.pushButton_2.clicked.connect(self.tab2ButtonClicked)

        self.pushButton_3.clicked.connect(self.tab3ButtonClicked)

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Movie Maint"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.checkBox.setText(_translate("MainWindow", "Absolute"))
        self.checkBox.setToolTip("Check to remove all joined data and replace with Movie Text supplied.")
        self.pushButton.setText(_translate("MainWindow", "Add Movie"))
        self.label.setText(_translate("MainWindow", "Movie Text"))
        self.label_2.setText(_translate("MainWindow", "Series Name"))
        self.label_3.setText(_translate("MainWindow", "Movies in Series"))
        self.pushButton_2.setText(_translate("MainWindow", "Add Series to Existing"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", u"AddSeries"))
        self.label_4.setText(_translate("MainWindow", u"Movie Title (Year)"))
        self.pushButton_3.setText(_translate("MainWindow", u"Publish"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Add Movie"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Add Series to Existing"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", u"WatchedToday"))

    def tab1ButtonClicked(self):

        put_uri = "http://localhost:8080/rest/createamoviefromtext"
        date_str = self.dateEdit.date().toString(Qt.ISODate)
        absolute_checked = self.checkBox.isChecked()
        if absolute_checked == True:
            date_str = "NONE"

        movie_info = {
            "info": self.plainTextEdit.toPlainText(),
            "viewDate": date_str,
            "absolute": absolute_checked
        }
        a = 42
        response = requests.put(put_uri, json=movie_info)
        print_result(response.status_code, "Movie created.")

    def tab2ButtonClicked(self):
        put_uri = "http://localhost:8080/rest/updatecollectionsonexisting"
        collections_info = {
            "titles": self.plainTextEdit_3.toPlainText(),
            "collection": self.plainTextEdit_2.toPlainText()
        }
        a = 42
        response = requests.put(put_uri, json=collections_info)
        print_result(response.status_code, "Collection added to existing movies.")

    def tab3ButtonClicked(self):
        put_uri = "http://localhost:8080/rest/viewedtoday"
        collections_info = {
            "titles": self.plainTextEdit_4.toPlainText(),
            "collection": "Not Used in service"
        }
        a = 42
        response = requests.put(put_uri, json=collections_info)
        print_result(response.status_code, "Date added.")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
