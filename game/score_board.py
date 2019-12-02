class ScoreBoard:
    """
    total_score = Liste mit allen round scores/Endergebnissen aller Runden.
    round_score = Anzahl angesagter Stiche/gemachter Stiche einer spezifischen runde + ausgespielter Karten.

    +20pkt f. richtige Vorhersage
    -10pkt f. jede abweichende Vorhersage
    +10pkt f. jeden gemachtden Stich

    """

    def __init__(self):
        self.total_score = list()  # liste mit allen round scores/endergebnissen aller runden
        self.round_score = list()  # anzahl angesagter sticht/gemachter stiche einer spezifischen runde

    def winner(self, player):
        """
        soll am ende des spiels ausgeben wer gewonnen hat
        :return:
        """
        print('congratz', player, 'you won')
