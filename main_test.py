# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_test.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import images.image_background_rc
from employer import Employe
from suiviTemps import SuiviTemps
from face_test import Ui_Dialog_face_recog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 900)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(-10, -40, 1500, 900))
        self.widget1.setObjectName("widget1")
        self.label_login = QtWidgets.QLabel(self.widget1)
        self.label_login.setGeometry(QtCore.QRect(480, 220, 491, 641))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_login.setFont(font)
        self.label_login.setStyleSheet("background-color:rgba(0, 0, 0, 150);\n"
"border-radius:20px;")
        self.label_login.setText("")
        self.label_login.setObjectName("label_login")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setGeometry(QtCore.QRect(640, 240, 171, 151))
        self.label_2.setStyleSheet("border-image: url(:/image1/logo2.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.login_button = QtWidgets.QPushButton(self.widget1)
        self.login_button.setGeometry(QtCore.QRect(500, 700, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        self.login_button.setFont(font)
        self.login_button.setStyleSheet("QPushButton#login_button{\n"
"font: 16pt \"Sitka\";\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.488636, stop:0.357955 rgba(0, 208, 111, 255), stop:1 rgba(56, 236, 255, 255));\n"
"border:none;\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QPushButton#login_button:hover{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.488636, stop:0.471591 rgba(2, 0, 153, 255), stop:1 rgba(195, 0, 211, 255));\n"
"color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"\n"
"}")
        self.login_button.setObjectName("login_button")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setGeometry(QtCore.QRect(0, 0, 1500, 901))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("border-image: url(:/image1/Blue Abstract Gradient Background Jamboard Background.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.Name = QtWidgets.QLineEdit(self.widget1)
        self.Name.setGeometry(QtCore.QRect(550, 510, 351, 71))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.Name.setFont(font)
        self.Name.setStyleSheet("QLineEdit#Name{\n"
"font: 14pt \"Sitka\";\n"
"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom: 2px solid rgba(105, 118, 132, 255);\n"
"color:white;\n"
"padding-bottom: 7px;\n"
"}\n"
"QLineEdit#Name:hover{\n"
"border-bottom: 2px solid rgb(0, 186, 45);\n"
"color:rgb(0, 186, 45);\n"
"}")
        self.Name.setObjectName("Name")
        self.password = QtWidgets.QLineEdit(self.widget1)
        self.password.setGeometry(QtCore.QRect(550, 600, 351, 71))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.password.setFont(font)
        self.password.setStyleSheet("QLineEdit#password{\n"
"font: 14pt \"Sitka\";\n"
"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom: 2px solid rgba(105, 118, 132, 255);\n"
"color:white;\n"
"padding-bottom: 7px;\n"
"}\n"
"QLineEdit#password:hover{\n"
"border-bottom: 2px solid rgb(0, 186, 45);\n"
"color:rgb(0, 186, 45);\n"
"}")
        self.password.setObjectName("password")
        self.login_button_2 = QtWidgets.QPushButton(self.widget1)
        self.login_button_2.setGeometry(QtCore.QRect(750, 700, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        self.login_button_2.setFont(font)
        self.login_button_2.setStyleSheet("QPushButton{\n"
"\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.488636, stop:0.357955 rgba(0, 208, 111, 255), stop:1 rgba(56, 236, 255, 255));\n"
"border:none;\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.488636, stop:0.471591 rgba(2, 0, 153, 255), stop:1 rgba(195, 0, 211, 255));\n"
"color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"\n"
"}QPushButton{\n"
"\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.488636, stop:0.357955 rgba(0, 208, 111, 255), stop:1 rgba(56, 236, 255, 255));\n"
"border:none;\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.488636, stop:0.471591 rgba(2, 0, 153, 255), stop:1 rgba(195, 0, 211, 255));\n"
"color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"\n"
"}")
        self.login_button_2.setObjectName("login_button_2")
        self.login_button_3 = QtWidgets.QPushButton(self.widget1)
        self.login_button_3.setGeometry(QtCore.QRect(590, 780, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        self.login_button_3.setFont(font)
        self.login_button_3.setStyleSheet("QPushButton{\n"
"\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.488636, stop:0.357955 rgba(0, 208, 111, 255), stop:1 rgba(56, 236, 255, 255));\n"
"border:none;\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.488636, stop:0.471591 rgba(2, 0, 153, 255), stop:1 rgba(195, 0, 211, 255));\n"
"color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"\n"
"}QPushButton{\n"
"\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.488636, stop:0.357955 rgba(0, 208, 111, 255), stop:1 rgba(56, 236, 255, 255));\n"
"border:none;\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.488636, stop:0.471591 rgba(2, 0, 153, 255), stop:1 rgba(195, 0, 211, 255));\n"
"color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"\n"
"}")
        self.login_button_3.setObjectName("login_button_3")
        self.Name_2 = QtWidgets.QLineEdit(self.widget1)
        self.Name_2.setGeometry(QtCore.QRect(550, 420, 351, 71))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.Name_2.setFont(font)
        self.Name_2.setStyleSheet("QLineEdit{\n"
"font: 14pt \"Sitka\";\n"
"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom: 2px solid rgba(105, 118, 132, 255);\n"
"color:white;\n"
"padding-bottom: 7px;\n"
"}\n"
"QLineEdit:hover{\n"
"border-bottom: 2px solid rgb(0, 186, 45);\n"
"color:rgb(0, 186, 45);\n"
"}")
        self.Name_2.setObjectName("Name_2")
        self.label.raise_()
        self.label_login.raise_()
        self.label_2.raise_()
        self.login_button.raise_()
        self.Name.raise_()
        self.password.raise_()
        self.login_button_2.raise_()
        self.login_button_3.raise_()
        self.Name_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1500, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.login_button.clicked.connect(self.ChekIN)
        self.login_button_2.clicked.connect(self.ChecKout)
        self.login_button_3.clicked.connect(self.Face_recognition)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login_button.setText(_translate("MainWindow", "Check in"))
        self.Name.setPlaceholderText(_translate("MainWindow", " Prenom :"))
        self.password.setPlaceholderText(_translate("MainWindow", " Password"))
        self.login_button_2.setText(_translate("MainWindow", "Check Out"))
        self.login_button_3.setText(_translate("MainWindow", ""))
        self.Name_2.setPlaceholderText(_translate("MainWindow", " Nom :"))

    def ChekIN(self):
        Nom=self.Name_2.text()
        Prenom=self.Name.text()
        password=self.password.text()

        employe=Employe.ChercherParNom(Nom,Prenom)
        if(password==employe[4]):
          print(employe[0])
          temps=SuiviTemps(employe[0])
          temps.Ajouter_checkin()
          msg = QMessageBox()
          msg.setWindowTitle("Emsi_Smart ")
          msg.setText("L'employé a été correctement ChekIN :)")
          msg.setIcon(QMessageBox.Warning)
          x = msg.exec_()
        else:
          msg = QMessageBox()
          msg.setWindowTitle("Emsi_Smart ")
          msg.setText("Password faux :)")
          msg.setIcon(QMessageBox.Critical)
          x = msg.exec_()    
        
    def ChecKout(self):
        Nom=self.Name_2.text()
        Prenom=self.Name.text()
        password=self.password.text()
        employe=Employe.ChercherParNom(Nom,Prenom)
        if(password==employe[4]):
          print(employe[0])
          temps=SuiviTemps(employe[0])
          temps.Ajouter_checkout()  
          msg = QMessageBox()
          msg.setWindowTitle("Emsi_Smart ")
          msg.setText("L'employé a été correctement ChekOut :)")
          msg.setIcon(QMessageBox.Warning)
          x = msg.exec_()
        else:
          msg = QMessageBox()
          msg.setWindowTitle("Emsi_Smart ")
          msg.setText("Password faux :)")
          msg.setIcon(QMessageBox.Critical)
          x = msg.exec_()    
        
    
    def Face_recognition(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog_face_recog()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
