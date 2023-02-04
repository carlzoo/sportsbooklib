Module sportsbooklib.calculators.implied_odds_calc
==================================================

Functions
---------

    
`get_implied_probability(odds: List[sportsbooklib.models.odds.odds.Odds]) ‑> Mapping[str, List[decimal.Decimal]]`
:   Given list of Odds, calculate the implied probability and fair odds.
    Based on https://github.com/octosport/octopy/blob/master/octopy/implied.py
    
    Parameters
    ----------
    odds : List[Odds]
        List of odds for calculation.
    
    Returns
    -------
    Dict:
        <implied_probability> List[Decimal]: List of implied probability in the respective order of the input odds
        <fair_odds> List[Decimal]: List of fair odds in the respective order of the input odds