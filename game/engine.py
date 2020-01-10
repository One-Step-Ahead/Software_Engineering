from game.game_board import GameBoard
from gui.connect import gui_connect

# Options
# Enter all options here:

# ****************************
# Make config here:
player_count = 4
cli_inputs = True
use_gui = True
# ****************************
g = GameBoard


def init():
    global g
    g = GameBoard(player_count, cli_inputs)
    if use_gui:
        gui_connect()
    else:
        g.start()

    # g.game_loop()
    # test(g)


init()
