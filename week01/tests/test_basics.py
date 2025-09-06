# test_basics.py
"""
Testy automatyczne dla zadań podstawowych
"""
import pytest
from week01.tasks import basics

def test_zadanie_1():
    assert basics.zadanie_1(2, 3) == 5  # Tu później podstawić implementację

def test_zadanie_2():
    assert basics.zadanie_2(2) == True
    assert basics.zadanie_2(3) == False