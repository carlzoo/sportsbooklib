from decimal import Decimal
from fractions import Fraction
from sportsbooklib.models.odds.enums import OddsFormat
from sportsbooklib.models.odds.exceptions import InvalidOddsFormatException, ZeroOddsValueException

class Odds:
    def __init__(self, event: str, value, format: OddsFormat):
        self.event = event
        self.value = value
        self.format = format
        self.us_odds = 0
        self.eu_odds = 0
        self.hk_odds = 0
        self.uk_odds = 0
        self.parse_odds_value()

    def parse_odds_value(self):
        if (not self.value) or (not self.format):
            raise InvalidOddsFormatException

        if self.format == OddsFormat.US:
            self.set_us_odds()
            self.convert_to_eu_odds()
            self.convert_to_hk_odds()
            self.convert_to_uk_odds()
        elif self.format == OddsFormat.EU:
            self.set_eu_odds()
            self.convert_to_us_odds()
            self.convert_to_hk_odds()
            self.convert_to_uk_odds()
        elif self.format == OddsFormat.HK:
            self.set_hk_odds()
        elif self.format == OddsFormat.UK:
            self.set_uk_odds()
        else:
            raise InvalidOddsFormatException
    
    def set_us_odds(self):
        value_to_parse = self.value[1:] if self.value[0] == '+' else self.value
        try:
            self.us_odds = int(round(Decimal(value_to_parse)))
            if self.us_odds == 0:
                raise ZeroOddsValueException
        except:
            raise InvalidOddsFormatException

    def set_eu_odds(self):
        try:
            self.eu_odds = round(Decimal(self.value),3)
            if self.eu_odds < 1:
                raise ZeroOddsValueException
        except:
            raise InvalidOddsFormatException

    def set_hk_odds(self):
        try:
            self.hk_odds = round(Decimal(self.value),3)
            if self.hk_odds <= 0:
                raise ZeroOddsValueException
        except:
            raise InvalidOddsFormatException

    def set_uk_odds(self):
        try:
            self.uk_odds = Fraction(self.value)
            if self.uk_odds == 0:
                raise ZeroOddsValueException
        except:
            raise InvalidOddsFormatException

    def convert_to_eu_odds(self):
        if self.format == OddsFormat.US:
            if self.us_odds < 0:
                self.eu_odds = round(100/self.us_odds+1,3)
            else:
                self.eu_odds = round(self.us_odds/100+1,3)
        elif self.format == OddsFormat.HK:
            self.eu_odds = self.hk_odds + 1
        else:
            self.eu_odds = round(self.uk_odds.numerator/Decimal(self.uk_odds.denominator)+1,3)
    
    def convert_to_hk_odds(self):
        if self.format == OddsFormat.US:
            if self.us_odds < 0:
                self.hk_odds = round(100/self.us_odds,3)
            else:
                self.hk_odds = round(self.us_odds/100,3)
        elif self.format == OddsFormat.EU:
            self.hk_odds = self.eu_odds-1
        else:
            self.hk_odds = round(self.uk_odds.numerator/Decimal(self.uk_odds.denominator),3)

    def convert_to_uk_odds(self):
        if self.format == OddsFormat.US:
            if self.us_odds < 0:
                self.uk_odds = Fraction(100/self.us_odds)
            else:
                self.uk_odds = Fraction(self.us_odds/100)
        elif self.format == OddsFormat.EU:
            self.uk_odds = Fraction(self.eu_odds-1)
        else:
            self.uk_odds = Fraction(self.hk_odds)

    def convert_to_us_odds(self):
        if self.format == OddsFormat.EU:
            if self.eu_odds < 2:
                self.us_odds = int(-1 * 100 / (self.eu_odds-1))
            else:
                self.us_odds = int(100 / (self.eu_odds-1))
        elif self.format == OddsFormat.HK:
            if self.hk_odds < 1:
                self.us_odds = int(-1 * 100 / (self.hk_odds))
            else:
                self.us_odds = int(100 / (self.hk_odds))
        else:
            if self.uk_odds.numerator < self.uk_odds.denominator:
                self.us_odds = -1 * round(Decimal(100) / (self.uk_odds.numerator/Decimal(self.uk_odds.denominator)))
            else:
                self.us_odds = round(Decimal(100) * (self.uk_odds.numerator/Decimal(self.uk_odds.denominator)))
        