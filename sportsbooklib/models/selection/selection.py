from sportsbooklib.models.odds.odds import Odds


class Selection:
    """

    The Selection Object.

    Attributes
    ----------
    name : str
        Name of the selection.
    odds : Odds
        The Odds object associated with the selection.
    """

    def __init__(self, name: str, odds: Odds):
        self.name = name
        self.odds = odds
