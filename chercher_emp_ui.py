# Form implementation generated from reading ui file 'c:\Users\Hp\Desktop\projet-pfa-2\chercher_emp.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1191, 670)
        Dialog.setStyleSheet("background-color:#CDBEFF;")
        self.label_5 = QtWidgets.QLabel(parent=Dialog)
        self.label_5.setGeometry(QtCore.QRect(780, 40, 381, 611))
        self.label_5.setStyleSheet("\n"
"border: 2px solid rgba(0, 0, 0, 255);\n"
"border-radius: 30px;\n"
"background-color:#332562;\n"
"")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(parent=Dialog)
        self.label_7.setGeometry(QtCore.QRect(920, 50, 201, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(-1)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:90px")
        self.label_7.setObjectName("label_7")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(790, 160, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:20px;\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(790, 240, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:20px;\n"
"")
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(parent=Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 751, 431))
        self.tableWidget.setStyleSheet("\n"
"border: 2px solid rgba(0, 0, 0, 255);\n"
"border-radius: 30px;\n"
"background-color:#FFFFFF;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(182)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(36)
        self.label_6 = QtWidgets.QLabel(parent=Dialog)
        self.label_6.setGeometry(QtCore.QRect(110, 450, 341, 211))
        self.label_6.setStyleSheet("\n"
"border: 2px solid rgba(0, 0, 0, 255);\n"
"border-radius: 30px;\n"
"background-color:#332562;\n"
"")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(120, 490, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:16px;\n"
"")
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 490, 261, 31))
        self.lineEdit_3.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:20px;\n"
"border:none;\n"
"border-bottom: 2px solid #FFFFFF;")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_8 = QtWidgets.QLabel(parent=Dialog)
        self.label_8.setGeometry(QtCore.QRect(120, 550, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:16px;\n"
"")
        self.label_8.setObjectName("label_8")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 550, 241, 31))
        self.lineEdit_4.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:20px;\n"
"border:none;\n"
"border-bottom: 2px solid #FFFFFF;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(230, 610, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(-1)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border: 2px solid #FFFFFF;\n"
"border-radius: 10px;\n"
"background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:20px")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(800, 190, 331, 41))
        self.label.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:20px;\n"
"border:none;\n"
"border-bottom: 2px solid #FFFFFF;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_9 = QtWidgets.QLabel(parent=Dialog)
        self.label_9.setGeometry(QtCore.QRect(800, 270, 331, 41))
        self.label_9.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:20px;\n"
"border:none;\n"
"border-bottom: 2px solid #FFFFFF;")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=Dialog)
        self.label_10.setGeometry(QtCore.QRect(800, 320, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:20px;\n"
"")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=Dialog)
        self.label_11.setGeometry(QtCore.QRect(800, 350, 331, 41))
        self.label_11.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:20px;\n"
"border:none;\n"
"border-bottom: 2px solid #FFFFFF;")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=Dialog)
        self.label_12.setGeometry(QtCore.QRect(800, 400, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:20px;\n"
"")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(parent=Dialog)
        self.label_13.setGeometry(QtCore.QRect(800, 430, 331, 41))
        self.label_13.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:20px;\n"
"border:none;\n"
"border-bottom: 2px solid #FFFFFF;")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(parent=Dialog)
        self.label_14.setGeometry(QtCore.QRect(800, 480, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:20px;\n"
"")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(parent=Dialog)
        self.label_15.setGeometry(QtCore.QRect(800, 520, 331, 41))
        self.label_15.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:20px;\n"
"border:none;\n"
"border-bottom: 2px solid #FFFFFF;")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_7.setText(_translate("Dialog", ""))
        self.label_2.setText(_translate("Dialog", "Nom :"))
        self.label_3.setText(_translate("Dialog", "Prenom :"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "#"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Date Arrivee"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Date Départ"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Periode"))
        self.label_4.setText(_translate("Dialog", "Nom :"))
        self.label_8.setText(_translate("Dialog", "Prenom :"))
        self.pushButton.setText(_translate("Dialog", ""))
        self.label_10.setText(_translate("Dialog", "Email :"))
        self.label_12.setText(_translate("Dialog", "Password :"))
        self.label_14.setText(_translate("Dialog", "Tache :"))
