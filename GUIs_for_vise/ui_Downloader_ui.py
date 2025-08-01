# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Downloader_uiPZQCfW.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(669, 207)
        MainWindow.setStyleSheet(u"background-color: rgb(86, 86, 86);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.link_enter = QLineEdit(self.centralwidget)
        self.link_enter.setObjectName(u"link_enter")
        self.link_enter.setGeometry(QRect(10, 40, 651, 121))
        self.link_enter.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(109, 109, 109);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 651, 21))
        self.btn_cancel = QPushButton(self.centralwidget)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setGeometry(QRect(554, 170, 101, 31))
        self.btn_cancel.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(109, 109, 109);")
        self.btn_download = QPushButton(self.centralwidget)
        self.btn_download.setObjectName(u"btn_download")
        self.btn_download.setGeometry(QRect(450, 170, 101, 31))
        self.btn_download.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(109, 109, 109);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.link_enter.setText("")
        self.link_enter.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Link here........", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700; font-style:italic; color:#ffffff;\">Enter Download Link here ===&gt;&gt;&gt;&gt;</span></p></body></html>", None))
        self.btn_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.btn_download.setText(QCoreApplication.translate("MainWindow", u"Download", None))
    # retranslateUi

