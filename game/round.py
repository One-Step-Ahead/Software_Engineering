from random import choice

from game.cards import Card


class Round:

    def __init__(self, actual_round: int):
        self.round_nr = actual_round
        self.atut = Card
        self.cards_in_play = list()
        self.all_predictions = dict()
        self.all_stich = list()

    def new_prediction(self, player, anz_stiche):
        if anz_stiche > self.round_nr:
            print("Called Stiche cant exceed amount of cards in game, please choose a lower number")
            raise ValueError  # ist die python form von exception throw
        else:
            self.all_predictions[player] = anz_stiche

    def set_new_atut(self, rounds_total: int, card_deck: list):
        if self.round_nr != rounds_total:
            self.atut = choice(card_deck)
        else:
            self.atut = None
