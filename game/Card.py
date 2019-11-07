from game import CardColor


class Card:
    pass


class ColoredCard(Card):

    def __init__(self, card_number, card_color):
        self.cardColor = card_color
        self.cardNumber = card_number


class SpecialCard(Card):

    def __init__(self, card_type):
        self.cardType = card_type
