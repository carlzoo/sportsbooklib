#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from sportsbooklib import models
from sportsbooklib.models.odds.enums import OddsFormat
from sportsbooklib.models.odds.exceptions import InvalidOddsFormatException
from sportsbooklib.models.odds.odds import Odds

def test_invalid_us_less_than_100():
    with pytest.raises(InvalidOddsFormatException):
        Odds(-50, 'US')

def test_invalid_us_equal_to_minus_100():
    with pytest.raises(InvalidOddsFormatException):
        Odds(-100, 'US')

def test_valid_us_negative():
    assert(Odds(-110, OddsFormat.US ).us_odds == -110)

def test_valid_us_positive():
    assert(Odds(+100, OddsFormat.US ).us_odds == 100)