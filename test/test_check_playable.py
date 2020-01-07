import unittest
from game.game_board import GameBoard
from game.cards import ColoredCard, SpecialCard
from game.stich import Stich


# noinspection DuplicatedCode
class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.g = GameBoard(4, False)

    def test_play_wizzard(self):
        self.s = Stich(self.g.player_queue, ColoredCard(0, "yellow"))

        hand_p0 = [SpecialCard("z"),
                   ColoredCard(5, "red")]
        hand_p1 = [ColoredCard(13, "red"),
                   ColoredCard(11, "red")]
        hand_p2 = [ColoredCard(6, "red"),
                   ColoredCard(1, "yellow")]
        hand_p3 = [ColoredCard(12, "red"),
                   SpecialCard("z")]
        cards_in_play = [ColoredCard(1, "red"),
                         ColoredCard(2, "red"),
                         ColoredCard(3, "red")]

        self.g.players[0].hand.extend(hand_p0)
        self.g.players[1].hand.extend(hand_p1)
        self.g.players[2].hand.extend(hand_p2)
        self.g.players[3].hand.extend(hand_p3)
        self.s.cards_in_play.extend(cards_in_play)

        self.assertTrue(self.s.check_if_playable(self.g.players[3].hand[1], self.g.players[3]))

    def test_farbzwang(self):
        self.s = Stich(self.g.player_queue, ColoredCard(0, "blue"))

        hand_p0 = [SpecialCard("z"),
                   ColoredCard(5, "red")]
        hand_p1 = [ColoredCard(13, "red"),
                   ColoredCard(11, "red")]
        hand_p2 = [ColoredCard(6, "red"),
                   ColoredCard(1, "yellow")]
        hand_p3 = [ColoredCard(12, "red"),
                   SpecialCard("z")]
        cards_in_play = [ColoredCard(1, "red"),
                         ColoredCard(2, "yellow"),
                         ColoredCard(3, "yellow")]

        self.g.players[0].hand.extend(hand_p0)
        self.g.players[1].hand.extend(hand_p1)
        self.g.players[2].hand.extend(hand_p2)
        self.g.players[3].hand.extend(hand_p3)
        self.s.cards_in_play.extend(cards_in_play)

        self.assertFalse(self.s.check_if_playable(self.g.players[2].hand[1], self.g.players[2]))

    def test_on_top_of_wizzard(self):
        self.s = Stich(self.g.player_queue, ColoredCard(0, "blue"))

        hand_p0 = [SpecialCard("z"),
                   ColoredCard(5, "red")]
        hand_p1 = [ColoredCard(13, "red"),
                   ColoredCard(11, "red")]
        hand_p2 = [ColoredCard(6, "red"),
                   ColoredCard(1, "yellow")]
        hand_p3 = [ColoredCard(12, "red"),
                   SpecialCard("z")]
        cards_in_play = [SpecialCard("z"),
                         ColoredCard(1, "red"),
                         ColoredCard(1, "blue")]

        self.g.players[0].hand.extend(hand_p0)
        self.g.players[1].hand.extend(hand_p1)
        self.g.players[2].hand.extend(hand_p2)
        self.g.players[3].hand.extend(hand_p3)
        self.s.cards_in_play.extend(cards_in_play)

        self.assertTrue(self.s.check_if_playable(self.g.players[2].hand[1], self.g.players[2]))

    def test_on_top_of_narr(self):
        self.s = Stich(self.g.player_queue, ColoredCard(0, "blue"))

        hand_p0 = [SpecialCard("z"),
                   ColoredCard(5, "red")]
        hand_p1 = [ColoredCard(13, "red"),
                   ColoredCard(11, "red")]
        hand_p2 = [ColoredCard(6, "red"),
                   ColoredCard(1, "yellow")]
        hand_p3 = [ColoredCard(12, "red"),
                   SpecialCard("z")]
        cards_in_play = [SpecialCard("n"),
                         ColoredCard(1, "red"),
                         ColoredCard(1, "blue")]

        self.g.players[0].hand.extend(hand_p0)
        self.g.players[1].hand.extend(hand_p1)
        self.g.players[2].hand.extend(hand_p2)
        self.g.players[3].hand.extend(hand_p3)
        self.s.cards_in_play.extend(cards_in_play)

        self.assertTrue(self.s.check_if_playable(self.g.players[2].hand[1], self.g.players[2]))
