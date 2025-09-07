# test_strings.py
import pytest
from week02.tasks import strings

def test_zadanie_1():
    assert strings.zadanie_1("Hello") == 5 
    assert strings.zadanie_1("") == 0

def test_zadanie_2():
    assert strings.zadanie_2("hello") == "olleh"
    assert strings.zadanie_2("mars") == "sram"
    assert strings.zadanie_2("") == ""

def test_zadanie_3():
    assert strings.zadanie_3("abc") is None
