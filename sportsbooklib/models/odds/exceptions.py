class InvalidOddsFormatException(Exception):
    'Odds value and/or format is invalid'
    pass


class ZeroOddsValueException(Exception):
    'Odds value must be greater than 0'
    pass
