# Form implementation generated from reading ui file 'c:\Users\Hp\Desktop\projet-pfa-2\afficherEmploye.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Afficher_employe(object):
    def setupUi(self, Afficher_employe):
        Afficher_employe.setObjectName("Afficher_employe")
        Afficher_employe.resize(1285, 571)
        Afficher_employe.setStyleSheet("background-color: #bbff00; \n"
"")
        self.tableWidget = QtWidgets.QTableWidget(parent=Afficher_employe)
        self.tableWidget.setGeometry(QtCore.QRect(80, 60, 1011, 461))
        self.tableWidget.setMaximumSize(QtCore.QSize(1011, 461))
        self.tableWidget.setStyleSheet("background-color: #ffffff; /* Fully opaque */\n"
"border: 2px solid black;\n"
"  border-radius: 5px;")
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.tableWidget.setAutoScrollMargin(15)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
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
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)

        self.retranslateUi(Afficher_employe)
        QtCore.QMetaObject.connectSlotsByName(Afficher_employe)

    def retranslateUi(self, Afficher_employe):
        _translate = QtCore.QCoreApplication.translate
        Afficher_employe.setWindowTitle(_translate("Afficher_employe", "Dialog"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Afficher_employe", "#"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Afficher_employe", "NOM"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Afficher_employe", "Prenom"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Afficher_employe", "Email"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Afficher_employe", "Phone"))
