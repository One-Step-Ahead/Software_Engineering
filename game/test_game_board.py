import unittest

from game.cards import ColoredCard
from game.game_board import *


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.g = GameBoard(4)
        self.g.new_round()
        self.g.new_round()

    def test_set_stich_queue(self):
        stich1 = Stich(self.g.player_queue, ColoredCard(1, 'red'))
        stich1.winner = self.g.player_queue[1]
        self.g.get_current_round().stiche.append(stich1)
        self.assertEqual(self.g.player_queue[1], self.g.set_stich_queue(1)[0])
