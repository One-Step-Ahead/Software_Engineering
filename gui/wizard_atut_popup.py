# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wizard_atut_popup.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
#Autut
    #im falle,dass ein Zauberer aufgedeckt wird brauchen wir ein popup über welches dann das atut entschieden wird


class Ui_Form(object):

    def clicked_red(self):
        pass

    def clicked_blue(self):
        pass

    def clicked_yellow(self):
        pass

    def clicked_green(self):
        pass

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(345, 150)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 311, 81))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.choose_red = QtWidgets.QPushButton(Form)
        self.choose_red.setGeometry(QtCore.QRect(10, 100, 75, 23))
        self.choose_red.setObjectName("choose_red")
        self.choose_red.clicked.connect(self.clicked_red)

        self.choose_yellow = QtWidgets.QPushButton(Form)
        self.choose_yellow.setGeometry(QtCore.QRect(90, 100, 75, 23))
        self.choose_yellow.setObjectName("choose_yellow")
        self.choose_yellow.clicked.connect(self.clicked_yellow)

        self.choose_blue = QtWidgets.QPushButton(Form)
        self.choose_blue.setGeometry(QtCore.QRect(170, 100, 75, 23))
        self.choose_blue.setObjectName("choose_blue")
        self.choose_blue.clicked.connect(self.clicked_blue)

        self.choose_green = QtWidgets.QPushButton(Form)
        self.choose_green.setGeometry(QtCore.QRect(250, 100, 75, 23))
        self.choose_green.setObjectName("choose_green")
        self.choose_green.clicked.connect(self.clicked_green)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Its a Wizard!\n"
"Please choos a Atut"))
        self.choose_red.setText(_translate("Form", "Red"))
        self.choose_yellow.setText(_translate("Form", "Yellow"))
        self.choose_blue.setText(_translate("Form", "Blue"))
        self.choose_green.setText(_translate("Form", "Green"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
