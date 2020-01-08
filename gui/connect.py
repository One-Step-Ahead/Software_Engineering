from game.game_board import GameBoard
from gui.interface import ui


def run_game_loop():
    global g
    for i in range(0, g.rounds_total):
        g.new_round()
        ui.Textausgabe.setText('It is now Round %i' % (g.get_current_round()))


def gui_connect():
    run_game_loop()

def set_player_cards_string():
    pass
