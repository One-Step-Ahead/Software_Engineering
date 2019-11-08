from game.game_board import GameBoard
from game.player import *


def test(g: GameBoard):
    test_number_of_players(g.players)

    for i in range(0, g.rounds_total):
        g.new_round()
        print_atut(g)
        test_print_players_cards(g.players)


def test_print_cards(card_deck: list):
    print('Total number of Cards in Deck:', len(card_deck))
    print('{ ', end='')
    for i in card_deck:
        i.print_card()
        print(end=' ')
    print('}\n')


def test_print_players_cards(players: list):
    print('*******************')
    for i in players:
        check_player_hand_cards(i)
        print()
    print('*******************\n')


def test_number_of_players(players: list):
    print('Total number of players: ', len(players))


def check_player_hand_cards(player: Player):
    print('Player:', player.id, 'Number of cards in hand:', len(player.hand))
    for i in player.hand:
        i.print_card()


def print_atut(g):
    if g.round != g.rounds_total:
        print("Atut this round: ", end='')
        g.atut.print_card()
        print()
    else:
        print("Atut this round: None")
