import unittest

from game.cards import ColoredCard
from game.game_board import GameBoard
from game.round import Round
from game.stich import Stich


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.g = GameBoard(4, False)

    def test_winner_new_stich(self):
        self.g.new_round()
        s = Stich(self.g.player_queue, ColoredCard(0, "yellow"))
        s.winner = self.g.players[3]
        self.g.get_current_round().stiche.append(s)

        self.assertEqual(self.g.set_stich_queue(2)[0], self.g.players[3])

    def test_stich_round_3(self):
        self.g.current_round_count = 3
        r = [Round(1), Round(2), Round(3)]
        s = [Stich(self.g.player_queue),
             Stich(self.g.player_queue)]

        s[1].winner = self.g.players[2]
        r[2].stiche.extend(s)
        self.g.score_board.round_score.extend(r)
        result = tuple(self.g.set_stich_queue(3))
        expected = tuple([self.g.players[2],
                          self.g.players[3],
                          self.g.players[0],
                          self.g.players[1]])
        self.assertTupleEqual(result, expected)
