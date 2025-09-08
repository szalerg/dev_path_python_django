# test_lists.py
import pytest
from week02.tasks import lists

def test_zadanie_1():
    assert lists.zadanie_1([1,2,3]) == 6

def test_zadanie_2():
    assert lists.zadanie_2([1,2,3]) == [3,2,1]

def test_zadanie_3():
    assert lists.zadanie_3([1,2,3]) == 3
