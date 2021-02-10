# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'msgbox.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(710, 239)
        self.black_frame = QtWidgets.QFrame(Form)
        self.black_frame.setGeometry(QtCore.QRect(0, 0, 711, 241))
        self.black_frame.setStyleSheet("#black_frame {\n"
"    background-color:rgb(17, 21, 255) ;\n"
"}")
        self.black_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.black_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.black_frame.setObjectName("black_frame")
        self.var_lbl = QtWidgets.QLabel(self.black_frame)
        self.var_lbl.setGeometry(QtCore.QRect(10, 20, 711, 71))
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(99)
        self.var_lbl.setFont(font)
        self.var_lbl.setStyleSheet("QLabel {\n"
"    color: rgb(73, 255, 41);\n"
"    font-weight: 1000;\n"
"    font-size: 40px;\n"
"}")
        self.var_lbl.setLineWidth(1)
        self.var_lbl.setWordWrap(False)
        self.var_lbl.setObjectName("var_lbl")
        self.const_lbl = QtWidgets.QLabel(self.black_frame)
        self.const_lbl.setGeometry(QtCore.QRect(0, 80, 711, 121))
        self.const_lbl.setStyleSheet("QLabel {\n"
"    color: yellow;\n"
"    font-weight: 700;\n"
"    font-size: 23px;\n"
"    \n"
"    \n"
"}")
        self.const_lbl.setObjectName("const_lbl")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.var_lbl.setText(_translate("Form", "<center>Player(X) Has Been Got a Score !</center>"))
        self.const_lbl.setText(_translate("Form", "<center>\n"
"Your Blocks Will Have Been Cleared When You <br> Close Here and You May Play Again !\n"
"</center>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

