from decimal import Decimal
from sportsbooklib.calculators.hold_calc import get_hold_for_selections
from sportsbooklib.models.odds.enums import OddsFormat
from sportsbooklib.models.odds import Odds
from sportsbooklib.models.selection.selection import Selection
import numpy as np


def test_get_2_way_hold():
    sel_1 = Selection(name="Selection 1", odds=Odds(-110, OddsFormat.US))
    sel_2 = Selection(name="Selection 2", odds=Odds(-110, OddsFormat.US))
    np.testing.assert_almost_equal(get_hold_for_selections(
        [sel_1, sel_2]), Decimal('0.0476'), decimal=4)


def test_get_3_way_hold():
    sel_1 = Selection(name="Selection 1", odds=Odds(275, OddsFormat.US))
    sel_2 = Selection(name="Selection 2", odds=Odds(275, OddsFormat.US))
    sel_3 = Selection(name="Selection 2", odds=Odds(-105, OddsFormat.US))
    np.testing.assert_almost_equal(get_hold_for_selections(
        [sel_1, sel_2, sel_3]), Decimal('0.0456'), decimal=4)
