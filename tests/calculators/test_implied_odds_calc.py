from decimal import Decimal
import numpy as np
import pytest

from sportsbooklib.calculators.exceptions import InvalidNumberOfInputsException
from sportsbooklib.calculators.implied_odds_calc import get_implied_probability
from sportsbooklib.models.odds.enums import OddsFormat
from sportsbooklib.models.odds import Odds


def test_invalid_input_empty_list():
    with pytest.raises(InvalidNumberOfInputsException):
        get_implied_probability([])


def test_invalid_list_1_item():
    with pytest.raises(InvalidNumberOfInputsException):
        get_implied_probability([Odds(-110, OddsFormat.US)])


def test_2_odds_equal():
    res = get_implied_probability([
        Odds(-110, OddsFormat.US), Odds(-110, OddsFormat.US)])
    np.testing.assert_almost_equal(
        res['implied_probability'], [Decimal('0.5238'), Decimal('0.5238')], decimal=4)
    np.testing.assert_almost_equal(
        res['fair_odds'], [Decimal('0.5'), Decimal('0.5')], decimal=4)


def test_2_odds_unequal():
    res = get_implied_probability([
        Odds(-120, OddsFormat.US), Odds(100, OddsFormat.US)])
    np.testing.assert_almost_equal(
        res['implied_probability'], [Decimal('0.5455'), Decimal('0.5')], decimal=4)
    np.testing.assert_almost_equal(
        res['fair_odds'], [Decimal('0.5217'), Decimal('0.4782')], decimal=4)


def test_3_odds():
    res = get_implied_probability([
        Odds(262, OddsFormat.US), Odds(340, OddsFormat.US), Odds(262, OddsFormat.US)])
    np.testing.assert_almost_equal(
        res['implied_probability'], [Decimal('0.2762'), Decimal('0.2272'), Decimal('0.2762')], decimal=4)
    np.testing.assert_almost_equal(
        res['fair_odds'], [Decimal('0.3542'), Decimal('0.2914'), Decimal('0.3542')], decimal=4)
