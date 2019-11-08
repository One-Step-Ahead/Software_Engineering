from game.player import *


class GameBoardMeta(type):
    _instance = None

    def __call__(self):
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class GameBoard(metaclass=GameBoardMeta):

    def __init__(self):
        self.card_deck = create_all_cards()
        self.players = create_players()
        self.played_cards = list()
        self.round_counter = int
