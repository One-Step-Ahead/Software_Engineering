# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prediction_popup.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Prediction(object):
    def setupUi(self, Prediction):
        Prediction.setObjectName("Prediction")
        Prediction.resize(243, 164)
        self.comboBox = QtWidgets.QComboBox(Prediction)
        self.comboBox.setGeometry(QtCore.QRect(100, 70, 41, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.headline = QtWidgets.QLabel(Prediction)
        self.headline.setGeometry(QtCore.QRect(70, 10, 131, 51))
        self.headline.setObjectName("headline")
        self.predict = QtWidgets.QPushButton(Prediction)
        self.predict.setGeometry(QtCore.QRect(80, 110, 75, 23))
        self.predict.setObjectName("predict")

        self.retranslateUi(Prediction)
        QtCore.QMetaObject.connectSlotsByName(Prediction)

    def retranslateUi(self, Prediction):
        _translate = QtCore.QCoreApplication.translate
        Prediction.setWindowTitle(_translate("Prediction", "Prediction"))
        Prediction.setStatusTip(_translate("Prediction", "blabla"))
        self.comboBox.setItemText(0, _translate("Prediction", "0"))
        self.comboBox.setItemText(1, _translate("Prediction", "1"))
        self.comboBox.setItemText(2, _translate("Prediction", "2"))
        self.comboBox.setItemText(3, _translate("Prediction", "3"))
        self.headline.setText(_translate("Prediction", "How many Stich are you  \n"
"going to make this Round?"))
        self.predict.setText(_translate("Prediction", "i foresaw it!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Prediction = QtWidgets.QWidget()
    ui = Ui_Prediction()
    ui.setupUi(Prediction)
    Prediction.show()
    sys.exit(app.exec_())
