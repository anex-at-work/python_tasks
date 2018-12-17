from task import HighestProduct
from random import randint

test_array = [1, 10, 2, 6, 5, 3]
short_test_array = [2, 30]
negative_test_array = [-5, -200, -3, -8, -65, -40]
empty_test_array = []
huge_test_array = [randint(1, 10) for _ in range(100000)]
huge_test_array += [11, 12, 13]


def test_calculate1():
    res = HighestProduct.calculate1(test_array)
    assert res == 300
    res = HighestProduct.calculate1(empty_test_array)
    assert res == 0
    res = HighestProduct.calculate1(short_test_array)
    assert res == 60
    res = HighestProduct.calculate1(negative_test_array)
    assert res == -120
    res = HighestProduct.calculate1(huge_test_array)
    assert res == 1716
    res = HighestProduct.calculate1(test_array, 2)
    assert res == 60


def test_calculate2():
    res = HighestProduct.calculate2(test_array)
    assert res == 300
    res = HighestProduct.calculate2(empty_test_array)
    assert res == 0
    res = HighestProduct.calculate2(short_test_array)
    assert res == 60
    res = HighestProduct.calculate2(negative_test_array)
    assert res == -120
    res = HighestProduct.calculate2(huge_test_array)
    assert res == 1716
    res = HighestProduct.calculate2(test_array, 2)
    assert res == 60
