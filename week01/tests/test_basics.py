# test_basics.py
"""
Testy automatyczne dla zadań podstawowych
"""
import pytest
from week01.tasks import basics

def test_zadanie_1():
    assert basics.zadanie_1(2, 3) == 5      # Tu później podstawić implementację

def test_zadanie_2():
    assert basics.zadanie_2(2) == True
    assert basics.zadanie_2(3) == False

def test_zadanie_3():
    assert basics.zadanie_3(12 ,18) == 6    # Wspólny dzielnik większy niż 1
    assert basics.zadanie_3(7 ,5)   == 1    # Liczby pierwsze
    assert basics.zadanie_3(20 ,30) == 10   # Większe liczby
    assert basics.zadanie_3(9, 9)   == 9    # Równe liczby