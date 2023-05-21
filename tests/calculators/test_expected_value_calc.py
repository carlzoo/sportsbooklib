from decimal import Decimal
import pytest
import numpy as np
from sportsbooklib.calculators.exceptions import NegativeImpliedProbabilityException

from sportsbooklib.calculators.expected_value_calc import get_expected_value, Odds
from sportsbooklib.models.odds.enums import OddsFormat


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
