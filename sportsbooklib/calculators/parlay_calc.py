from decimal import Decimal
from itertools import combinations
from math import prod
from typing import List, Mapping, Union
from sportsbooklib.models.exceptions import InvalidSelectionsInputException
from sportsbooklib.models.odds.enums import OddsFormat
from sportsbooklib.models.odds.odds import Odds

from sportsbooklib.models.selection.selection import Selection


def get_round_robin_payout(stake: Decimal, selections: List[Selection]) -> List[Mapping[str, Union[Decimal, int]]]:
    """
    Given stake and list of n odds, calculate all round robins from 2 to n, n>=2,max win and total risk for each combo

    Parameters
    ----------
    stake : Decimal
        stake to risk per leg.
    selections : List[Selection]
        List of selections to compute

    Returns
    -------
    Dict:
        <legs> int: Number of legs in round robin
        <total_risk> Decimal: Total amount risked
        <max_win> Decimal: Max win for n legs of round robin
    """
    n = len(selections)
    # base cases
    if n < 2:
        raise InvalidSelectionsInputException

    res = []
    indices = [i for i in range(1, n)]
    for r in range(1, n+1):
        indices_combinations = list(combinations(indices, r))
        total_risk = stake * len(indices_combinations)
        max_win = 0
        for combo in indices_combinations:
            win = stake * \
                prod(map(lambda x: x.odds.eu_odds, combo)) - \
                stake * (n-r)
            max_win = max(max_win, win)
        res.append(
            {'legs': r, 'total_risk': total_risk, 'max_win': max_win})
    return res


def get_parlay_payout(stake: Decimal, selections: List[Selection]) -> Mapping[str, Union[Odds, Decimal]]:
    """
    Given stake and list of n odds, calculate total odds and payout for parlay

    Parameters
    ----------
    stake : Decimal
        stake to risk per leg.
    selections : List[Selection]
        List of selections to compute

    Returns
    -------
    Dict:
        <odds> Odds: Total combined odds
        <amount> Decimal: Total payout
    """
    parlay_odds = prod(map(lambda x: x.odds.eu_odds, selections))
    return {'odds': Odds(parlay_odds, OddsFormat.EU), 'amount': stake * parlay_odds}
