class Card:
    pass


class ColoredCard(Card):

    def __init__(self, card_number, card_color):
        self.cardColor = card_color
        self.cardNumber = card_number


class SpecialCard(Card):

    def __init__(self, card_type):
        self.cardType = card_type


def create_all_cards():
    card_deck = create13_colored_cards("red")
    card_deck += create13_colored_cards("blue")
    card_deck += create13_colored_cards("green")
    card_deck += create13_colored_cards("yellow")
    card_deck += create_special_cards()


    return card_deck


def create13_colored_cards(color):
    """Creates a full list of 13 (colored) cards."""
    array = []
    for i in range(1, 14):
        array.append(ColoredCard(i, color))
    return array


def create_special_cards():
    """Create all 4 special cards"""
    array = []
    for i in range(0, 4):
        array.append(create_zauberer())
        array.append(create_narr())
    return array


def create_zauberer():
    return SpecialCard('z')


def create_narr():
    return SpecialCard('n')
