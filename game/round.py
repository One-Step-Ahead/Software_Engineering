from collections import defaultdict
from random import choice

from game.cards import ColoredCard, SpecialCard, input_card
from game.player import Player
from game.stich import Stich


class Round:

    def __init__(self, actual_round: int):
        self.round_nr = actual_round
        self.atut = ColoredCard
        self.cards_in_play = list()
        self.predictions = dict()
        self.stiche = list()
        self.stiche_won = defaultdict(int)
        self.score_result = dict()

    def input_prediction(self, player: Player) -> int:
        print('Player No.:', player.id, 'how many "Stiche" will you win?')
        while True:
            try:
                input_value = int(input())
                return input_value
            except ValueError:
                print('Please input a Number! How many "Stiche" will you win?')

    def predict(self, player: Player):
        prediction_value = self.input_prediction(player)
        if prediction_value > self.round_nr:
            print("Called Stiche cant exceed amount of cards in game, please choose a lower number")
            raise ValueError  # ist die python form von exception throw
        else:
            self.predictions[player] = prediction_value

    def set_atut_manually(self):
        chosen_card = input_card([ColoredCard(0, 'red'),
                                  ColoredCard(0, 'green'),
                                  ColoredCard(0, 'blue'),
                                  ColoredCard(0, 'yellow')])
        self.atut = chosen_card

    def set_new_atut(self, rounds_total: int, card_deck: list):
        if self.round_nr != rounds_total:
            new_atut = choice(card_deck)
            if isinstance(new_atut, ColoredCard):
                self.atut = new_atut
            elif isinstance(new_atut, SpecialCard):
                if new_atut.cardType == 'z':
                    self.set_atut_manually()
                else:
                    self.atut = None
        else:
            self.atut = None

    def calculate_score(self) -> int:
        self.count_win()

    def count_win(self):
        for i in self.stiche:
            if isinstance(i, Stich):
                if isinstance(self.stiche_won[i.winner], type(int)):
                    self.stiche_won[i.winner] = 1
                else:
                    self.stiche_won[i.winner] += 1
