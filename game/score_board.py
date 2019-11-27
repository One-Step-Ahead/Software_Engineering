from game.player import Player
from game.round import Round


class ScoreBoard:

    def __init__(self):
        self.total_score = list()
        self.round_score = list()
        self.prediction_total = list()
        self.rounds = []

    def make_prediction(self, player: Player, prediction: int, round: Round):
        self.prediction_total.append(Prediction(player, prediction, round.round_nr))


class Prediction:

    def __init__(self, player: Player, prediction: int, round: int):
        if prediction > round:
            print("Called Stiche cant exceed ammount of cards in game, please choose a lower number")
            raise ValueError  # ist die python form von exception throw
        else:
            self.player = player
            self.prediction = prediction
            self.round = round
