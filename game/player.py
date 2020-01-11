from random import choice, randint  # Joyce

from game.cards import Card


class Player:
    names = ['Sebastian',
             'Johannes',
             'Gerald',
             'Max',
             'Moritz',
             'Lisa',
             'Katharina',
             'Sandra',
             'Verena',
             'Sabrina']

    def __init__(self, player_number: int, name=None):
        self.number = player_number + 1
        self.score = int(0)
        self.hand = list()
        self.name = name

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

    def set_name(self, name='player'):
        if name == 'player':
            print('Enter Player name for Player', self.number + 1, ':')
            name = input()
        self.name = name

    def set_random_name(self):
        self.name = Player.names.pop(randint(0, (len(Player.names) - 1)))
        from game.game_board import GameBoard
        if GameBoard.display_mode:
            print("Player ", self.number, " is now named ", self.name)