Module sportsbooklib.calculators.hold_calc
==========================================

Functions
---------

    
`get_hold(odds: List[sportsbooklib.models.odds.Odds]) ‑> decimal.Decimal`
:   Calculate hold, given list of Odds, where length of list > 1
    
    Parameters
    ----------
    odds : List[Odds]
        List of odds to calculate hold
    
    Returns
    -------
    Decimal
        The hold value as a Decimal

    
`get_hold_for_selections(selections: List[sportsbooklib.models.selection.Selection]) ‑> decimal.Decimal`
:   Calculate hold, given list of Selection's odds, where length of list > 1
    
    Parameters
    ----------
    odds : List[Selection]
        List of Selection to calculate hold
    
    Returns
    -------
    Decimal
        The hold value as a Decimal