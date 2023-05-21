from decimal import Decimal
from typing import Mapping, List, Union
from sportsbooklib.calculators.exceptions import NegativeStakeInputException
from sportsbooklib.calculators.implied_odds_calc import get_implied_probability
from sportsbooklib.models.odds import Odds


def get_arbitrage(stake: Decimal, odds: List[Odds]) -> Mapping[str, Union[List[Decimal], Decimal]]:
    """

    Calculate the max arbitrage profit based on given stake and odds.

    Parameters
    ----------
    stake: Decimal
        Total stake to risk
    odds : List[Odds]
        List of odds for calculation.

    Returns
    -------
    Dict:
        <stakes> List[Decimal]: List of stake amount to put on each odds.
        <profit> Decimal: Overall profit
    """

    if stake < 0:
        raise NegativeStakeInputException

    implied_probabilities = get_implied_probability(
        odds)["implied_probability"]
    arbitrage_probability = sum(implied_probabilities)
    stakes = [stake * implied_probabilities[i] /
              arbitrage_probability for i in range(len(odds))]
    profit = stake / arbitrage_probability - stake
    return {'stakes': stakes, 'profit': profit}
