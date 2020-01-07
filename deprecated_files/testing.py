from game.game_board import GameBoard
from game.player import Player


def test(g: GameBoard):
    test_number_of_players(g.players)

    g.game_loop()

    # for i in range(0, g.rounds_total):
    #     g.new_round()
    #     print_atut(g)
    #     test_print_players_cards(g.players)


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


def print_atut(g: GameBoard):
    if g.get_current_round().atut is None:
        print("Atut this round: None")
    elif g.get_current_round() != g.rounds_total:
        print("Atut this round: ", end='')
        g.get_current_round().atut.print_card()
        print()


def make_prediction_test(g: GameBoard):
    g.score_board.make_prediction(g.players[0], 5)


if __name__ == '__main__':
    raise DeprecationWarning
