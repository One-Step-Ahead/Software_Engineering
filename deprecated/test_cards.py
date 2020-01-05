import unittest
from unittest.mock import patch

from game.cards import ColoredCard, ask_for_card


class TestCountWin(unittest.TestCase):
    def setUp(self) -> None:
        self.hand = [ColoredCard(3, 'red'),
                     ColoredCard(1, 'blue'),
                     ColoredCard(1, 'yellow'),
                     ColoredCard(2, 'blue'),
                     ColoredCard(10, 'yellow'),
                     ColoredCard(12, 'blue'),
                     ColoredCard(12, 'blue'),
                     ColoredCard(12, 'blue'),
                     ColoredCard(12, 'blue'),
                     ColoredCard(12, 'blue'),
                     ColoredCard(12, 'blue'),
                     ColoredCard(12, 'blue'),
                     ColoredCard(12, 'blue'),
                     ColoredCard(12, 'blue'),
                     ColoredCard(12, 'blue'),
                     ColoredCard(12, 'blue'),
                     ColoredCard(12, 'blue'),
                     ColoredCard(12, 'blue'),
                     ColoredCard(12, 'blue'),
                     ColoredCard(12, 'blue'),
                     ]

    def test_card_input(self):
        user_input = 20
        with patch('builtins.input', return_value=user_input):
            result = ask_for_card(self.hand)
        self.assertEqual(result, self.hand[19])

    def test_card_wrong_input_number_high(self):
        user_input = 100
        with patch('builtins.input', return_value=user_input):
            result = ask_for_card(self.hand)
            self.assertRaises(IndexError)

    def test_card_wrong_input_number_negative(self):
        user_input = -15
        with patch('builtins.input', return_value=user_input):
            result = ask_for_card(self.hand)
            self.assertRaises(ValueError)
