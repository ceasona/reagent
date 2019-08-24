# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'control.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 500)
        Form.setMinimumSize(QtCore.QSize(600, 500))
        Form.setMaximumSize(QtCore.QSize(600, 500))
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(50, 125, 500, 250))
        self.widget.setMinimumSize(QtCore.QSize(500, 250))
        self.widget.setMaximumSize(QtCore.QSize(500, 250))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgb(3, 3, 3);\n"
"\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(130, 150, 211, 60))
        self.pushButton.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 60))
        self.pushButton.setStyleSheet("\n"
"QPushButton{\n"
"    background-color:rgb(0, 0, 0);\n"
"    border-radius:15px;\n"
"    font: 25 20pt \"微软雅黑 Light\";\n"
"    color: rgb(255, 255, 255);\n"
"    border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(0, 0, 77);\n"
"   \n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(91, 0, 0);\n"
"}\n"
"QPushButton:disabled{\n"
"    background-color:rgb(88, 88, 88);\n"
"}\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(190, 30, 100, 100))
        self.widget_2.setMinimumSize(QtCore.QSize(100, 100))
        self.widget_2.setMaximumSize(QtCore.QSize(100, 100))
        self.widget_2.setStyleSheet("border-image: url(:/newPrefix/下载.jpg);")
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 400, 500, 40))
        self.label.setMinimumSize(QtCore.QSize(500, 40))
        self.label.setMaximumSize(QtCore.QSize(500, 40))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 25 18pt \"微软雅黑 Light\";\n"
"\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.openCsv)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "选择文件"))
        self.label.setText(_translate("Form", "xls文件要求：在第一列依此往下填充数据"))

import img_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

