from game import Card


def init():
    createAllCards()


def createAllCards():
    allCards = create13Cards("red")
    allCards += create13Cards("blue")
    allCards += create13Cards("green")
    allCards += create13Cards("yellow")


def create13Cards(color):
    array = []

    for i in range(1, 13):
        array.append(Card.ColoredCard(i, color))

    return array
