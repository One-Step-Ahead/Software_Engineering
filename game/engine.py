from game.game_board import GameBoard
from game.testing import test


def init():
    player_count = 4
    g = GameBoard(player_count)
    test(g)


init()
