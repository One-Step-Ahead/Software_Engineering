from game.cards import ColoredCard
from game.cards import input_card
from game.game_board import *


def play_card(player: Player, played_card: Card):
    player.hand.remove(played_card)


def check_if_playable(chosen_card: Card, cards_in_play: list, player_hand: list) -> bool:
    """
    Checks if the card you are about to play is legit.

    :param player_hand: All cards that the player has in his' hand.
    :param chosen_card: Card you are about to play.
    :param cards_in_play: The cards that have been played / are on the board.
    :return:
    """
    if len(cards_in_play) == 0:
        return True
    elif type(chosen_card) is type(SpecialCard):
        return True
    elif cant_serve(cards_in_play, player_hand):
        return True
    elif farbzwang_check(chosen_card, cards_in_play):
        return True
    else:
        return False


def farbzwang_check(card_about_to_be_played: Card, cards_in_play: list) -> bool:
    """
    :return True if card matches playable "Farbzwang" conditions
    """
    first_played_card = cards_in_play[0]

    if isinstance(card_about_to_be_played, SpecialCard):
        return True
    elif isinstance(card_about_to_be_played, ColoredCard) and isinstance(first_played_card, ColoredCard):
        if card_about_to_be_played.cardColor == first_played_card.cardColor:
            return True
    else:
        return False


def cant_serve(cards_in_play: list, player_hand: list):
    """
    If the player has no cards that allow him to serve the color on the board :return True.
    """
    for i in player_hand:
        if farbzwang_check(i, cards_in_play):
            return False
    return True


def play_round(gameboard):
    allowed = bool
    chosen_card = Card
    for i in gameboard.player_queue:
        print("It is now the turn of Player:", i.id)
        while allowed:
            chosen_card = input_card()
            if check_if_playable(chosen_card, gameboard.round.cards_in_play, i.hand):
                allowed = False
            else:
                print('You are not allowed to play this card right now!')
        i.play_card(chosen_card, i.hand)
