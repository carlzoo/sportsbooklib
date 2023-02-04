from decimal import Decimal
from typing import List
from sportsbooklib.calculators.implied_odds_calc import get_implied_probability
from sportsbooklib.models.selection.selection import Selection
from sportsbooklib.models.odds.odds import Odds


def get_hold(odds: List[Odds]) -> Decimal:
    implied_odds_result = get_implied_probability(odds)
    return sum(implied_odds_result['implied_probability']) - Decimal(1)


def get_hold_for_selections(selections: List[Selection]) -> Decimal:
    return get_hold([selection.odds for selection in selections])
