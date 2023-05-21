class InvalidNumberOfInputsException(Exception):
    'Must input at least 2 odds'
    pass


class NegativeStakeInputException(Exception):
    'Must provide positive stake input'
    pass


class NegativeImpliedProbabilityException(Exception):
    'Implied Probability must be greater or equal to 0'
    pass
