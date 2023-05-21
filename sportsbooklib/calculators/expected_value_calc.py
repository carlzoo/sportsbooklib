from decimal import Decimal
from typing import List
from sportsbooklib.calculators.exceptions import *
from sportsbooklib.calculators.implied_odds_calc import get_implied_probability

from sportsbooklib.models.odds import Odds
from sportsbooklib.models.selection import Selection


def get_expected_value_for_legs(leg_odds: List[Odds], final_odds: Odds, target_leg: int = 0) -> Decimal:
    """
    Calculate the expected value of a bet for the target_leg index in leg_odds.

    Args:
        leg_odds (List[Odds]): List of odds for the legs.
        final_odds (Odds): The final odds of the bet.
        target_leg (int): The index in leg_odds to use. Default is 0.

    Raises:
        InvalidTargetLegException
        InvalidNumberOfInputsException

    Returns:
        Decimal: The expected value of the bet.
    """

    if len(leg_odds) < 2:
        raise InvalidNumberOfInputsException

    if target_leg < 0 or target_leg >= len(leg_odds):
        raise InvalidTargetLegException

    implied_fair_odds = get_implied_probability(leg_odds)
    return get_expected_value(implied_fair_odds['fair_odds'][target_leg], final_odds)


def get_expected_value_for_selections(selections: List[Selection], final_odds: Odds, target_leg: int = 0) -> Decimal:
    """
    Calculate the expected value of a bet for the target_leg index in selections.
    Selection Wrapper for get_expected_value_for_legs

    Args:
        selections (List[Selection]): List of selections.
        final_odds (Odds): The final odds of the bet.
        target_leg (int): The index in leg_odds to use. Default is 0.

    Returns:
        Decimal: The expected value of the bet.
    """
    return get_expected_value_for_legs(list(map(lambda x: x.odds, selections)), final_odds, target_leg)


def get_expected_value(implied_probability: Decimal, final_odds: Odds) -> Decimal:
    """
    Calculate the expected value of a bet.

    Args:
        implied_probability (Decimal): The implied probability of winning the bet.
        final_odds (Odds): The final odds of the bet.

    Raises:
        NegativeImpliedProbabilityException

    Returns:
        Decimal: The expected value of the bet.
    """
    if implied_probability < 0:
        raise NegativeImpliedProbabilityException

    implied_loss_probabilty = 1 - implied_probability
    amount_won = final_odds.us_odds if final_odds.us_odds > 0 else (
        Decimal(100 / (-1 * final_odds.us_odds)) * 100)
    return round((implied_probability * amount_won) - implied_loss_probabilty * 100, 3)
