from random import choice

from game.cards import SpecialCard


class Player:

    def __init__(self, player_number):
        self.id = player_number
        self.score = 0
        self.hand = []
        self.stich_score = int

    def draw_card(self, card_deck: list, amount=1):
        for i in range(0, amount):
            selected_card = choice(card_deck)
            self.hand.append(selected_card)
            card_deck.remove(selected_card)

    def play_card(self):
        pass

    def get_number_of_special_cards(self):
        cards = 0
        for i in self.hand:
            if isinstance(i, SpecialCard):
                cards += 1
        return cards
