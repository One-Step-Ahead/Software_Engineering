from game.cards import create_all_cards
from game.player import create_players
from game.testing import test_print_cards, test_print_players


def init():
    card_deck = create_all_cards()
    players = create_players()
    test_print_cards(card_deck)
    test_print_players(players)

    players[0].draw_card(card_deck)
    test_print_players(players)


init()
