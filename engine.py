from game.game_board import GameBoard

# Options
# Enter all options here:

player_count = 6
cli_inputs = True
use_gui = False


def init():
    global g
    g = GameBoard(player_count, cli_inputs)
    if use_gui:
        # gui_connect()
        pass
    else:
        g.game_loop()

    # g.start()
    # test(g)


init()
