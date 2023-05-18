from decimal import Decimal
from itertools import combinations
from math import prod
from typing import List, Mapping, Union
from sportsbooklib.models.exceptions import InvalidSelectionsInputException
from sportsbooklib.models.odds.enums import OddsFormat
from sportsbooklib.models.odds.odds import Odds

from sportsbooklib.models.selection.selection import Selection


def generate_combinations(n):
    numbers = list(range(n))
    combos = []

    for r in range(2, n + 1):
        combos.extend(combinations(numbers, r))

    return combos


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
    indices_combinations = list(generate_combinations(n))
    total_risk = stake * len(indices_combinations)
    max_win = 0
    max_odds = 0
    for combo in indices_combinations:
        legs = len(combo)
        total_odds = prod(map(lambda x: selections[x].odds.eu_odds, combo))
        win = stake * total_odds - (stake * (n-legs))
        if win > max_win:
            max_odds = Odds(total_odds, OddsFormat.EU)
            max_win = win
        res.append({'legs': legs, 'total_risk': total_risk,
                    'total_odds': max_odds, 'max_win': max_win})
    return res
