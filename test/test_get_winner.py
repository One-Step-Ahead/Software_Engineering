import unittest

from game.game_board import *


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.g = GameBoard(4, False)

    def test_two_winners(self):
        self.g.players[0].score = 100
        self.g.players[1].score = 200
        self.g.players[2].score = 50
        self.g.players[3].score = 200
        self.assertEqual(self.g.get_winner(), [self.g.players[1], self.g.players[3]])

    def test_one_winners(self):
        self.g.players[0].score = 100
        self.g.players[1].score = 200
        self.g.players[2].score = 50
        self.g.players[3].score = 150
        self.assertEqual(self.g.get_winner(), [self.g.players[1]])

    def test_three_winners(self):
        self.g.players[0].score = 50
        self.g.players[1].score = -100
        self.g.players[2].score = 50
        self.g.players[3].score = 50
        self.assertEqual(self.g.get_winner(), [self.g.players[0],
                                               self.g.players[2],
                                               self.g.players[3]])
