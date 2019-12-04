from collections import deque

from game.cards import input_card, ColoredCard
from game.game_board import Player, Card, SpecialCard


class Stich:
    def __init__(self, player_q: deque):
        self.player_q = player_q
        self.cards_in_play = list()
        self.winner = Player

    def farbzwang_check(self, card_about_to_be_played: Card) -> bool:
        """
        :return True if card matches playable "Farbzwang" conditions
        """
        first_played_card = self.cards_in_play[0]

        if isinstance(card_about_to_be_played, SpecialCard):
            return True
        elif isinstance(card_about_to_be_played, ColoredCard) and isinstance(first_played_card, ColoredCard):
            if card_about_to_be_played.cardColor == first_played_card.cardColor:
                return True
        else:
            return False

    def cant_serve(self, player: Player):
        """
        If the player has no cards that allow him to serve the color on the board :return True.
        """
        for i in player.hand:
            if self.farbzwang_check(i):
                return False
        return True

    def check_wizzad_win(self):
        for i in self.cards_in_play:
            if isinstance(i, SpecialCard):
                if i.cardType == 'z':
                    return True
            else:
                return False

    def check_if_playable(self, chosen_card: Card, player: Player) -> bool:
        """
        Checks if the card you are about to play is legit.
        :param player: The Player that wants to play the chosen_card.
        :param chosen_card: Card you are about to play.
        :return:
        """
        if len(self.cards_in_play) == 0:
            return True
        elif type(chosen_card) is type(SpecialCard):
            return True
        elif self.cant_serve(player):
            return True
        elif self.farbzwang_check(chosen_card):
            return True
        else:
            return False

    def get_player(self, player_number: int, player_q: list):
        return player_q[player_number]

    def check_stich_winner(self) -> type(Player):
        """
        :return: Player that won the Stich
        """

        if self.check_wizzad_win():
            return self.winner

    def play(self, player_queue: deque):
        """
        Execute the Stich!
        """
        allowed = bool
        chosen_card = Card

        for i in player_queue:
            print("It is now the turn of Player:", i.id)
            while allowed:
                chosen_card = input_card(i.hand)
                if self.check_if_playable(chosen_card, i):
                    allowed = False
                else:
                    print('You are not allowed to play this card right now!')
            i.play_card(chosen_card, player_queue)
        self.check_stich_winner()
