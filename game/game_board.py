from game.cards import *
from game.testing import test_print


def init():
    card_deck = create_all_cards()
    test_print(card_deck)


init()
