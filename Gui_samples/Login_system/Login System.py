"""
Python Login System

"""
import sys

from PyQt5.QtWidgets import QMainWindow
from PyQt5 import Qt


class MyLoginWindow(QMainWindow):

    def __init__(self):
        self.username_info = ""
        self.password_info = ""
        self.new_input_formatted_username = ""
        self.new_input_formatted_password = ""
        self.New_UserName = ""
        self.New_Password = ""
        self.Confirm_Password = ""
        file = open("LoginInfo")
        self.already_saved = file.readlines()
        file.close()

        super(MyLoginWindow, self).__init__()
        self.setObjectName("MainWindow")
        self.resize(543, 453)
        self.setWindowTitle("Welcome To Login Panel")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 90, 101, 31))
        self.label_2.setStyleSheet("font: 18pt \"Microsoft Himalaya\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 160, 101, 21))
        self.label_3.setStyleSheet("font: 18pt \"Microsoft Himalaya\";")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 240, 111, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(200, 0, 211, 41))
        self.label_5.setStyleSheet("font: 20pt \"Modern No. 20\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 300, 301, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(330, 60, 81, 21))
        self.label_7.setStyleSheet("font: 18pt \"Microsoft Himalaya\";")
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(330, 90, 131, 31))
        self.label_9.setStyleSheet("font: 18pt \"Microsoft Himalaya\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(330, 160, 131, 21))
        self.label_10.setStyleSheet("font: 18pt \"Microsoft Himalaya\";")
        self.label_10.setObjectName("label_10")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 310, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(330, 230, 161, 21))
        self.label_12.setStyleSheet("font: 18pt \"Microsoft Himalaya\";")
        self.label_12.setObjectName("label_12")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 120, 151, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 190, 151, 22))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(330, 120, 151, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(330, 190, 151, 22))
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(330, 260, 151, 22))
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(70, 60, 81, 21))
        self.label_8.setStyleSheet("font: 18pt \"Microsoft Himalaya\";")
        self.label_8.setObjectName("label_8")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 543, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.UserName = ""
        self.Password = ""

        self.retranslateUi()
        self.initLogin()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.label_5.setText(_translate("MainWindow", "Login System"))
        self.label_6.setText(_translate("MainWindow", "Log:"))
        self.label_7.setText(_translate("MainWindow", "SignUp"))
        self.label_9.setText(_translate("MainWindow", "New Username"))
        self.label_10.setText(_translate("MainWindow", "New Password"))
        self.pushButton.setText(_translate("MainWindow", "SignUp"))
        self.label_12.setText(_translate("MainWindow", "Confirm Password"))
        self.label_8.setText(_translate("MainWindow", "Login"))
        self.pushButton_2.setText(_translate("MainWindow", "Login"))

    def initLogin(self):
        self.pushButton_2.setText("Login")
        self.pushButton_2.clicked.connect(self.inputsFromUser)
        self.pushButton.clicked.connect(self.signUp)

    def inputsFromUser(self):
        if self.UserName is not None:
            self.UserName = str(self.lineEdit.text())
            self.Password = str(self.lineEdit_2.text())
            self.openSource()

    def openSource(self):
        """Open the source file and save it in the format"""
        self.new_input_formatted_username = str("Username =" + " " + self.UserName)
        self.new_input_formatted_password = str("Password =" + " " + self.Password)
        self.checkDatabase()

    def checkDatabase(self):
        """
        Verifying with the source code or Database

        """
        for i, users in enumerate(self.already_saved):
            if self.new_input_formatted_username == str(self.already_saved[i].rstrip("\n")):
                self.username_info = str(self.already_saved[i].rstrip("\n"))
            if self.new_input_formatted_password == str(self.already_saved[i]).rstrip("\n"):
                self.password_info = str(self.already_saved[i]).rstrip("\n")

        if self.new_input_formatted_username == self.username_info.rstrip("\n"):
            if self.new_input_formatted_password == self.password_info.rstrip("\n"):
                self.label_6.setText("Successfully Logged in")
            else:
                self.label_6.setText("Username and Password is incorrect")
        else:
            self.label_6.setText("The system couldn't find the Username, Please sign up")

    def signUp(self):
        """
        Sign Up Logic

        """
        if self.lineEdit_3 is not None:
            self.New_UserName = str(str("Username = ") + str(self.lineEdit_3.text()))
            #print(self.New_UserName)
        if self.lineEdit_4 is not None:
            self.New_Password = str(str("Password = ") + str(self.lineEdit_4.text()))
            # print(self.New_Password)
        if self.lineEdit_5 is not None:
            self.Confirm_Password = str(str("Password = ") + self.lineEdit_5.text())

        if self.New_Password == self.Confirm_Password:
            if self.New_UserName + "\n" in self.already_saved:
                self.label_6.setText("The Username already exist!!!")
            else:
                self.label_6.setText("Sign Up Successful")
                New_Login = open("LoginInfo", 'a')
                New_UserName = str(self.New_UserName)
                New_Password = str(self.New_Password)

                New_UsersList = [New_UserName, New_Password]
                for users in New_UsersList:
                    New_Login.writelines(users)
                    New_Login.writelines("\n")
                New_Login.close()
        else:
            self.label_6.setText("New Password and Confirm Password doesnt Match")


if __name__ == "__main__":
    import sys
    from PyQt5 import QtGui, QtWidgets, QtCore

    app = QtWidgets.QApplication(sys.argv)
    Login = MyLoginWindow()
    Login.show()
    sys.exit(app.exec_())
