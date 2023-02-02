from decimal import Decimal
from typing import List
from sportsbooklib.models.selection.selection import Selection
from sportsbooklib.models.odds.odds import Odds


def get_hold(odds: List[Odds]) -> Decimal:
    return sum([x.implied_odds for x in odds]) - Decimal(1)


def get_hold_for_selections(selections: List[Selection]) -> Decimal:
    return get_hold([selection.odds for selection in selections])
