from random import choice  # Joyce

from game.cards import SpecialCard, Card


class Player:

    def __init__(self, player_number):
        self.id = player_number
        self.score = int(0)
        self.hand = list()
        self.stich_score = int

    def draw_random_card(self, card_deck: list, amount=1):
        for i in range(0, amount):
            selected_card = choice(card_deck)
            self.hand.append(selected_card)
            card_deck.remove(selected_card)

    def play_card(self, card: Card, played_cards: list):
        """
        Adds the played card to the played_card list.
        Also removes the played card from the players hand.
        """
        played_cards.append(card)
        self.hand.remove(card)

    def get_number_of_special_cards(self):
        """Returns the number of special cards in the hand of the Player"""

        cards = 0
        for i in self.hand:
            if isinstance(i, SpecialCard):
                cards += 1
        return cards
