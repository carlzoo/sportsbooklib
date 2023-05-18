from decimal import Decimal
from math import prod
from typing import List, Mapping, Union
from sportsbooklib.models.exceptions import InvalidSelectionsInputException
from sportsbooklib.models.odds.enums import OddsFormat
from sportsbooklib.models.odds.odds import Odds

from sportsbooklib.models.selection.selection import Selection


def get_parlay_payout(stake: Decimal, selections: List[Selection]) -> List[Mapping[str, Union[Decimal, Odds]]]:
    """
    Given stake and list of n odds, calculate combined odds and return

    Parameters
    ----------
    stake : Decimal
        stake to risk
    selections : List[Selection]
        List of selections to compute

    Returns
    -------
    Dict:
        <odds> Odds: Total odds of the parlay
        <win> Decimal: Total amount won
    """
    n = len(selections)
    # base cases
    if n < 2:
        raise InvalidSelectionsInputException

    odds_value = Decimal(prod(map(lambda x: x.odds.eu_odds, selections)))
    odds = Odds(
        odds_value, OddsFormat.EU)
    win = stake * odds.eu_odds
    return {'odds': odds, 'return': win}
