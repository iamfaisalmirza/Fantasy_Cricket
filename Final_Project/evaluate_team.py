# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluate_team.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from team_score import Ui_TeamScore
import sqlite3
conn = sqlite3.connect('cricket.db')
cur = conn.cursor()


class Ui_EvalTeam(object):

    def __init__(self):
        super().__init__()
        self.totalScore = 0
        self.teamPoints = 0

    def points(self):
        s = []
        for i in range(self.listEvaluatePlayers.count()):
            s.append(self.listEvaluatePlayers.item(i).text())
        for t in s:
            cur.execute("select Value from stats where Player='"+t+"';")
            rs = cur.fetchone()
            self.teamPoints += int(rs[0])

    def player_score(self, team):
        self.listEvaluatePlayers.clear()
        self.listEvaluatePoints.clear()
        self.score = []
        self.player = []
        name = str(team).replace("'", "!")
        cur.execute("select Players from teams where Name='"+name+"';")
        result = cur.fetchall()
        conn.commit()
        for t in result:
            self.player.append(str(t[0]))
        # print(self.player)
        for i in self.player:
            pscore = 0
            cur.execute("select * from match where Player='"+i+"';")
            rs = cur.fetchone()
            try:
                pscore = rs[1]//2  # runs/2
                # print(pscore)
            except:
                pscore = 0
            if int (rs[1]) >= 50:
                pscore += 5 # 5 points for half century
            if rs[1] >= 100:
                pscore += 10  # 10 points for century
            try:
                if 80 <= (rs[1] / rs[2])*100 <= 100:
                    pscore += 2
                if (rs[1] / rs[2])*100 > 100:
                    pscore += 4
            except:
                pscore += 0
            pscore += (rs[3] + rs[4]*2)
            pscore += rs[8]*10
            if rs[8] >= 3:
                pscore += 5
                if rs[8] >= 5:
                    pscore += 10
            try:
                if 3.5 < rs[7]/(rs[5]/6) <= 4.5:
                    pscore += 4
                if 2 <= rs[7]/(rs[5]/6) <= 3.5:
                    pscore += 7
                if rs[7]/(rs[5]/6) < 2:
                    pscore += 10
            except:
                pscore += 0
            pscore += 10*(rs[9] + rs[10] + rs[11])
            self.score.append(pscore)
        for i in range(len(self.player)):
            # print(self.player[i])
            self.listEvaluatePlayers.addItem(self.player[i])
            self.listEvaluatePoints.addItem(str(self.score[i]))
        self.points()

    def teamScore(self):
        self.windowScore = QtWidgets.QDialog()
        self.uiScore = Ui_TeamScore()
        self.uiScore.setupUi(self.windowScore)
        self.calScore()
        self.uiScore.labelTeamScore.setText(str(self.totalScore))
        self.windowScore.show()

    def calScore(self):
        self.totalScore = 0
        for i in self.score:
            self.totalScore += int(i)

    def evaladd(self):
        cur.execute("select distinct Name from teams;")
        result = cur.fetchall()
        for t in result:
            self.comboEvaluateTeam.addItem(t[0].replace("!", "'"))

    def setupUi(self, EvalTeam):
        EvalTeam.setObjectName("EvalTeam")
        EvalTeam.resize(480, 500)
        EvalTeam.setStyleSheet("QDialog{\n"
                               "background-color:rgb(190, 190, 190)\n"
                               "}\n"
                               "QComboBox{\n"
                               "background-color:rgb(255, 255, 255)\n"
                               "}")
        self.label = QtWidgets.QLabel(EvalTeam)
        self.label.setGeometry(QtCore.QRect(1, 20, 471, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(EvalTeam)
        self.label_3.setGeometry(QtCore.QRect(280, 100, 39, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(EvalTeam)
        self.horizontalLayoutWidget_2.setGeometry(
            QtCore.QRect(9, 129, 462, 327))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listEvaluatePlayers = QtWidgets.QListWidget(
            self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setPointSize(10)
        self.listEvaluatePlayers.setFont(font)
        self.listEvaluatePlayers.setStyleSheet("color : #0d6ba6")
        self.listEvaluatePlayers.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOn)
        self.listEvaluatePlayers.setObjectName("listEvaluatePlayers")
        self.horizontalLayout_2.addWidget(self.listEvaluatePlayers)
        spacerItem = QtWidgets.QSpacerItem(
            10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.listEvaluatePoints = QtWidgets.QListWidget(
            self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setPointSize(10)
        self.listEvaluatePoints.setFont(font)
        self.listEvaluatePoints.setStyleSheet("color : #0d6ba6")
        self.listEvaluatePoints.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOn)
        self.listEvaluatePoints.setObjectName("listEvaluatePoints")
        self.horizontalLayout_2.addWidget(self.listEvaluatePoints)
        self.horizontalLayoutWidget = QtWidgets.QWidget(EvalTeam)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(38, 50, 401, 24))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.comboEvaluateTeam = QtWidgets.QComboBox(
            self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboEvaluateTeam.setFont(font)
        self.comboEvaluateTeam.currentTextChanged.connect(self.player_score)
        self.comboEvaluateTeam.setObjectName("comboEvaluateTeam")
        self.comboEvaluateTeam.addItem("")
        self.horizontalLayout.addWidget(self.comboEvaluateTeam)

        self.comboEvaluateMatch = QtWidgets.QComboBox(
            self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboEvaluateMatch.setFont(font)
        self.comboEvaluateMatch.setObjectName("comboEvaluateMatch")
        self.comboEvaluateMatch.addItem("")
        self.comboEvaluateMatch.addItem("Match1")
        self.horizontalLayout.addWidget(self.comboEvaluateMatch)
        self.line = QtWidgets.QFrame(EvalTeam)
        self.line.setGeometry(QtCore.QRect(10, 80, 462, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(EvalTeam)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 47, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.btnCalculateScore = QtWidgets.QPushButton(EvalTeam)
        self.btnCalculateScore.setGeometry(QtCore.QRect(170, 462, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnCalculateScore.setFont(font)
        self.btnCalculateScore.clicked.connect(self.teamScore)
        self.btnCalculateScore.setObjectName("btnCalculateScore")

        self.retranslateUi(EvalTeam)
        QtCore.QMetaObject.connectSlotsByName(EvalTeam)

    def retranslateUi(self, EvalTeam):
        _translate = QtCore.QCoreApplication.translate
        EvalTeam.setWindowTitle(_translate("EvalTeam", "Evaluate Team"))
        self.label.setText(_translate(
            "EvalTeam", "Evaluate the Performance of your Fantasy Team"))
        self.label_3.setText(_translate("EvalTeam", "Points"))
        self.comboEvaluateMatch.setItemText(
            0, _translate("EvalTeam", "Select Match"))
        self.comboEvaluateTeam.setItemText(
            0, _translate("EvalTeam", "Select Team"))
        self.label_4.setText(_translate("EvalTeam", "Players"))
        self.btnCalculateScore.setText(
            _translate("EvalTeam", "Calculate Score"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EvalTeam = QtWidgets.QDialog()
    ui = Ui_EvalTeam()
    ui.setupUi(EvalTeam)
    EvalTeam.show()
    sys.exit(app.exec_())