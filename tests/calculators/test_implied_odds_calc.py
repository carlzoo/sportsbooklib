from decimal import Decimal
import numpy as np
import pytest

from sportsbooklib.calculators.exceptions import InvalidNumberOfInputsException
from sportsbooklib.calculators.implied_odds_calc import get_implied_probability
from sportsbooklib.models.odds.enums import OddsFormat
from sportsbooklib.models.odds.odds import Odds


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
