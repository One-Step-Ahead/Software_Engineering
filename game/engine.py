from game.game_board import GameBoard
from game.testing import test


def init():
    g = GameBoard()
    test(g)


init()
