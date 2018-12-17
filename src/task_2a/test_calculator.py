import pytest
from calculator import Calculator

correct_expression = '-1.2 * (2 + 6 / 3) + 6 / (5 + (-6 + 8) / 2)'  # -3.8
correct_expression2 = '6 / (5 + (-6 + 8) / 2)'  # 1
correct_expression3 = '-1.2 * (2 + 6 / 3)'  # -4.8
wrong_expression = '-1.2 * 2 + 6 / 3)'


def test_simple_calc():
    res = Calculator(correct_expression).simple_calc()
    assert res == -3.8


def test_calc():
    res = Calculator(correct_expression).calc()
    assert res == -3.8
    res = Calculator(correct_expression2).calc()
    assert res == 1.0
    res = Calculator(correct_expression3).calc()
    assert res == -4.8
    res = Calculator(wrong_expression).calc()
    assert res == None

