from decimal import Decimal
from typing import List
from sportsbooklib.calculators.implied_odds_calc import get_implied_probability

from sportsbooklib.models.odds.odds import Odds


def get_expected_value_for_legs(leg_odds: List[Odds], final_odds: Odds, target_leg: int = 0) -> Decimal:
    implied_fair_odds = get_implied_probability(leg_odds)
    return get_expected_value(implied_fair_odds['implied_probability'][target_leg], final_odds)


def get_expected_value(implied_probability: Decimal, final_odds: Odds) -> Decimal:
    implied_loss_probabilty = 1 - implied_probability
    amount_won = final_odds.us_odds if final_odds.us_odds > 0 else (
        100 / (-1 * final_odds.us_odds)) * 100
    return round((implied_probability * amount_won) - implied_loss_probabilty * 100, 3)
