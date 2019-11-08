from game.cards import *
from game.player import *


class GameBoardMeta(type):
    _instance = None

    def __call__(self):
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class GameBoard(metaclass=GameBoardMeta):

    def __init__(self):
        self.card_deck = list()
        self.players = create_players()
        self.cards_in_play = list()
        self.round_counter = 0

    def new_round(self):
        self.round_counter += 1

        self.card_deck.clear()
        create_all_cards(self.card_deck)
        for i in self.players:
            i.hand.clear()
            i.stich_score = 0
            i.draw_card(self.card_deck, self.round_counter)
        print('New Round! [', self.round_counter, ']', sep='')
