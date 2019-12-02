class Card:
    def __init__(self):
        pass

    def print_card(self):
        print("[None]", end='')
        pass


class ColoredCard(Card):

    def __init__(self, card_number, card_color):
        super().__init__()
        self.cardColor = card_color
        self.cardNumber = card_number

    def print_card(self):
        print('[', self.cardColor, sep='', end='|')
        print(self.cardNumber, end=']')


class SpecialCard(Card):

    def __init__(self, card_type: str):
        super().__init__()
        self.cardType = card_type

    def print_card(self):
        print('[', self.cardType, sep='', end=']')


def create_all_cards():
    card_deck = create13_colored_cards("red")
    card_deck += create13_colored_cards("blue")
    card_deck += create13_colored_cards("green")
    card_deck += create13_colored_cards("yellow")
    card_deck += create_special_cards()

    return card_deck


def create13_colored_cards(color):
    """Creates a full list of 13 (colored) cards."""
    array = list()
    for i in range(1, 14):
        array.append(ColoredCard(i, color))
    return array


def create_special_cards():
    """Create all 4 special cards"""
    array = list()
    for i in range(0, 4):
        array.append(create_zauberer())
        array.append(create_narr())
    return array


def create_zauberer():
    return SpecialCard('z')


def create_narr():
    return SpecialCard('n')


def input_card(hand: list, ) -> Card:
    """
    Display available Cards
    Prompts player with input request
    Input should be int corresponding to a card from the "hand"
    should return said card
    """
    position_of_handcard = 1
    for i in hand:
        print("Card Nr.:", position_of_handcard, end='')
        i.print_card()
        position_of_handcard += 1
    selected_card = input('What card do you want to play?')
    selected_card_nr = int(selected_card)
    return hand[selected_card_nr]
