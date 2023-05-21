#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal
from fractions import Fraction
import pytest
from sportsbooklib.models.odds.enums import OddsFormat
from sportsbooklib.models.odds.exceptions import InvalidOddsFormatException
from sportsbooklib.models.odds import Odds


def test_invalid_us_less_than_100():
    with pytest.raises(InvalidOddsFormatException):
        Odds(-50, OddsFormat.US)


def test_invalid_us_equal_to_minus_100():
    with pytest.raises(InvalidOddsFormatException):
        Odds(-100, OddsFormat.US)


def test_valid_us_negative():
    assert (Odds(-110, OddsFormat.US).us_odds == -110)


def test_valid_us_positive():
    assert (Odds(+100, OddsFormat.US).us_odds == 100)


def test_invalid_eu_odds():
    with pytest.raises(InvalidOddsFormatException):
        Odds(Decimal(0.5), OddsFormat.EU)


def test_valid_eu_odds():
    assert (Odds(Decimal(1.50), OddsFormat.EU).eu_odds == Decimal(1.50))


def test_invalid_hk_odds():
    with pytest.raises(InvalidOddsFormatException):
        Odds(Decimal(-0.5), OddsFormat.HK)


def test_valid_hk_odds():
    assert (Odds(Decimal(0.50), OddsFormat.HK).hk_odds == Decimal(0.50))


def test_invalid_uk_odds():
    with pytest.raises(InvalidOddsFormatException):
        Odds(Fraction(-2, 3), OddsFormat.UK)


def test_valid_uk_odds():
    assert (Odds(Fraction(1, 2), OddsFormat.UK).uk_odds == Fraction(1, 2))


def test_conversion_us_negative():
    odds = Odds(-300, OddsFormat.US)
    assert (odds.us_odds == -300)
    assert (odds.eu_odds == Decimal('1.333'))
    assert (odds.hk_odds == Decimal('0.333'))
    assert (odds.uk_odds == Fraction(1, 3))


def test_conversion_us_positive():
    odds = Odds(100, OddsFormat.US)
    assert (odds.us_odds == 100)
    assert (odds.eu_odds == Decimal('2.000'))
    assert (odds.hk_odds == Decimal('1.000'))
    assert (odds.uk_odds == Fraction(1))


def test_conversion_eu_under_2():
    odds = Odds(Decimal(1.64), OddsFormat.EU)
    assert (odds.us_odds == -156)
    assert (odds.eu_odds == Decimal('1.640'))
    assert (odds.hk_odds == Decimal('0.640'))
    assert (odds.uk_odds == Fraction(16, 25))


def test_conversion_eu_over_2():
    odds = Odds(Decimal(2.64), OddsFormat.EU)
    assert (odds.us_odds == 164)
    assert (odds.eu_odds == Decimal('2.640'))
    assert (odds.hk_odds == Decimal('1.640'))
    assert (odds.uk_odds == Fraction(41, 25))


def test_conversion_hk_under_1():
    odds = Odds(Decimal(0.64), OddsFormat.HK)
    assert (odds.us_odds == -156)
    assert (odds.eu_odds == Decimal('1.640'))
    assert (odds.hk_odds == Decimal('0.640'))
    assert (odds.uk_odds == Fraction(16, 25))


def test_conversion_hk_over_1():
    odds = Odds(Decimal(1.64), OddsFormat.HK)
    assert (odds.us_odds == 164)
    assert (odds.eu_odds == Decimal('2.640'))
    assert (odds.hk_odds == Decimal('1.640'))
    assert (odds.uk_odds == Fraction(41, 25))


def test_conversion_uk_under_1():
    odds = Odds(Fraction(1, 3), OddsFormat.UK)
    assert (odds.us_odds == -300)
    assert (odds.eu_odds == Decimal('1.333'))
    assert (odds.hk_odds == Decimal('0.333'))
    assert (odds.uk_odds == Fraction(1, 3))


def test_conversion_uk_over_1():
    odds = Odds(Fraction(11, 10), OddsFormat.UK)
    assert (odds.us_odds == 110)
    assert (odds.eu_odds == Decimal('2.10'))
    assert (odds.hk_odds == Decimal('1.10'))
    assert (odds.uk_odds == Fraction(11, 10))
