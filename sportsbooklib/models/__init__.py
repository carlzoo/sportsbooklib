"""
The models submodule.
"""


from decimal import Decimal
from typing import List, Mapping, Union
from sportsbooklib.calculators.parlay_calc import get_parlay_payout, get_round_robin_payout
from sportsbooklib.models.exceptions import InvalidSelectionsInputException
from sportsbooklib.models.odds.enums import OddsFormat
from sportsbooklib.models.odds.odds import Odds
from sportsbooklib.models.selection.selection import Selection
from math import prod
from itertools import combinations


class Ticket:
    """
    The Ticket Object which represents the betslip.

    Attributes
    ----------
    selections : List[Selection]
        List of Selection for the betslip
    stake : Decimal
        The stake for the betslip
    round_robin_payout: List[Mapping[str, Union[Decimal, int]]]
        List of possible round robin wins and combinations
    parlay_payout: 
        The payout for all selections parlayed together
    """

    def __init__(self, selections: List[Selection], stake: Decimal):
        self.selections = selections
        self.stake = stake

        self.round_robin_payout = get_round_robin_payout(
            self.stake, self.selections)
        self.parlay_payout = get_parlay_payout(self.stake, self.selections)
