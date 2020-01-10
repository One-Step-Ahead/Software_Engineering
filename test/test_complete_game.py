
import unittest

from game.game_board import *


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.g = GameBoard(4, False)

    def test_four_winners(self):
        self.g.winners = self.g.players
        self.g.winners[0].name = "Paul"
        self.g.winners[1].name = "Lisa"
        self.g.winners[2].name = "Bob"
        self.g.winners[3].name = "Hanna"
        self.g.complete_game()
