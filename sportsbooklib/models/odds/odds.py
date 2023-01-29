#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal, InvalidOperation
from fractions import Fraction
from sportsbooklib.models.odds.enums import OddsFormat
from sportsbooklib.models.odds.exceptions import InvalidOddsFormatException
from typing import Union


class Odds:
    def __init__(self, value: Union[int, Fraction, Decimal], format: OddsFormat):
        self.value = value
        self.format = format
        self.us_odds = 0
        self.eu_odds = 0
        self.hk_odds = 0
        self.uk_odds = 0
        self.implieds_odds = 0

        self.parse_odds_value()
        self.get_implied_odds()

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
        self.us_odds = self.value
        if self.us_odds < 100 and self.us_odds >= -100:
            raise InvalidOddsFormatException
        if self.us_odds == -100:
            raise InvalidOddsFormatException

    def set_eu_odds(self):
        try:
            self.eu_odds = round(Decimal(self.value), 3)
            if self.eu_odds < 1:
                raise InvalidOddsFormatException
        except InvalidOperation:
            raise InvalidOddsFormatException

    def set_hk_odds(self):
        try:
            self.hk_odds = round(Decimal(self.value), 3)
            if self.hk_odds <= 0:
                raise InvalidOddsFormatException
        except InvalidOperation:
            raise InvalidOddsFormatException

    def set_uk_odds(self):
        try:
            self.uk_odds = Fraction(self.value)
            if self.uk_odds <= 0:
                raise InvalidOddsFormatException
        except ValueError:
            raise InvalidOddsFormatException

    def convert_to_eu_odds(self):
        if self.format == OddsFormat.US:
            if self.us_odds < 0:
                self.eu_odds = round(-1 * 100/Decimal(self.us_odds)+1, 3)
            else:
                self.eu_odds = round(Decimal(self.us_odds)/100+1, 3)
        elif self.format == OddsFormat.HK:
            self.eu_odds = self.hk_odds + 1
        else:
            self.eu_odds = round(self.uk_odds.numerator /
                                 Decimal(self.uk_odds.denominator)+1, 3)

    def convert_to_hk_odds(self):
        if self.format == OddsFormat.US:
            if self.us_odds < 0:
                self.hk_odds = round(-1 * 100/Decimal(self.us_odds), 3)
            else:
                self.hk_odds = round(Decimal(self.us_odds)/100, 3)
        elif self.format == OddsFormat.EU:
            self.hk_odds = self.eu_odds-1
        else:
            self.hk_odds = round(self.uk_odds.numerator /
                                 Decimal(self.uk_odds.denominator), 3)

    def convert_to_uk_odds(self):
        if self.format == OddsFormat.US:
            if self.us_odds < 0:
                self.uk_odds = Fraction(100 / (-1 * self.us_odds))
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
                self.us_odds = int(100 * self.eu_odds - 100)
        elif self.format == OddsFormat.HK:
            if self.hk_odds < 1:
                self.us_odds = int(-1 * 100 / (self.hk_odds))
            else:
                self.us_odds = int(100 * (self.hk_odds))
        else:
            if self.uk_odds.numerator < self.uk_odds.denominator:
                self.us_odds = -1 * round(Decimal(100) / (self.uk_odds.numerator /
                                                          Decimal(self.uk_odds.denominator)))
            else:
                self.us_odds = round(
                    Decimal(100) * (self.uk_odds.numerator/Decimal(self.uk_odds.denominator)))

    def get_implied_odds(self):
        if self.us_odds < 0:
            positive_value = self.us_odds * -1
            self.implied_odds = positive_value/(positive_value + 100)
        else:
            self.implied_odds = 100/(self.us_odds + 100)

    def __str__(self):
        if self.format == OddsFormat.US:
            if self.value > 0:
                return '+' + str(self.us_odds)
            else:
                return str(self.us_odds)
        elif self.format == OddsFormat.UK:
            return str(self.uk_odds.numerator) + '/' + str(self.uk_odds.denominator)
        elif self.format == OddsFormat.HK:
            return str(self.hk_odds)
        else:
            return str(self.eu_odds)
