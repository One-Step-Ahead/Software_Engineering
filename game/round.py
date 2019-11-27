from game.cards import Card
from game.player import Player


class Round:

    def __init__(self, actual_round: int):
        self.round_nr = actual_round
        self.atut = Card
        self.cards_in_play = list()
        self.current_player = Player

    def new_stich(self):
        self.cards_in_play.clear()
