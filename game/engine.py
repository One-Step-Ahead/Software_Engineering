from game.game_board import GameBoard
from game.testing import test

# Options
# Enter all options here:

player_count = 4
cli_inputs = True


def init(player_total: int):
    g = GameBoard(player_total, cli_inputs)
    # g.start_game()
    test(g)


init(player_count)
