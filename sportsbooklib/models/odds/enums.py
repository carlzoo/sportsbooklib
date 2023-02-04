from enum import Enum


class OddsFormat(Enum):
    """
    OddsFormat:

        - US - US Format (-110)
        - EU - European Format (1.909)
        - HK - Hong Kong Format (0.909)
        - UK - UK Fractional Format (10/11)
    """
    US = 'US'
    EU = 'EU'
    UK = 'UK'
    HK = 'HK'
