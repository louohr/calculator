# Unit tests

from Calculator.calculations import add, subtract, divide, multiply


def test_add():
    assert add(1, 2) != 5
    assert add(3, 4) == 7


def test_sub():
    assert subtract(4, 5) != 1
    assert subtract(10, 2) == 8


def test_div():
    assert divide(7, 2) != 4
    assert divide(10, 0) == 1  # ZeroDivisionError: division by zero


def test_mult():
    assert multiply(7, 2) != 13
    assert multiply(3, 3) == 9
