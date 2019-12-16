from unittest import TestCase

from game.cards import ColoredCard
from game.game_board import *
from game.stich import Stich


class TestStichWinner(TestCase):
    def setUp(self) -> None:
        self.g = GameBoard(4)
        self.g.new_round()
        self.s = Stich(self.g.player_queue, ColoredCard(1, 'red'))

    def test_single_atutwin(self):
        self.s.cards_in_play.append(ColoredCard(5, 'green'))
        self.s.cards_in_play.append(ColoredCard(6, 'green'))
        self.s.cards_in_play.append(ColoredCard(10, 'green'))
        self.s.cards_in_play.append(ColoredCard(5, 'red'))

        self.assertEqual(self.s.check_stich_winner(), self.s.player_q[3])

    def test_colorwin(self):
        self.s.cards_in_play.append(ColoredCard(5, 'green'))
        self.s.cards_in_play.append(ColoredCard(6, 'green'))
        self.s.cards_in_play.append(ColoredCard(10, 'green'))
        self.s.cards_in_play.append(ColoredCard(13, 'green'))

        self.assertEqual(self.s.check_stich_winner(), self.s.player_q[3])

    def test_wizzard_win(self):
        self.s.cards_in_play.append(SpecialCard("z"))
        self.s.cards_in_play.append(ColoredCard(6, 'green'))
        self.s.cards_in_play.append(ColoredCard(10, 'green'))
        self.s.cards_in_play.append(ColoredCard(13, 'green'))

        self.assertEqual(self.s.check_stich_winner(), self.s.player_q[0])

    def test_narr_only_win(self):
        self.s.cards_in_play.append(SpecialCard("n"))
        self.s.cards_in_play.append(SpecialCard("n"))
        self.s.cards_in_play.append(SpecialCard("n"))
        self.s.cards_in_play.append(SpecialCard("n"))

        self.assertEqual(self.s.check_stich_winner(), self.s.player_q[0])

    def test_multiple_atut_win(self):
        self.s.cards_in_play.append(ColoredCard(6, 'red'))
        self.s.cards_in_play.append(ColoredCard(10, 'red'))
        self.s.cards_in_play.append(ColoredCard(13, 'red'))
        self.s.cards_in_play.append(SpecialCard('n'))

        self.assertEqual(self.s.check_stich_winner(), self.s.player_q[2])
