# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets, QtGui


class Ui_MainWindow(object):
    """
    folgend werden die funktionen definiert welche durch buttonclicks ausgeführt werden
    was sollen die knöpfe machen?
    "cards" sollen
        1.Die Karten der jeweiligen Spielerhand anzeigen und
        2.Auf Clicken versuchen diese Karte zu spielen

    Last_Card_Played
    soll dann die geklickte/gespielte karte anzeigen

    def update_scoreboard(self):
        current_time= str(datetime.datetime.now().time())
        ui.label.setText(current_time)
    """

    def clicked_card_0(self):
        print("This is Card 1")
        self.Card_2.setIcon(QtGui.QIcon(''))

    def clicked_card_1(self):
        print("This is Card 2")
        self.Card_1.setIcon(QtGui.QIcon(''))  # dateipfad einfügen

    def clicked_card_2(self):
        print("This is Card 3")
        self.Card_2.setIcon(QtGui.QIcon(''))

    def clicked_card_3(self):
        print("This is Card 4")

    def clicked_card_4(self):
        print("This is Card 5")

    def clicked_card_5(self):
        print("This is Card 6")

    def clicked_card_6(self):
        print("This is Card 7")

    def clicked_card_7(self):
        print("This is Card 8")

    def clicked_card_8(self):
        print("This is Card 9")

    def clicked_card_9(self):
        print("This is Card 10")

    def clicked_card_10(self):
        print("This is Card 11")

    def clicked_card_11(self):
        print("This is Card 12")

    def clicked_card_12(self):
        print("This is Card 13")

    def clicked_card_13(self):
        print("This is Card 14")

    def clicked_card_14(self):
        print("This is Card 15")

    def clicked_aktuelle_stiche(self):
        print("aktuelle stiche")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1117, 897)
        MainWindow.setToolTip("")
        MainWindow.setStyleSheet(
            "file:///C:/Users/sebas/Documents/FH_local/3Sem/Software Engineering/LearningWizzard/software/game/styling.css")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.P1_Last_Played = QtWidgets.QPushButton(self.centralwidget)
        self.P1_Last_Played.setGeometry(QtCore.QRect(520, 290, 81, 121))
        self.P1_Last_Played.setText("")
        self.P1_Last_Played.setObjectName("P1_Last_Played")

        self.P4_Last_Played = QtWidgets.QPushButton(self.centralwidget)
        self.P4_Last_Played.setGeometry(QtCore.QRect(400, 210, 121, 81))
        self.P4_Last_Played.setText("")
        self.P4_Last_Played.setObjectName("P4_Last_Played")

        self.P3_Last_Played = QtWidgets.QPushButton(self.centralwidget)
        self.P3_Last_Played.setGeometry(QtCore.QRect(520, 90, 81, 121))
        self.P3_Last_Played.setText("")
        self.P3_Last_Played.setObjectName("P3_Last_Played")

        self.P2_Last_Played = QtWidgets.QPushButton(self.centralwidget)
        self.P2_Last_Played.setGeometry(QtCore.QRect(600, 210, 121, 81))
        self.P2_Last_Played.setText("")
        self.P2_Last_Played.setObjectName("P2_Last_Played")

        self.Textausgabe = QtWidgets.QLabel(self.centralwidget)
        self.Textausgabe.setGeometry(QtCore.QRect(370, 770, 471, 71))
        self.Textausgabe.setObjectName("Textausgabe")

        self.Punktetabelle = QtWidgets.QLabel(self.centralwidget)
        self.Punktetabelle.setGeometry(QtCore.QRect(890, 10, 211, 271))
        self.Punktetabelle.setObjectName("Punktetabelle")

        self.Aktuelle_Stiche = QtWidgets.QPushButton(self.centralwidget)
        self.Aktuelle_Stiche.setGeometry(QtCore.QRect(40, 790, 281, 51))
        self.Aktuelle_Stiche.setObjectName("Aktuelle_Stiche")
        self.Aktuelle_Stiche.clicked.connect(self.clicked_aktuelle_stiche)

        self.Rundendisplay = QtWidgets.QLabel(self.centralwidget)
        self.Rundendisplay.setGeometry(QtCore.QRect(10, 20, 211, 271))
        self.Rundendisplay.setObjectName("Rundendisplay")

        self.Card_0 = QtWidgets.QPushButton(self.centralwidget)
        self.Card_0.setGeometry(QtCore.QRect(280, 490, 81, 121))
        self.Card_0.setText("")
        self.Card_0.setObjectName("Card_0")
        self.Card_0.clicked.connect(self.clicked_card_0)

        self.Card_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Card_1.setGeometry(QtCore.QRect(360, 490, 81, 121))
        self.Card_1.setText("")
        self.Card_1.setObjectName("Card_1")
        self.Card_1.clicked.connect(self.clicked_card_1)

        self.Card_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Card_2.setGeometry(QtCore.QRect(440, 490, 81, 121))
        self.Card_2.setText("")
        self.Card_2.setObjectName("Card_2")
        self.Card_2.clicked.connect(self.clicked_card_2)

        self.Card_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Card_3.setGeometry(QtCore.QRect(520, 490, 81, 121))
        self.Card_3.setText("")
        self.Card_3.setObjectName("Card_3")
        self.Card_3.clicked.connect(self.clicked_card_3)

        self.Card_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Card_4.setGeometry(QtCore.QRect(600, 490, 81, 121))
        self.Card_4.setText("")
        self.Card_4.setObjectName("Card_4")
        self.Card_4.clicked.connect(self.clicked_card_4)

        self.Card_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Card_5.setGeometry(QtCore.QRect(680, 490, 81, 121))
        self.Card_5.setText("")
        self.Card_5.setObjectName("Card_5")
        self.Card_5.clicked.connect(self.clicked_card_5)

        self.Card_6 = QtWidgets.QPushButton(self.centralwidget)
        self.Card_6.setGeometry(QtCore.QRect(760, 490, 81, 121))
        self.Card_6.setText("")
        self.Card_6.setObjectName("Card_6")
        self.Card_6.clicked.connect(self.clicked_card_6)

        self.Card_7 = QtWidgets.QPushButton(self.centralwidget)
        self.Card_7.setGeometry(QtCore.QRect(240, 620, 81, 121))
        self.Card_7.setText("")
        self.Card_7.setObjectName("Card_7")
        self.Card_7.clicked.connect(self.clicked_card_7)

        self.Card_8 = QtWidgets.QPushButton(self.centralwidget)
        self.Card_8.setGeometry(QtCore.QRect(320, 620, 81, 121))
        self.Card_8.setText("")
        self.Card_8.setObjectName("Card_8")
        self.Card_8.clicked.connect(self.clicked_card_8)

        self.Card_9 = QtWidgets.QPushButton(self.centralwidget)
        self.Card_9.setGeometry(QtCore.QRect(400, 620, 81, 121))
        self.Card_9.setText("")
        self.Card_9.setObjectName("Card_9")
        self.Card_9.clicked.connect(self.clicked_card_9)

        self.Card_10 = QtWidgets.QPushButton(self.centralwidget)
        self.Card_10.setGeometry(QtCore.QRect(480, 620, 81, 121))
        self.Card_10.setText("")
        self.Card_10.setObjectName("Card_10")
        self.Card_10.clicked.connect(self.clicked_card_10)

        self.Card_11 = QtWidgets.QPushButton(self.centralwidget)
        self.Card_11.setGeometry(QtCore.QRect(560, 620, 81, 121))
        self.Card_11.setText("")
        self.Card_11.setObjectName("Card_11")
        self.Card_11.clicked.connect(self.clicked_card_11)

        self.Card_12 = QtWidgets.QPushButton(self.centralwidget)
        self.Card_12.setGeometry(QtCore.QRect(640, 620, 81, 121))
        self.Card_12.setText("")
        self.Card_12.setObjectName("Card_12")
        self.Card_12.clicked.connect(self.clicked_card_12)

        self.Card_13 = QtWidgets.QPushButton(self.centralwidget)
        self.Card_13.setGeometry(QtCore.QRect(720, 620, 81, 121))
        self.Card_13.setText("")
        self.Card_13.setObjectName("Card_13")
        self.Card_13.clicked.connect(self.clicked_card_13)

        self.Card_14 = QtWidgets.QPushButton(self.centralwidget)
        self.Card_14.setGeometry(QtCore.QRect(800, 620, 81, 121))
        self.Card_14.setText("")
        self.Card_14.setObjectName("Card_14")
        self.Card_14.clicked.connect(self.clicked_card_14)

        self.yours_handcards = QtWidgets.QLabel(self.centralwidget)
        self.yours_handcards.setGeometry(QtCore.QRect(290, 442, 331, 31))
        self.yours_handcards.setObjectName("your_handcards")

        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(460, 20, 201, 51))
        self.title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setWordWrap(False)
        self.title.setObjectName("title")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1117, 21))
        self.menubar.setObjectName("menubar")

        self.menuMenue = QtWidgets.QMenu(self.menubar)
        self.menuMenue.setObjectName("menuMenue")

        self.menuRules = QtWidgets.QMenu(self.menubar)
        self.menuRules.setObjectName("menuRules")

        self.menuSetup = QtWidgets.QMenu(self.menubar)
        self.menuSetup.setObjectName("menuSetup")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMenue.menuAction())
        self.menubar.addAction(self.menuSetup.menuAction())
        self.menubar.addAction(self.menuRules.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.player_cards = [self.Card_0, self.Card_1, self.Card_2, self.Card_3, self.Card_4, self.Card_5,
                             self.Card_6, self.Card_7, self.Card_8, self.Card_9, self.Card_10,
                             self.Card_11, self.Card_12, self.Card_13, self.Card_14]

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Learning Wizard"))

        self.Textausgabe.setText(_translate("MainWindow", "spieler x hat karte y gespielt"))

        self.Punktetabelle.setText(_translate("MainWindow", "Score: \n"
                                                            " Player 1: \n"
                                                            " \n"
                                                            " Player 2: \n"
                                                            " \n"
                                                            " Player 3: \n"
                                                            " \n"
                                                            " Player 4: \n"
                                                            " "))

        self.Aktuelle_Stiche.setText(_translate("MainWindow", "Player 1: __ Player2:__  Player3: __ Player4: __"))

        self.Rundendisplay.setText(_translate("MainWindow", "Aktuelle Runde: \n"
                                                            " \n"
                                                            " Aktueller Stich:\n"
                                                            ""))

        self.yours_handcards.setText(_translate("MainWindow", "Your Handcards"))

        self.title.setText(_translate("MainWindow", "LeWi 1.0"))

        self.menuMenue.setTitle(_translate("MainWindow", "New Game"))

        self.menuRules.setTitle(_translate("MainWindow", "Rules"))

        self.menuSetup.setTitle(_translate("MainWindow", "Setup"))
