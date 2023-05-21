import numpy as np
import pytest
from sportsbooklib.calculators.parlay_calc import get_parlay_payout
from decimal import Decimal

from sportsbooklib.models.exceptions import InvalidSelectionsInputException
from sportsbooklib.models.odds.enums import OddsFormat
from sportsbooklib.models.odds import Odds
from sportsbooklib.models.selection import Selection


def test_invalid_empty_selections():
    with pytest.raises(InvalidSelectionsInputException):
        get_parlay_payout(Decimal('1.00'), [])


def test_invalid_one_selections():
    selections = [Selection("item", Odds('1.50', OddsFormat.EU))]
    with pytest.raises(InvalidSelectionsInputException):
        get_parlay_payout(
            Decimal('1.00'), selections)


def test_two_selections():
    selections = [Selection("item1", Odds('1.50', OddsFormat.EU)), Selection(
        "item2", Odds('2.50', OddsFormat.EU))]
    result = get_parlay_payout(Decimal(2.00), selections)
    np.testing.assert_equal(
        result['odds'].eu_odds, Decimal('3.75'))
    np.testing.assert_equal(
        result['return'], Decimal('7.50'))


def test_three_selections():
    selections = [Selection("item1", Odds(-200, OddsFormat.US)), Selection(
        "item2", Odds(-300, OddsFormat.US)), Selection(
        "item2", Odds(-400, OddsFormat.US))]
    result = get_parlay_payout(Decimal(2.00), selections)
    np.testing.assert_equal(
        result['odds'].eu_odds, Decimal('2.499'))
    np.testing.assert_equal(
        result['return'], Decimal('4.998'))
