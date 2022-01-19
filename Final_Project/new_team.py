# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_team.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

#from main_game import Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QMessageBox
import sqlite3
conn = sqlite3.connect('cricket.db')
cur = conn.cursor()


class Ui_NewTeam(object):

    def validName(self):
        cur.execute("select distinct Name from teams;")
        result = cur.fetchall()
        for i in result:
            if self.editNewTeam.text() == i[0].replace("!", "'"):
                print("Name is already in use.")
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Warning!!!")
                msg.setText("Team name is already in use.")
                msg.exec()
                self.editNewTeam.setText("")

    def setupUi(self, NewTeam):
        NewTeam.setObjectName("NewTeam")
        NewTeam.resize(320, 240)
        NewTeam.setStyleSheet("QDialog{\n"
                              "background-color:rgb(180, 180, 180)\n"
                              "}")
        self.verticalLayout = QtWidgets.QVBoxLayout(NewTeam)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(NewTeam)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.editNewTeam = QtWidgets.QLineEdit(NewTeam)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.editNewTeam.setFont(font)
        self.editNewTeam.setText("")
        self.editNewTeam.setObjectName("editNewTeam")
        self.verticalLayout.addWidget(self.editNewTeam)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.btnNewTeam = QtWidgets.QPushButton(NewTeam)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnNewTeam.setFont(font)
        self.btnNewTeam.clicked.connect(self.validName)
        self.btnNewTeam.setObjectName("btnNewTeam")
        self.verticalLayout.addWidget(self.btnNewTeam)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)

        self.retranslateUi(NewTeam)
        QtCore.QMetaObject.connectSlotsByName(NewTeam)

    def retranslateUi(self, NewTeam):
        _translate = QtCore.QCoreApplication.translate
        NewTeam.setWindowTitle(_translate("NewTeam", "New Team"))
        self.label.setText(_translate("NewTeam", "Create New Team"))
        self.editNewTeam.setPlaceholderText(
            _translate("NewTeam", "Enter new team name"))
        self.btnNewTeam.setText(_translate("NewTeam", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewTeam = QtWidgets.QDialog()
    ui = Ui_NewTeam()
    ui.setupUi(NewTeam)
    NewTeam.show()
    sys.exit(app.exec_())
