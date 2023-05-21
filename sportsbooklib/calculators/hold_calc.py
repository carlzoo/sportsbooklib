from decimal import Decimal
from typing import List
from sportsbooklib.calculators.implied_odds_calc import get_implied_probability
from sportsbooklib.models.selection import Selection
from sportsbooklib.models.odds import Odds


def get_hold(odds: List[Odds]) -> Decimal:
    """

    Calculate hold, given list of Odds, where length of list > 1

    Parameters
    ----------
    odds : List[Odds]
        List of odds to calculate hold

    Returns
    -------
    Decimal
        The hold value as a Decimal
    """
    implied_odds_result = get_implied_probability(odds)
    return sum(implied_odds_result['implied_probability']) - Decimal(1)


def get_hold_for_selections(selections: List[Selection]) -> Decimal:
    """
    Calculate hold, given list of Selection's odds, where length of list > 1

    Parameters
    ----------
    odds : List[Selection]
        List of Selection to calculate hold

    Returns
    -------
    Decimal
        The hold value as a Decimal
    """
    return get_hold([selection.odds for selection in selections])
