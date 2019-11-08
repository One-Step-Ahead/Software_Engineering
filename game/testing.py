from game.game_board import GameBoard
from game.player import *


def test_print_cards(card_deck: list):
    print('Total number of Cards in Deck:', len(card_deck))
    print('{ ', end='')
    for i in card_deck:
        i.print_card()
        print(end=' ')
    print('}\n')


def test_print_players_cards(players: list):
    for i in players:
        check_player_hand_cards(i)
        print()


def test_number_of_players(players: list):
    print('Total number of players: ', len(players))


def check_player_hand_cards(player: Player):
    print('This is the Hand of Player', player.id)
    for i in player.hand:
        i.print_card()


def test(g: GameBoard):
    test_number_of_players(g.players)
    test_print_cards(g.card_deck)
    test_print_players_cards(g.players)

    g.players[0].draw_card(g.card_deck)
    test_print_players_cards(g.players)
