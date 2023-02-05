Module sportsbooklib.models.odds.odds
=====================================

Classes
-------

`Odds(value: Union[int, fractions.Fraction, decimal.Decimal], format: sportsbooklib.models.odds.enums.OddsFormat)`
:   The Odds Object.
    
    Attributes
    ----------
    value : Union[int, Fraction, Decimal]
        The odds value as an integer, Decimal or Fraction
    format : OddsFormat
        The format of the odds as OddsFormat (US, EU, HK, UK)

    ### Methods

    `convert_to_eu_odds(self)`
    :

    `convert_to_hk_odds(self)`
    :

    `convert_to_uk_odds(self)`
    :

    `convert_to_us_odds(self)`
    :

    `parse_odds_value(self)`
    :

    `set_eu_odds(self)`
    :

    `set_hk_odds(self)`
    :

    `set_uk_odds(self)`
    :

    `set_us_odds(self)`
    :