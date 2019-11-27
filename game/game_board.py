from game.cards import create_all_cards
from game.player import *
from game.round import Round
from game.score_board import ScoreBoard


class GameBoardMeta(type):
    _instance = None

    def __call__(cls, player_total):
        if cls._instance is None:
            cls._instance = super().__call__(player_total)
        return cls._instance


class GameBoard(metaclass=GameBoardMeta):

    def __init__(self, player_total: int):
        self.players = create_players(player_total)
        self.rounds_total = get_rounds_total(player_total)
        self.card_deck = list()
        self.score_board = ScoreBoard()
        self.actual_round_count = 0
        self.round = Round

    def new_round(self):
        # Reihenfolge ist wichtig!
        self.actual_round_count += 1
        self.score_board.rounds.append(Round(self.actual_round_count))
        self.reset_card_deck()
        self.prepare_players()
        self.set_new_atut(self.rounds_total, self.card_deck)
        print('New Round! [', self.actual_round_count, ']', sep='')

    def prepare_players(self):
        for i in self.players:
            i.hand.clear()
            i.stich_score = 0
            i.draw_card(self.card_deck, self.actual_round_count)

    def reset_card_deck(self):
        self.card_deck.clear()
        self.card_deck = create_all_cards()

    def game_loop(self):
        self.new_round()
        self.score_board.make_prediction(self.round.current_player, 1)

    def set_new_atut(self, rounds_total: int, card_deck: list):
        if self.actual_round_count != rounds_total:
            self.round.atut = choice(card_deck)
        else:
            self.round.atut = Card()


def create_players(total_player_number):
    players = []
    for i in range(0, total_player_number):
        players.append(Player(i))
    return players


def get_rounds_total(total_player_number: int) -> int:
    if total_player_number == 3:
        return 20
    if total_player_number == 4:
        return 15
    if total_player_number == 5:
        return 12
    if total_player_number == 6:
        return 10
    else:
        raise ValueError("PlayerCount needs to be between 3-6!")
