from game.game_board import *


def play_card(player: Player, played_card: Card):
    player.hand.remove(played_card)


def play_round(gameboard):
    for i in gameboard.player_queue:
        play_card()
