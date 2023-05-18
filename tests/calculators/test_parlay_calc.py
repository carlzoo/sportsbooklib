import numpy as np
import pytest
from sportsbooklib.calculators.parlay_calc import get_round_robin_payout
from decimal import Decimal

from sportsbooklib.models.exceptions import InvalidSelectionsInputException
from sportsbooklib.models.odds.enums import OddsFormat
from sportsbooklib.models.odds.odds import Odds
from sportsbooklib.models.selection.selection import Selection


def test_invalid_empty_selections_round_robin():
    with pytest.raises(InvalidSelectionsInputException):
        get_round_robin_payout(Decimal('1.00'), [])


def test_invalid_one_selections_round_robin():
    selections = [Selection("test", Odds('1.50', OddsFormat.EU))]
    with pytest.raises(InvalidSelectionsInputException):
        get_round_robin_payout(
            Decimal('1.00'), selections)


def test_two_selections_round_robin():
    selections = [
        Selection('item1', Odds(-400, OddsFormat.US)),
        Selection('item2', Odds(-200, OddsFormat.US))
    ]
    result = get_round_robin_payout(
        Decimal('2.00'), selections)
    np.testing.assert_equal(
        len(result), 1)
    np.testing.assert_equal(
        result[0]['legs'], 2)
    np.testing.assert_equal(
        result[0]['total_risk'], Decimal('2.00'))
    np.testing.assert_almost_equal(
        result[0]['total_odds'].eu_odds, Decimal('1.875'), 4)
    np.testing.assert_almost_equal(
        result[0]['max_win'], Decimal('3.75'), 3)


def test_three_selections_round_robin():
    selections = [
        Selection('item1', Odds(-143, OddsFormat.US)),
        Selection('item2', Odds(-255, OddsFormat.US)),
        Selection('item3', Odds(250, OddsFormat.US))
    ]
    result = get_round_robin_payout(
        Decimal('2.00'), selections)
    np.testing.assert_equal(
        len(result), 4)
