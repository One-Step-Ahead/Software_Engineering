from game import player
from game.cards import *
from game.player import *


def test_print_cards(card_deck: list):
    print('Total number of Cards in Deck:', len(card_deck))
    print('{', end='')
    for i in card_deck:
        if type(i) is ColoredCard:
            print(i.cardColor, end=' ')
            print(i.cardNumber, end=', ')
        elif type(i) is SpecialCard:
            print(i.cardType, end=', ')
    print('}')


def test_print_players(players: list):
    print('Total number of players: ', len(players))
    for i in players:
        check_player_hand_cards(i)


def check_player_hand_cards(player: Player):
    for i in player.hand:
        print('This is the Hand of Player', player.id)
        print(i, end=',')
