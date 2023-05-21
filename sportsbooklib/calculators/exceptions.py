class InvalidNumberOfInputsException(Exception):
    'Must input at least 2 odds'
    pass


class NegativeStakeInputException(Exception):
    'Must provide positive stake input'
    pass


class NegativeImpliedProbabilityException(Exception):
    'Implied Probability must be greater or equal to 0'
    pass


class InvalidTargetLegException(Exception):
    'Target leg must be 0 to len(target_legs)-1'
    pass
