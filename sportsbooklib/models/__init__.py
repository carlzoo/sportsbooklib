"""
The models submodule.
"""


from decimal import Decimal
from typing import List
from sportsbooklib.calculators.parlay_calc import get_round_robin_payout
from sportsbooklib.models.selection.selection import Selection


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
    """

    def __init__(self, selections: List[Selection], stake: Decimal):
        self.selections = selections
        self.stake = stake

        self.round_robin_payout = get_round_robin_payout(
            self.stake, self.selections)
