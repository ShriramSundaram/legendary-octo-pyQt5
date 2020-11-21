"""
Python Login System

Created by Shriram Sundaram , Jan 2020

Basic Login Panel using PyQt5
"""

from PyQt5.QtWidgets import QMainWindow


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
        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setObjectName("central_widget")
        # username label
        self.username_label = QtWidgets.QLabel(self.central_widget)
        self.username_label.setGeometry(QtCore.QRect(70, 90, 101, 31))
        self.username_label.setStyleSheet("font: 18pt \"Microsoft Himalaya\";")
        self.username_label.setObjectName("username_label")
        # password label
        self.password_label = QtWidgets.QLabel(self.central_widget)
        self.password_label.setGeometry(QtCore.QRect(70, 160, 101, 21))
        self.password_label.setStyleSheet("font: 18pt \"Microsoft Himalaya\";")
        self.password_label.setObjectName("password_label")
        # title label
        self.title_label = QtWidgets.QLabel(self.central_widget)
        self.title_label.setGeometry(QtCore.QRect(200, 0, 211, 41))
        self.title_label.setStyleSheet("font: 20pt \"Modern No. 20\";")
        self.title_label.setObjectName("title_label")
        # log label
        self.log_label = QtWidgets.QLabel(self.central_widget)
        self.log_label.setGeometry(QtCore.QRect(40, 300, 301, 21))
        self.log_label.setObjectName("log_label")
        # signup label
        self.signup_label = QtWidgets.QLabel(self.central_widget)
        self.signup_label.setGeometry(QtCore.QRect(330, 60, 81, 21))
        self.signup_label.setStyleSheet("font: 18pt \"Microsoft Himalaya\";")
        self.signup_label.setObjectName("signup_label")
        # new username label
        self.new_username_label = QtWidgets.QLabel(self.central_widget)
        self.new_username_label.setGeometry(QtCore.QRect(330, 90, 131, 31))
        self.new_username_label.setStyleSheet("font: 18pt \"Microsoft Himalaya\";")
        self.new_username_label.setObjectName("new_username_label")
        # new password label
        self.new_password_label = QtWidgets.QLabel(self.central_widget)
        self.new_password_label.setGeometry(QtCore.QRect(330, 160, 131, 21))
        self.new_password_label.setStyleSheet("font: 18pt \"Microsoft Himalaya\";")
        self.new_password_label.setObjectName("new_password_label")
        # confirm password label
        self.confirm_password_label = QtWidgets.QLabel(self.central_widget)
        self.confirm_password_label.setGeometry(QtCore.QRect(330, 230, 161, 21))
        self.confirm_password_label.setStyleSheet("font: 18pt \"Microsoft Himalaya\";")
        self.confirm_password_label.setObjectName("confirm_password_label")
        # login label
        self.login_label = QtWidgets.QLabel(self.central_widget)
        self.login_label.setGeometry(QtCore.QRect(70, 60, 81, 21))
        self.login_label.setStyleSheet("font: 18pt \"Microsoft Himalaya\";")
        self.login_label.setObjectName("login_label")
        # signup button
        self.signup_button = QtWidgets.QPushButton(self.central_widget)
        self.signup_button.setGeometry(QtCore.QRect(340, 310, 111, 41))
        self.signup_button.setObjectName("signup_button")
        # login button
        self.login_button = QtWidgets.QPushButton(self.central_widget)
        self.login_button.setGeometry(QtCore.QRect(80, 240, 111, 41))
        self.login_button.setObjectName("login_button")
        # line 
        self.lineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 120, 151, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.central_widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 190, 151, 22))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.central_widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(330, 120, 151, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.central_widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(330, 190, 151, 22))
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.central_widget)
        self.lineEdit_5.setGeometry(QtCore.QRect(330, 260, 151, 22))
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 543, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.UserName = ""
        self.Password = ""

        self.re_translate_ui()
        self.init_login()

    def re_translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.username_label.setText(_translate("MainWindow", "Username"))
        self.password_label.setText(_translate("MainWindow", "Password"))
        self.title_label.setText(_translate("MainWindow", "Login System"))
        self.log_label.setText(_translate("MainWindow", "Log:"))
        self.signup_label.setText(_translate("MainWindow", "SignUp"))
        self.new_username_label.setText(_translate("MainWindow", "New Username"))
        self.new_password_label.setText(_translate("MainWindow", "New Password"))
        self.signup_button.setText(_translate("MainWindow", "SignUp"))
        self.confirm_password_label.setText(_translate("MainWindow", "Confirm Password"))
        self.login_label.setText(_translate("MainWindow", "Login"))
        self.login_button.setText(_translate("MainWindow", "Login"))

    def init_login(self):
        self.login_button.setText("Login")
        self.login_button.clicked.connect(self.inputs_from_user)
        self.signup_button.clicked.connect(self.sign_up)

    def inputs_from_user(self):
        if self.UserName is not None:
            self.UserName = str(self.lineEdit.text())
            self.Password = str(self.lineEdit_2.text())
            self.refresh_database()
            self.open_source()

    def open_source(self):
        """Open the source file and save it in the format"""
        self.new_input_formatted_username = str("Username =" + " " + self.UserName)
        self.new_input_formatted_password = str("Password =" + " " + self.Password)
        self.check_database()

    def check_database(self):
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
                self.log_label.setText("Successfully Logged in")
                self.reset_login()
            else:
                self.log_label.setText("Username and Password is incorrect")
                self.reset_login()
        else:
            self.log_label.setText("The system couldn't find the User, "
                                   "Please signup")
            self.log_label.adjustSize()
            self.reset_login()

    def sign_up(self):
        """
        Sign Up Logic

        """
        if self.lineEdit_3 is not None:
            self.New_UserName = str(str("Username = ") + str(self.lineEdit_3.text()))
            # print(self.New_UserName)
        if self.lineEdit_4 is not None:
            self.New_Password = str(str("Password = ") + str(self.lineEdit_4.text()))
            # print(self.New_Password)
        if self.lineEdit_5 is not None:
            self.Confirm_Password = str(str("Password = ") + self.lineEdit_5.text())

        if self.New_Password == self.Confirm_Password:
            if self.New_UserName + "\n" in self.already_saved:
                self.log_label.setText("The Username already exist!!!")
                self.reset_signup()
            else:
                self.log_label.setText("Sign Up Successful")
                New_Login = open("LoginInfo", 'a')
                New_UserName = str(self.New_UserName)
                New_Password = str(self.New_Password)

                New_UsersList = [New_UserName, New_Password]
                for users in New_UsersList:
                    New_Login.writelines(users)
                    New_Login.writelines("\n")
                New_Login.close()
                self.reset_signup()
        else:
            self.log_label.setText("New Password and Confirm Password doesnt Match")
            self.reset_signup()

    def reset_signup(self):
        self.lineEdit_3.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_4.setText("")

    def reset_login(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")

    def refresh_database(self):
        file = open("LoginInfo")
        self.already_saved = file.readlines()
        file.close()


if __name__ == "__main__":
    import sys
    from PyQt5 import QtWidgets, QtCore

    app = QtWidgets.QApplication(sys.argv)
    Login = MyLoginWindow()
    Login.show()
    sys.exit(app.exec_())
