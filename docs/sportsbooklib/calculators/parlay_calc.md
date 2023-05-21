Module sportsbooklib.calculators.parlay_calc
============================================

Functions
---------

    
`get_parlay_payout(stake: decimal.Decimal, selections: List[sportsbooklib.models.selection.selection.Selection]) ‑> List[Mapping[str, Union[decimal.Decimal, sportsbooklib.models.odds.Odds]]]`
:   Given stake and list of n odds, calculate combined odds and return
    
    Parameters
    ----------
    stake : Decimal
        stake to risk
    selections : List[Selection]
        List of selections to compute
    
    Returns
    -------
    Dict:
        <odds> Odds: Total odds of the parlay
        <win> Decimal: Total amount won