from sportsbooklib.models.selection.selection import Selection
from sportsbooklib.models.odds.odds import Odds
from sportsbooklib.models.odds.enums import OddsFormat


def test_selection_constructor():
    selection = Selection(name='test', odds=Odds(-110, OddsFormat.US))
    assert (selection.name == 'test')
    assert (selection.odds.us_odds == -110)
