Module sportsbooklib.calculators.arbitrage_calc
===============================================

Functions
---------

    
`get_arbitrage(stake: decimal.Decimal, odds: List[sportsbooklib.models.odds.odds.Odds]) ‑> Mapping[str, Union[List[decimal.Decimal], decimal.Decimal]]`
:   Calculate the max arbitrage profit based on given stake and odds.
    
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