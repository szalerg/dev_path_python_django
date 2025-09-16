import pytest
from week03.tasks import conditions

def test_zadanie_1():
    assert conditions.zadanie_1(5) == "dodatnia"
    assert conditions.zadanie_1(-3) == "ujemna"
    assert conditions.zadanie_1(0) == "zero"

def test_zadanie_2():
    assert conditions.zadanie_2(2020) == True
    assert conditions.zadanie_2(1900) == False

def test_zadanie_3():
    assert conditions.zadanie_3(3, 4, 5) == True
    assert conditions.zadanie_3(1, 2, 3) == False
