import unittest
from unittest.mock import patch

from game.cards import ColoredCard, input_card


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
            result = input_card(self.hand)
        self.assertEqual(result, self.hand[19])
