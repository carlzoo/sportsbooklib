from decimal import Decimal
import numpy as np
import pytest

from sportsbooklib.calculators.arbitrage_calc import get_arbitrage
from sportsbooklib.calculators.exceptions import NegativeStakeInputException
from sportsbooklib.models.odds.enums import OddsFormat
from sportsbooklib.models.odds.odds import Odds


def test_negative_stake():
    odds = [
        Odds(Decimal('1.18'), OddsFormat.EU),
        Odds(Decimal('7.00'), OddsFormat.EU)
    ]
    with pytest.raises(NegativeStakeInputException):
        get_arbitrage(
            Decimal('-500'), odds)


def test_arbitrage_calc_2_way():
    odds = [
        Odds(Decimal('1.18'), OddsFormat.EU),
        Odds(Decimal('7.00'), OddsFormat.EU)
    ]
    result = get_arbitrage(
        Decimal('500'), odds)
    np.testing.assert_almost_equal(
        result['stakes'], [Decimal('427.8728'), Decimal('72.1271')], decimal=4)
    np.testing.assert_almost_equal(
        result['profit'], [Decimal('4.89')], decimal=4)


def test_arbitrage_calc_3_way():
    odds = [
        Odds(-435, OddsFormat.US),
        Odds(840, OddsFormat.US),
        Odds(3400, OddsFormat.US),
    ]
    result = get_arbitrage(
        Decimal('363.22'), odds)
    np.testing.assert_almost_equal(
        result['stakes'], [Decimal('311.5110'), Decimal('40.7615'), Decimal('10.9473')], decimal=4)
    np.testing.assert_almost_equal(
        result['profit'], [Decimal('19.9386')], decimal=4)


def test_arbitrage_negative_profit():
    odds = [
        Odds(-110, OddsFormat.US),
        Odds(-110, OddsFormat.US)
    ]
    result = get_arbitrage(
        Decimal('110'), odds)
    np.testing.assert_almost_equal(
        result['stakes'], [Decimal('54.9999'), Decimal('54.9999')], decimal=4)
    np.testing.assert_almost_equal(
        result['profit'], [Decimal('-5.005')], decimal=4)
