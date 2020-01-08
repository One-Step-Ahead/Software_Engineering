from game.game_board import GameBoard

# Options
# Enter all options here:

player_count = 4
cli_inputs = True
use_gui = False


def init(player_total: int):
    g = GameBoard(player_total, cli_inputs)
    # g.start()
    g.game_loop()
    # test(g)


init(player_count)
