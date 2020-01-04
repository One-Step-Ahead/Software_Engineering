import unittest

from game.cards import ColoredCard
from game.game_board import GameBoard
from game.round import Round
from game.stich import Stich


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.g = GameBoard(4)
        self.players = self.g.players

    def tearDown(self) -> None:
        del self.g
        del self.players

    def test_score_round_1(self):
        round = Round(1)
        stich1 = Stich(self.g.player_queue, ColoredCard(0, 'red'))
        round.stiche.append(stich1)
        stich1.winner = self.g.players[0]
        prediction = {self.players[0]: 1,
                      self.players[1]: 0,
                      self.players[2]: 0,
                      self.players[3]: 1}
        round.predictions = prediction

        round.calculate_score(self.g.players)
        self.assertEqual(self.g.players[0].score, 30)
        self.assertEqual(self.g.players[1].score, 20)
        self.assertEqual(self.g.players[2].score, 20)
        self.assertEqual(self.g.players[3].score, -10)

    def test_score_round_3(self):
        round = Round(3)
        stich1 = Stich(self.g.player_queue, ColoredCard(0, 'red'))
        stich2 = Stich(self.g.player_queue, ColoredCard(0, 'red'))
        stich3 = Stich(self.g.player_queue, ColoredCard(0, 'red'))
        round.stiche.append(stich1)
        round.stiche.append(stich2)
        round.stiche.append(stich3)
        stich1.winner = self.g.players[0]
        stich2.winner = self.g.players[1]
        stich3.winner = self.g.players[0]
        prediction = {self.players[0]: 2,
                      self.players[1]: 3,
                      self.players[2]: 0,
                      self.players[3]: 1}
        round.predictions = prediction

        round.calculate_score(self.g.players)
        self.assertEqual(self.g.players[0].score, 40)
        self.assertEqual(self.g.players[1].score, -20)
        self.assertEqual(self.g.players[2].score, 20)
        self.assertEqual(self.g.players[3].score, -10)
