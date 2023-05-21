Module sportsbooklib.calculators.expected_value_calc
====================================================

Functions
---------

    
`get_expected_value(implied_probability: decimal.Decimal, final_odds: sportsbooklib.models.odds.odds.Odds) ‑> decimal.Decimal`
:   Calculate the expected value of a bet.
    
    Args:
        implied_probability (Decimal): The implied probability of winning the bet.
        final_odds (Odds): The final odds of the bet.
    
    Raises:
        NegativeImpliedProbabilityException
    
    Returns:
        Decimal: The expected value of the bet.

    
`get_expected_value_for_legs(leg_odds: List[sportsbooklib.models.odds.odds.Odds], final_odds: sportsbooklib.models.odds.odds.Odds, target_leg: int = 0) ‑> decimal.Decimal`
:   Calculate the expected value of a bet for the target_leg index in leg_odds.
    
    Args:
        leg_odds (List[Odds]): List of odds for the legs.
        final_odds (Odds): The final odds of the bet.
        target_leg (int): The index in leg_odds to use. Default is 0.
    
    Returns:
        Decimal: The expected value of the bet.