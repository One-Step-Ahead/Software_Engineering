from game.cards import *


def init():
    card_deck = create_all_cards()

    test_print(card_deck)


def test_print(card_deck):
    print(card_deck)
    print(card_deck[0].cardColor, end=' ')
    print(card_deck[0].cardNumber, end=', ')
    print(card_deck[1].cardColor, end=' ')
    print(card_deck[1].cardNumber, end=', ')
    print(card_deck[2].cardColor, end=' ')
    print(card_deck[2].cardNumber, end=', ')
    print(card_deck[16].cardColor, end=' ')
    print(card_deck[16].cardNumber, end=', ')


init()
