from collections import deque

from game.cards import input_card, ColoredCard
from game.game_board import Player, Card, SpecialCard


class Stich:
    def __init__(self, player_q: deque, atut: ColoredCard):
        self.player_q = player_q
        self.cards_in_play = list()
        self.winner = Player
        self.atut = atut

    def farbzwang_check(self, card_about_to_be_played: Card) -> bool:
        """
        :return True if card matches playable "Farbzwang" conditions
        """
        first_played_card = self.cards_in_play[0]

        if isinstance(card_about_to_be_played, SpecialCard):
            return True
        elif isinstance(card_about_to_be_played, ColoredCard) and isinstance(first_played_card, ColoredCard):
            if card_about_to_be_played.card_color == first_played_card.card_color:
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

    def get_player(self, player_number: int):
        return self.player_q[player_number]

    def check_wizard_win(self):
        player_number = 0
        for i in self.cards_in_play:
            if isinstance(i, SpecialCard):
                if i.cardType == 'z':
                    self.winner = self.get_player(player_number)
                    return True
            player_number += 1
        return False

    def compare_cards(self, card1: ColoredCard, card2: ColoredCard):
        if card1.card_value > card2.card_value:
            return card1
        else:
            return card2

    def check_colored_win(self):
        """
        This method checks for:
            Atut
            if Farbzwang got satisfied
            if there are only Narren being played
        """
        dominant_color = None
        for i in self.cards_in_play:
            if isinstance(i, SpecialCard):
                continue
            elif isinstance(i, ColoredCard):
                dominant_color = i.card_color
                break

        strongest_card = None
        for i in self.cards_in_play:
            if isinstance(i, ColoredCard):
                if strongest_card is None:
                    strongest_card = i
                    continue
                elif strongest_card.card_color == self.atut.card_color and i.card_color != self.atut.card_color:
                    continue
                elif i.card_color == self.atut.card_color:
                    if strongest_card.card_color != self.atut.card_color:
                        strongest_card = i
                        continue
                    else:
                        if strongest_card.card_value < i.card_value:
                            strongest_card = i
                            continue
                        else:
                            continue
                else:
                    if strongest_card.card_value < i.card_value:
                        strongest_card = i
                        continue
                    else:
                        continue
        if strongest_card is None:
            self.winner = self.get_player(0)
            return True
        self.winner = self.get_player(self.cards_in_play.index(strongest_card))
        return True

    def check_stich_winner(self) -> type(Player):
        """
        :return: Player that won the Stich
        """
        if self.check_wizard_win():
            return self.winner
        if self.check_colored_win():
            return self.winner
        else:
            raise RuntimeError('The system was not able to find a card that won the Stich! Please fix me!')

    def play(self, player_queue: deque):
        """
        Execute the Stich.
        """
        correct_input = bool
        chosen_card = Card

        for i in player_queue:
            print("It is now the turn of Player:", i.id)
            while correct_input:
                chosen_card = input_card(i.hand)
                if self.check_if_playable(chosen_card, i):
                    correct_input = False
                else:
                    print('You are not allowed to play this card right now!')
            i.play_card(chosen_card, player_queue)
        self.check_stich_winner()
