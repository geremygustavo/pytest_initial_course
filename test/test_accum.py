import pytest

from stuf.accum import Accumulator


# from stuf.accum import Accumulator




def test_acumulator_init():
    accum2 = Accumulator()
    assert accum2.count == 0
