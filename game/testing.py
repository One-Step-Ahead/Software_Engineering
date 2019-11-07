from game.cards import *


def test_print(card_deck):
    print('Total number of Cards in Deck:', len(card_deck))
    print('{', end='')
    for i in card_deck:
        if type(i) is ColoredCard:
            print(i.cardColor, end=' ')
            print(i.cardNumber, end=', ')
        elif type(i) is SpecialCard:
            print(i.cardType, end=', ')
    print('}')
