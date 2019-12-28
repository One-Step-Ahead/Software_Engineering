class Card:
    def __init__(self):
        pass

    def print_card(self):
        print("[None]", end='')
        pass


class ColoredCard(Card):

    def __init__(self, card_number: int, card_color: str):
        super().__init__()
        self.card_color = card_color
        self.card_value = card_number

    def print_card(self):
        print('[', self.card_color, sep='', end='|')
        print(self.card_value, end=']')


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


def input_card(hand: list) -> Card:
    """
    Display available Cards
    Prompts player with input request
    Input should be int corresponding to a card from the "hand"
    should return said card
    """
    position_of_handcard = 1
    for i in hand:
        print("Card", position_of_handcard, end='')
        i.print_card()
        print(end='  ')
        position_of_handcard += 1
    while True:
        try:
            selected_card = input('What card do you want to play?')
            if int(selected_card) < 0:
                raise ValueError
            break
        except ValueError:
            print('Pleas enter a Number that is greater than 0 (e.g. 1)')
        except IndexError:
            print('You dont have that many cards')
    selected_card_nr = int(selected_card) - 1
    return hand[selected_card_nr]
