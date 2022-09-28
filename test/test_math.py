from contextlib import nullcontext
from itertools import product
import pytest


def test_one_plus_one():
    assert 1 + 1 == 2


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0
    assert 'division by zero' in str(e.value)


products = [

    (2, 5, 10),
    (1, 99, 99),
    (0, 5, 0),
    (2, -5, -10),
    (-5, -5, 25),
    (2.5, 6.7, 16.75),
]


@pytest.mark.parametrize('a,b,product', products)
def test_multiplication(a, b, product):
    assert a * b == product
