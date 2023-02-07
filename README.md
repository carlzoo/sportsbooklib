[![Actions Status](https://github.com/carlzoo/sportsbooklib/workflows/build/badge.svg)](https://github.com/carlzoo/sportsbooklib/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# sportsbooklib
Python module for performing sportsbook odds calculations

# Features
The follow features are supported:
- Conversion between US (-110), EU(1.909), UK (10/11), HK (0.909) formats
- Calculating the implied probability and fair odds
- Calculating the hold
- Arbitrage Calculator

Planned features in [issues](https://github.com/carlzoo/sportsbooklib/labels/enhancement).

# Documentation
Documentation can be found in the [docs](https://github.com/carlzoo/sportsbooklib/tree/main/docs) directory

# Setup

Requirements: Python >=3.6

```
pip install -U pytest 
pip install .
```

# Running tests
In the root directory of the project, run
```
pytest
```

# Linting
To check linting issues, uses flake8:
```
pip install -U flake8
flake8 . --count --max-complexity=15 --max-line-length=127 --statistics
```

To fix linting issues, install autopep8:
```
pip install -U autopep8
autopep8 --in-place --recursive .
```

# Usage
Simply import ```sportsbooklib``` into your python code.

Example: Watch this space


# Contributing

For contributions and discussions check our [Contributing Guide](https://github.com/carlzoo/sportsbooklib/blob/main/CONTRIBUTING.md)
