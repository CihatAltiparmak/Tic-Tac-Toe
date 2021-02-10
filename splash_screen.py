# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SplashScreen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QProgressBar

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.shadowFrame = QtWidgets.QFrame(self.centralwidget)
        self.shadowFrame.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.shadowFrame.setStyleSheet("QFrame {\n"
"    background-color: rgb(56,58,89);\n"
"    color: rgb(220,220,220);\n"
"    border-radius: 10px;\n"
"}")
        self.shadowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.shadowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.shadowFrame.setObjectName("shadowFrame")
        self.main_lbl = QtWidgets.QLabel(self.shadowFrame)
        self.main_lbl.setGeometry(QtCore.QRect(0, 140, 791, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        self.main_lbl.setFont(font)
        self.main_lbl.setStyleSheet("QLabel {color: rgb(254, 121, 199)}")
        self.main_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.main_lbl.setWordWrap(False)
        self.main_lbl.setObjectName("main_lbl")
        self.enjoyurgame_lbl = QtWidgets.QLabel(self.shadowFrame)
        self.enjoyurgame_lbl.setGeometry(QtCore.QRect(0, 210, 791, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.enjoyurgame_lbl.setFont(font)
        self.enjoyurgame_lbl.setStyleSheet("QLabel {color: rgb(98, 114, 164)}")
        self.enjoyurgame_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.enjoyurgame_lbl.setWordWrap(False)
        self.enjoyurgame_lbl.setObjectName("enjoyurgame_lbl")
        self.progress_bar = QProgressBar(self.shadowFrame)
        self.progress_bar.setObjectName(u"progressBar")
        self.progress_bar.setGeometry(QRect(0, 390, 801, 23))
        self.progress_bar.setStyleSheet(u"QProgressBar {\n"
"	\n"
"	background-color: rgb(98, 114, 164);\n"
"	color: rgb(200, 200, 200);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}")
        self.progress_bar.setValue(0)
        self.loading_lbl = QtWidgets.QLabel(self.shadowFrame)
        self.loading_lbl.setGeometry(QtCore.QRect(0, 450, 821, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.loading_lbl.setFont(font)
        self.loading_lbl.setStyleSheet("QLabel {color: rgb(98, 114, 164)}")
        self.loading_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.loading_lbl.setWordWrap(False)
        self.loading_lbl.setObjectName("loading_lbl")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_lbl.setText(_translate("MainWindow", "<html><head/><body>\n"
"<p>\n"
"<strong>Tic Tac Toe</strong> Game\n"
"\n"
"</p></body></html>"))
        self.enjoyurgame_lbl.setText(_translate("MainWindow", "<html><head/><body>\n"
"<p>\n"
"<strong>Enjoy Your</strong> Game\n"
"\n"
"</p></body></html>"))
        self.loading_lbl.setText(_translate("MainWindow", "<html><head/><body>\n"
"<p>\n"
"<strong>Loading...</strong>\n"
"\n"
"</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

