import pytest
from week03.tasks import functions

def test_zadanie_1():
    assert functions.zadanie_1(2, 3) == 5

def test_zadanie_2():
    assert functions.zadanie_2("Anna") == "Hello, Anna!"

def test_zadanie_3():
    assert functions.zadanie_3([1, 5, 3]) == 5
