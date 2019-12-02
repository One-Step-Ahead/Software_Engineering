from collections import deque

from game.cards import input_card
from game.game_board import Player, Card
from game.rules import check_wizzad_win, check_if_playable


class Stich:
    def __init__(self, player_q: deque):
        self.player_q = player_q
        self.cards_in_play = list()
        self.winner = Player

    def get_player(player_number: int, player_q: list):
        return player_q[player_number]

    def check_stich_winner(self, cards_in_play: list, player_q: deque) -> Player:
        """

        :param cards_in_play:
        :return: Player that won the Stich
        """
        if check_wizzad_win(cards_in_play):  # todo Bitte mit Stich implementieren (returnt nix)
            return Player

    def play(self, player_queue: deque):
        """
        Execute the Stich!
        """
        allowed = bool
        chosen_card = Card

        for i in player_queue:
            print("It is now the turn of Player:", i.id)
            while allowed:
                chosen_card = input_card(i.hand)
                if check_if_playable(chosen_card, self.cards_in_play, i.hand):
                    allowed = False
                else:
                    print('You are not allowed to play this card right now!')
            i.play_card(chosen_card, i.hand)
        self.check_stich_winner(self.cards_in_play, player_queue)
