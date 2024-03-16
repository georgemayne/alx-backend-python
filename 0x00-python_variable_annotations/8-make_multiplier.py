#!/usr/bin/env python3
""" Complex types - functions """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Function that multiplies a float by multiplier """
    return lambda x: x * multiplier
