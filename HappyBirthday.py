# -*- coding: utf-8 -*-
# Created using PyQt5 libraries
#
# Created by: Shriram Sundaram
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PyQt5.QtGui import QPixmap


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setObjectName("MainWindow")
        self.resize(1024, 718)
        self.setWindowTitle("Our App KS")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.Image1 = QtWidgets.QLabel(self.centralwidget)
        self.Image1.setGeometry(QtCore.QRect(290, 190, 311, 231))
        self.Image1.setText("")
        self.Image1.setPixmap(QtGui.QPixmap("Bday_Greetings.PNG"))
        self.Image1.setScaledContents(True)
        self.Image1.setObjectName("Image1")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 430, 392, 236))
        self.calendarWidget.setObjectName("calendarWidget")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(410, 610, 141, 41))
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 10), QtCore.QTime(7, 20, 0)))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(640, 610, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(810, 610, 131, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 40, 131, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(880, 10, 121, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 20, 451, 101))
        self.label_2.setStyleSheet("font: 75 italic 32pt \"Sitka\";\n"
                                   "background-color: rgb(0, 255, 0);")
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(410, 440, 521, 151))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(660, 190, 141, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(862, 191, 131, 41))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(760, 270, 205, 41))
        self.label_3.setObjectName("label_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(760, 320, 151, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(810, 190, 51, 61))
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(790, 140, 81, 41))
        self.label_4.setObjectName("label_4")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(self)
        self.actionNew.setObjectName("actionNew")
        self.actionSave_Ctrl_S = QtWidgets.QAction(self)
        self.actionSave_Ctrl_S.setObjectName("actionSave_Ctrl_S")
        self.actionSave_as = QtWidgets.QAction(self)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionKeerthanApp1_0 = QtWidgets.QAction(self)
        self.actionKeerthanApp1_0.setObjectName("actionKeerthanApp1_0")
        self.action2020 = QtWidgets.QAction(self)
        self.action2020.setObjectName("action2020")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave_Ctrl_S)
        self.menuFile.addAction(self.actionSave_as)
        self.menuAbout.addAction(self.actionKeerthanApp1_0)
        self.menuAbout.addAction(self.action2020)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.retranslateUi()
        self.initUI()

    def initUI(self):
        self.label_2.setText("Every year it comes and Goes!!! ")
        self.label_2.adjustSize()

        self.pushButton.clicked.connect(self.imageForYou)

        self.pushButton_2.setText("About You")
        self.pushButton_2.clicked.connect(self.aboutYou)

        self.pushButton_3.setText("Wishes")
        self.pushButton_3.clicked.connect(self.wishes)

        self.pushButton_4.clicked.connect(self.resetAll)
        self.pushButton_5.clicked.connect(self.gameLogic)

        self.ourMsgbox = QMessageBox(self)
        self.ourMsgbox.setGeometry(200, 200, 400, 400)
        self.ourMsgbox.setWindowTitle("Popup Window!")
        self.ourMsgbox.setText("Welcome Birthday Baby!!!")
        self.ourMsgbox.setTextFormat(1000)

        x = self.ourMsgbox.exec()

    def wishes(self):
        self.label_2.setText("Happy Birthday Baby()!!!")
        self.label_2.adjustSize()

    def aboutYou(self):
        self.label.setText(
            "\n \n A kind, lovely and precisely more mature women. you always accompany your well wishers \n"
            "with your full support!!! You have a been expressing your gratitude to your friends and \n"
            "family!!! You have clearly Understood that focus is the key towards your success \n"
            "You have faced numerous hurdles and hardens  in your life, with all those tough lessons- \"\n"
            "You are ready to march into your new life!!! - You knew how life algorithm works:) \n"
            "\n Keerthana - Thrive to Succeed ")
        self.label.adjustSize()

    def imageForYou(self):
        self.Image1.setPixmap(QtGui.QPixmap("Keerz2.PNG"))
        self.Image1.setScaledContents(True)

    def resetAll(self):
        self.Image1.setPixmap(QtGui.QPixmap("Bday_Greetings.PNG"))
        self.Image1.setScaledContents(True)
        self.label_2.setText("Every year it comes and Goes!!!" )
        self.label_2.adjustSize()
        self.label.setText("For You")
        self.label.adjustSize()

    def gameLogic(self):
        text1 = self.comboBox.currentText()
        text2 = self.comboBox_2.currentText()

        if (text1 == "Keerthana") and (text2 == "Keerthana"):
            self.label_3.setText("Nanum Rowdy Tan")
        elif ((text1 == "Keerthana") and (text2 == "Shuresh")) or ((text1 == "Shuresh") and (text2 == "Keerthana")):
            self.label_3.setText("Combo : Deiva Thirumagal")
        elif ((text1 == "Keerthana") and (text2 == "Pushpalatha")) or (
                (text1 == "Pushpalatha") and (text2 == "Keerthana")):
            self.label_3.setText("Combo : SandaKozhi")
        elif ((text1 == "Keerthana") and (text2 == "Niranchanna")) or (
                (text1 == "Niranchanna") and (text2 == "Keerthana")):
            self.label_3.setText("Combo : Paasa Paravaigal!!!")
        elif ((text1 == "Shuresh") and (text2 == "Pushpalatha")) or ((text1 == "Pushpalatha") and (text2 == "Shuresh")):
            self.label_3.setText("Combo:Samsaram Athu Minsaaram")
        elif ((text1 == "Niranchanna") and (text2 == "Pushpalatha")) or (
                (text1 == "Pushpalatha") and (text2 == "Niranchanna")):
            self.label_3.setText("Combo: Mayakannadi")
        elif ((text1 == "Shuresh") and (text2 == "Niranchanna")) or ((text1 == "Niranchanna") and (text2 == "Shuresh")):
            self.label_3.setText("Combo: Kadaikutti Singam")
        elif (text1 == "Niranchanna") and (text2 == "Niranchanna"):
            self.label_3.setText("Yaara Di Nee Mozhini")
        elif (text1 == "Pushpalatha") and (text2 == "Pushpalatha"):
            self.label_3.setText("Ratha Sarithiram!!!")
        elif (text1 == "Shuresh") and (text2 == "Shuresh"):
            self.label_3.setText("Anbe Shivam (Shiva Shiva)!!!")
        else:
            self.label_3.setText("Invalid Combo")

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("MainWindow", "imageForYou"))
        self.pushButton_2.setText(_translate("MainWindow", "AboutYou"))
        self.pushButton_3.setText(_translate("MainWindow", "Wishes"))
        self.pushButton_4.setText(_translate("MainWindow", "Reset"))
        self.label_2.setText(_translate("MainWindow", "For You My Everthing"))
        self.label.setText(_translate("MainWindow", "For You"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Keerthana"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Niranchanna"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Pushpalatha"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Shuresh"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Shuresh"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Keerthana"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Niranchanna"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Pushpalatha"))
        self.label_3.setText(_translate("MainWindow", "Answer"))
        self.pushButton_5.setText(_translate("MainWindow", "Submit"))
        self.textEdit.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">+</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Family Game"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit "))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionSave_Ctrl_S.setText(_translate("MainWindow", "Save Ctrl + S"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionKeerthanApp1_0.setText(_translate("MainWindow", "KeerthanApp1.0"))
        self.action2020.setText(_translate("MainWindow", "2020"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myUi = MyWindow()
    myUi.show()
    sys.exit(app.exec_())
