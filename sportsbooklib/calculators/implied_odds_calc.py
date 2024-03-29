from decimal import Decimal
from typing import List, Mapping
import numpy as np
from sportsbooklib.calculators.exceptions import InvalidNumberOfInputsException
from sportsbooklib.models.odds import Odds
from sportsbooklib.models.odds.enums import OddsFormat


def get_implied_probability(odds: List[Odds]) -> Mapping[str, List[Decimal]]:
    '''

    Given list of Odds, calculate the implied probability and fair odds.
    Based on https://github.com/octosport/octopy/blob/master/octopy/implied.py

    Parameters
    ----------
    odds : List[Odds]
        List of odds for calculation.

    Returns
    -------
    Dict:
        <implied_probability> List[Decimal]: List of implied probability in the respective order of the input odds
        <no_vig_probability> List[Decimal]: List of fair odds in the respective order of the input odds
    '''
    if len(odds) < 2:
        raise InvalidNumberOfInputsException

    odds_decimal = np.array(
        list(map(lambda x: x.eu_odds, odds)), dtype=Decimal)
    p_i = 1 / odds_decimal
    # multiplicative method
    # TODO: support shin, power, additive methods
    normalization = sum(p_i)
    no_vig_probability = p_i / normalization
    return {'implied_probability': p_i, 'no_vig_probability': no_vig_probability}


def get_implied_odds(probability: Decimal) -> Odds:
    """
    Calculate the implied odds based on a given probability.

    Args:
        probability (Decimal): The probability.

    Returns:
        Odds: The implied odds.

    Raises:
        None.

    Examples:
        >>> probability = Decimal('0.5')
        >>> get_implied_odds(probability)
        Odds(Decimal('2.0'), 'EU')

        >>> probability = Decimal('0.2')
        >>> get_implied_odds(probability)
        Odds(Decimal('5.0'), 'EU')
    """
    return Odds(1/probability, OddsFormat.EU)
