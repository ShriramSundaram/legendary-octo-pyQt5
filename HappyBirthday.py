# -*- coding: utf-8 -*-
# Created using PyQt5 libraries
#
# Created by: "Shriram Sundaram"
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QMessageBox


class MyWindow(QMainWindow):
    def __init__(self):
        """
            Setting up the User Interface with Buttons, Images, Greetings, Date&Time and ComboBox
        """
        super(MyWindow, self).__init__()
        self.setObjectName("MainWindow")
        self.resize(1024, 718)
        self.setWindowTitle("Your Bday App")

        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setObjectName("central_widget")
        self.msg_pop_up = ""
        # Configure Image in Label
        self.bday_image = QtWidgets.QLabel(self.central_widget)
        self.bday_image.setGeometry(QtCore.QRect(290, 190, 311, 231))
        self.bday_image.setText("")
        self.bday_image.setPixmap(QtGui.QPixmap("Bday_Greetings.jpg"))
        self.bday_image.setScaledContents(True)
        self.bday_image.setObjectName("bday_image")

        self.calendar_widget = QtWidgets.QCalendarWidget(self.central_widget)
        self.calendar_widget.setGeometry(QtCore.QRect(10, 430, 392, 236))
        self.calendar_widget.setObjectName("calendar_widget")
        # Configure Date and Time
        self.date_time_edit = QtWidgets.QDateTimeEdit(self.central_widget)
        self.date_time_edit.setGeometry(QtCore.QRect(410, 610, 141, 41))
        self.date_time_edit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 10), QtCore.QTime(7, 20, 0)))
        self.date_time_edit.setObjectName("date_time_edit")
        # Configure Buttons
        self.image_for_you_button = QtWidgets.QPushButton(self.central_widget)
        self.image_for_you_button.setGeometry(QtCore.QRect(640, 610, 131, 41))
        self.image_for_you_button.setObjectName("image_for_you_button")

        self.about_you_button = QtWidgets.QPushButton(self.central_widget)
        self.about_you_button.setGeometry(QtCore.QRect(810, 610, 131, 41))
        self.about_you_button.setObjectName("about_you_button")

        self.wishes_button = QtWidgets.QPushButton(self.central_widget)
        self.wishes_button.setGeometry(QtCore.QRect(0, 40, 131, 41))
        self.wishes_button.setObjectName("wishes_button")

        self.reset_all_button = QtWidgets.QPushButton(self.central_widget)
        self.reset_all_button.setGeometry(QtCore.QRect(880, 10, 121, 61))
        self.reset_all_button.setObjectName("reset_all_button")

        self.submit_button = QtWidgets.QPushButton(self.central_widget)
        self.submit_button.setGeometry(QtCore.QRect(760, 320, 151, 51))
        self.submit_button.setObjectName("submit_button")
        # Configure Labels
        self.wishes_label = QtWidgets.QLabel(self.central_widget)
        self.wishes_label.setGeometry(QtCore.QRect(200, 20, 451, 101))
        self.wishes_label.setStyleSheet("font: 75 italic 32pt \"Sitka\";\n"
                                        "background-color: rgb(0, 255, 0);")
        self.wishes_label.setTextFormat(QtCore.Qt.PlainText)
        self.wishes_label.setWordWrap(False)
        self.wishes_label.setObjectName("wishes_label")

        self.about_you_label = QtWidgets.QLabel(self.central_widget)
        self.about_you_label.setGeometry(QtCore.QRect(410, 440, 521, 151))
        self.about_you_label.setObjectName("about_you_label")

        self.answer_label = QtWidgets.QLabel(self.central_widget)
        self.answer_label.setGeometry(QtCore.QRect(760, 270, 205, 41))
        self.answer_label.setObjectName("answer_label")

        self.family_game_label = QtWidgets.QLabel(self.central_widget)
        self.family_game_label.setGeometry(QtCore.QRect(790, 140, 81, 41))
        self.family_game_label.setObjectName("family_game_label")
        # Configure ComboBox
        self.comboBox = QtWidgets.QComboBox(self.central_widget)
        self.comboBox.setGeometry(QtCore.QRect(660, 190, 141, 41))
        self.comboBox.setObjectName("comboBox")
        for idx in range(4):
            self.comboBox.addItem("")

        self.comboBox_second = QtWidgets.QComboBox(self.central_widget)
        self.comboBox_second.setGeometry(QtCore.QRect(862, 191, 131, 41))
        self.comboBox_second.setObjectName("comboBox_second")
        for idx in range(4):
            self.comboBox_second.addItem("")

        self.setCentralWidget(self.central_widget)
        self.re_translate_ui()
        self.init_ui()

    def init_ui(self):
        self.wishes_label.setText("Every year it comes and Goes!!! ")
        self.wishes_label.adjustSize()

        self.image_for_you_button.clicked.connect(self.image_for_you)

        self.about_you_button.setText("About You")
        self.about_you_button.clicked.connect(self.about_you)

        self.wishes_button.setText("Wishes")
        self.wishes_button.clicked.connect(self.wishes)

        self.reset_all_button.clicked.connect(self.reset_all)
        self.submit_button.clicked.connect(self.game_logic)

        self.msg_pop_up = QMessageBox(self)
        self.msg_pop_up.setGeometry(200, 200, 400, 400)
        self.msg_pop_up.setWindowTitle("Popup Window!")

        self.msg_pop_up.setText("Welcome Birthday Baby!!!")
        self.msg_pop_up.setTextFormat(1000)

        self.msg_pop_up.exec()

    def wishes(self):
        self.wishes_label.setText("Happy Birthday Baby()!!!")
        self.wishes_label.adjustSize()

    def about_you(self):
        self.about_you_label.setText(
            "\n \n"
            "\n A Brief msg to her! ")
        self.about_you_label.adjustSize()

    def image_for_you(self):
        self.bday_image.setPixmap(QtGui.QPixmap("Bday_image.jpg"))
        self.bday_image.setScaledContents(True)

    def reset_all(self):
        self.bday_image.setPixmap(QtGui.QPixmap("Bday_Greetings.jpg"))
        self.bday_image.setScaledContents(True)
        self.wishes_label.setText("Every year it comes and Goes!!!")
        self.wishes_label.adjustSize()
        self.about_you_label.setText("For You")
        self.about_you_label.adjustSize()

    def game_logic(self):
        text1 = self.comboBox.currentText()
        text2 = self.comboBox_second.currentText()

        if (text1 == "YourGirlName") and (text2 == "YourGirlName"):
            self.answer_label.setText("Describe Her")
        elif ((text1 == "YourGirlName") and (text2 == "HerFatherName")) or (
                (text1 == "HerFatherName") and (text2 == "YourGirlName")):
            self.answer_label.setText("Combo : Describe the Combo")
        elif ((text1 == "YourGirlName") and (text2 == "HerMotherName")) or (
                (text1 == "HerMotherName") and (text2 == "YourGirlName")):
            self.answer_label.setText("Combo : Describe the Combo")
        elif ((text1 == "YourGirlName") and (text2 == "HerSisterName")) or (
                (text1 == "HerSisterName") and (text2 == "YourGirlName")):
            self.answer_label.setText("Combo : Describe the Combo!!!")
        elif ((text1 == "HerFatherName") and (text2 == "HerMotherName")) or (
                (text1 == "HerMotherName") and (text2 == "HerFatherName")):
            self.answer_label.setText("Combo: Describe the Combo")
        elif ((text1 == "HerSisterName") and (text2 == "HerMotherName")) or (
                (text1 == "HerMotherName") and (text2 == "HerSisterName")):
            self.answer_label.setText("Combo: Describe the Combo")
        elif ((text1 == "HerFatherName") and (text2 == "HerSisterName")) or (
                (text1 == "HerSisterName") and (text2 == "HerFatherName")):
            self.answer_label.setText("Combo: Describe the Combo")
        elif (text1 == "HerSisterName") and (text2 == "HerSisterName"):
            self.answer_label.setText("Describe Her")
        elif (text1 == "HerMotherName") and (text2 == "HerMotherName"):
            self.answer_label.setText("Describe Her!!!")
        elif (text1 == "HerFatherName") and (text2 == "HerFatherName"):
            self.answer_label.setText(" Describe Him!!!")
        else:
            self.answer_label.setText("Invalid Combo")

    def re_translate_ui(self):
        """

        :return: Setting up the Default name for Buttons and Labels
        """
        _translate = QtCore.QCoreApplication.translate
        self.image_for_you_button.setText(_translate("MainWindow", "Image For You"))
        self.about_you_button.setText(_translate("MainWindow", "AboutYou"))
        self.wishes_button.setText(_translate("MainWindow", "Wishes"))
        self.reset_all_button.setText(_translate("MainWindow", "Reset"))
        self.submit_button.setText(_translate("MainWindow", "Submit"))

        self.wishes_label.setText(_translate("MainWindow", "For You My Everthing"))
        self.about_you_label.setText(_translate("MainWindow", "For You"))
        self.answer_label.setText(_translate("MainWindow", "Answer"))

        self.comboBox.setItemText(0, _translate("MainWindow", "YourGirlName"))
        self.comboBox.setItemText(1, _translate("MainWindow", "HerSisterName"))
        self.comboBox.setItemText(2, _translate("MainWindow", "HerMotherName"))
        self.comboBox.setItemText(3, _translate("MainWindow", "HerFatherName"))

        self.comboBox_second.setItemText(0, _translate("MainWindow", "HerFatherName"))
        self.comboBox_second.setItemText(1, _translate("MainWindow", "YourGirlName"))
        self.comboBox_second.setItemText(2, _translate("MainWindow", "HerSisterName"))
        self.comboBox_second.setItemText(3, _translate("MainWindow", "HerMotherName"))

        self.family_game_label.setText(_translate("MainWindow", "Family Game"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myUi = MyWindow()
    myUi.show()
    sys.exit(app.exec_())
