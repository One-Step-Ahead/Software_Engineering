import unittest
from unittest import TestCase

from game.cards import ColoredCard
from game.game_board import *
from game.stich import Stich


class TestStichWinner(TestCase):
    def setUp(self) -> None:
        self.g = GameBoard(4)
        self.g.new_round()
        self.s = Stich(self.g.player_queue, ColoredCard(1, 'red'))

    def test_check_stich_winner_atutwin(self):
        """ Testing if the function is able to check the """
        self.s.cards_in_play.append(ColoredCard(5, 'green'))
        self.s.cards_in_play.append(ColoredCard(6, 'green'))
        self.s.cards_in_play.append(ColoredCard(10, 'green'))
        self.s.cards_in_play.append(ColoredCard(5, 'red'))

        self.assertEqual(self.s.check_stich_winner(), self.s.player_q[3])

    def test_check_stich_winner_colorwin(self):
        self.s.cards_in_play.append(ColoredCard(5, 'green'))
        self.s.cards_in_play.append(ColoredCard(6, 'green'))
        self.s.cards_in_play.append(ColoredCard(10, 'green'))
        self.s.cards_in_play.append(ColoredCard(13, 'green'))

        self.assertEqual(self.s.check_stich_winner(), self.s.player_q[3])


if __name__ == '__main__':
    unittest.main()
