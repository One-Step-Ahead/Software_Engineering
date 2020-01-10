from game.game_board import GameBoard
from game.player import Player

from gui.interface import *

"""
This file connects the interface with the game logic.

:Interface takes care of interface related stuff.
:Core takes care of the logic.
"""


class Interface:
    def __init__(self):
        """
        this makes the interface running
        """
        import sys

        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        sys.exit(self.app.exec_())

    def set_player_cards_string(player: Player):
        pass


class Core:
    def __init__(self, gameboard: GameBoard):
        """
        Core contains controlls all top-level functions of the game.

        :param gameboard: takes in the gameboard
        :param interface: initialize the interface
        """
        self.g = gameboard
        self.i = Interface()

    def run_game_loop(self):
        for i in range(0, self.g.rounds_total):
            self.g.new_round()
            self.i.ui.Textausgabe.setText('It is now Round %i' % (g.get_current_round()))
            for j in self.g.player_queue:
                self.g.get_current_round().predict(j)

# todo make runnable
