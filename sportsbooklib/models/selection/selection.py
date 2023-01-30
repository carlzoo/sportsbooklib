from sportsbooklib.models.odds.odds import Odds


class Selection:
    def __init__(self, name: str, odds: Odds):
        self.name = name
        self.odds = odds
