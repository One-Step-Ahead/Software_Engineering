from collections import deque

from game.cards import create_all_cards
from game.player import *
from game.round import Round
from game.score_board import ScoreBoard
from game.stich import Stich


class GameBoard:
    def __init__(self, player_total: int, display_mode: bool):
        """
        :param player_total: total ammount of players that are going to play the game
        :param display_mode: True: CLI inputs are on; False: CLI inputs are turned off
        """
        self.players = create_players(player_total)
        self.rounds_total = get_rounds_total(player_total)
        self.card_deck = list()
        self.score_board = ScoreBoard()
        self.current_round_count = 0
        self.player_queue = deque(self.players)
        self.display_mode = display_mode

    def get_current_round(self) -> Round:
        return self.score_board.round_score[self.current_round_count - 1]

    def create_new_round(self):
        self.score_board.round_score.append(Round(self.current_round_count))

    def prepare_players(self):
        for i in self.players:
            i.hand.clear()
            i.stich_score = 0
            i.draw_random_card(self.card_deck, self.current_round_count)

    def reset_card_deck(self):
        self.card_deck.clear()
        self.card_deck = create_all_cards()

    def cycle_player_q(self):
        self.player_queue.append(self.player_queue.popleft())

    def new_round(self):
        self.current_round_count += 1
        self.create_new_round()
        self.reset_card_deck()
        self.prepare_players()
        self.get_current_round().set_new_atut(self.rounds_total,
                                              self.card_deck,
                                              self.player_queue)
        print('New Round! [', self.current_round_count, ']', sep='')
        if self.display_mode:
            print('The Atut for this round is: ')
            self.get_current_round().print_atut(self.rounds_total)
            print()

    def set_stich_queue(self, stich_count: int) -> deque:
        stich_queue = deque(self.player_queue)
        winner = self.get_current_round().stiche[stich_count - 2].winner
        while winner != stich_queue[0]:
            stich_queue.append(stich_queue.popleft())
        return stich_queue

    def get_winner(self) -> Player:
        winner = Player
        for i in self.players:
            if winner is Player:
                winner = i
            if isinstance(i, Player):
                if i.score > winner.score:
                    winner = i
        return winner

    def complete_game(self):
        winner = self.get_winner()
        if winner.name is None:
            print('Winner of the game is:', winner.id + 1)
        else:
            print('Winner of the game is:', winner.name)

    def game_loop(self):
        for i in range(0, self.rounds_total):
            self.new_round()
            for j in self.player_queue:
                self.get_current_round().predict(j)
            for k in range(1, self.current_round_count + 1):
                if k == 1:
                    new_stich = Stich(self.player_queue, self.get_current_round().atut)
                else:
                    new_stich = Stich(self.set_stich_queue(k), self.get_current_round().atut)
                self.get_current_round().stiche.append(new_stich)
                new_stich.play(self.player_queue)
            self.get_current_round().calculate_score(self.players)
            self.cycle_player_q()
        self.complete_game()

    def get_player_names(self):
        for i in self.players:
            if isinstance(i, Player):
                if self.display_mode:
                    i.set_name()

    def start(self):
        self.get_player_names()
        self.game_loop()


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


def create_players(total_player_number: int) -> list:
    players = []
    for i in range(0, total_player_number):
        players.append(Player(i))
    return players
