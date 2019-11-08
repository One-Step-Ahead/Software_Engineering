from random import choice


class Player:
    total_player_number = 4

    def __init__(self, player_number):
        self.id = player_number
        self.score = 0
        self.hand = []
        self.stich_score = int

    def draw_card(self, card_deck: list):
        selected_card = choice(card_deck)
        self.hand.append(selected_card)
        card_deck.remove(selected_card)

    def play_card(self, ):
        pass


def create_players():
    players = []
    for i in range(0, Player.total_player_number):
        players.append(Player(i))
    return players
