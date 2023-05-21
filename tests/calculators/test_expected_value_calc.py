from decimal import Decimal
import pytest
import numpy as np
from sportsbooklib.calculators.exceptions import InvalidNumberOfInputsException, InvalidTargetLegException, \
    NegativeImpliedProbabilityException

from sportsbooklib.calculators.expected_value_calc import get_expected_value, Odds, get_expected_value_for_legs
from sportsbooklib.calculators.expected_value_calc import get_expected_value_for_selections
from sportsbooklib.models.odds.enums import OddsFormat
from sportsbooklib.models.selection import Selection


def test_get_expected_value_positive_odds():
    odds = Odds(150, OddsFormat.US)
    implied_probability = Decimal('0.6')
    expected_value = Decimal('50.000')
    np.testing.assert_equal(get_expected_value(
        implied_probability, odds), expected_value)


def test_get_expected_value_negative_odds():
    odds = Odds(-200, OddsFormat.US)
    implied_probability = Decimal('0.5')
    expected_value = Decimal('-25.000')
    np.testing.assert_equal(get_expected_value(
        implied_probability, odds), expected_value)


def test_get_expected_value_large_odds():
    odds = Odds(10000, OddsFormat.US)
    implied_probability = Decimal('0.3')
    expected_value = Decimal('2930.000')
    np.testing.assert_equal(get_expected_value(
        implied_probability, odds), expected_value)


def test_get_expected_value_negative_implied_probability():
    odds = Odds(300, OddsFormat.US)
    implied_probability = Decimal('-0.1')
    with pytest.raises(NegativeImpliedProbabilityException):
        get_expected_value(implied_probability, odds)


def test_get_expected_value_for_legs_empty_leg():
    odds = Odds(150, OddsFormat.US)
    legs = []
    with pytest.raises(InvalidNumberOfInputsException):
        get_expected_value_for_legs(legs, odds)


def test_get_expected_value_for_legs_one_leg():
    odds = Odds(150, OddsFormat.US)
    legs = [
        Odds(-110, OddsFormat.US)
    ]
    with pytest.raises(InvalidNumberOfInputsException):
        get_expected_value_for_legs(legs, odds)


def test_get_expected_value_for_two_legs():
    final_odds = Odds(150, OddsFormat.US)
    legs = [
        Odds(-130, OddsFormat.US),
        Odds(110, OddsFormat.US)
    ]
    expected_value = Decimal('35.694')
    np.testing.assert_equal(get_expected_value_for_legs(
        legs, final_odds), expected_value)


def test_get_expected_value_for_three_legs():
    final_odds = Odds(700, OddsFormat.US)
    legs = [
        Odds(600, OddsFormat.US),
        Odds(425, OddsFormat.US),
        Odds(-250, OddsFormat.US)
    ]
    expected_value = Decimal('9.091')
    np.testing.assert_equal(get_expected_value_for_legs(
        legs, final_odds), expected_value)


def test_get_expected_value_invalid_target_leg_negative():
    final_odds = Odds(150, OddsFormat.US)
    legs = [
        Odds(-130, OddsFormat.US),
        Odds(110, OddsFormat.US)
    ]
    with pytest.raises(InvalidTargetLegException):
        get_expected_value_for_legs(legs, final_odds, -1)


def test_get_expected_value_invalid_target_leg_too_large():
    final_odds = Odds(150, OddsFormat.US)
    legs = [
        Odds(-130, OddsFormat.US),
        Odds(110, OddsFormat.US)
    ]
    with pytest.raises(InvalidTargetLegException):
        get_expected_value_for_legs(legs, final_odds, 2)


def test_get_expected_value_for_two_legs_second_target_leg():
    final_odds = Odds(-400, OddsFormat.US)
    legs = [
        Odds(280, OddsFormat.US),
        Odds(-435, OddsFormat.US)
    ]
    expected_value = Decimal('-5.567')
    np.testing.assert_equal(get_expected_value_for_legs(
        legs, final_odds, 1), expected_value)


def test_get_expected_value_for_two_selections():
    final_odds = Odds(150, OddsFormat.US)
    selections = [
        Selection('item1', Odds(-130, OddsFormat.US)),
        Selection('item2', Odds(110, OddsFormat.US))
    ]
    expected_value = Decimal('35.694')
    np.testing.assert_equal(get_expected_value_for_selections(
        selections, final_odds), expected_value)
