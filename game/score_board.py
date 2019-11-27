class ScoreBoard:
    """
    total_score = Liste mit allen round scores/Endergebnissen aller Runden.
    round_score = Anzahl angesagter Stiche/gemachter Stiche einer spezifischen runde + ausgespielter Karten.
    """

    def __init__(self):
        self.total_score = list()  # liste mit allen round scores/endergebnissen aller runden
        self.round_score = list()  # anzahl angesagter sticht/gemachter stiche einer spezifischen runde
