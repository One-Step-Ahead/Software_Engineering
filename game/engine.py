from game.game_board import GameBoard
from game.testing import test

player_count = 4


def init(player_total: int):
    g = GameBoard(player_total)
    test(g)


init(player_count)
