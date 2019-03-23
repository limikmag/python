import pytest
import algorithms.math.fast_exponential as math


def test_recursive():
    assert math.power(2, 10) == 1024
    assert math.power(2, 0) == 1
    assert math.power(0, 0) == 1
    assert math.power(12, 12) == 8916100448256


def test_iterative():
    assert math.fast_power(2, 10) == 1024
    assert math.fast_power(2, 0) == 1
    assert math.fast_power(0, 0) == 1
    assert math.fast_power(12, 12) == 8916100448256