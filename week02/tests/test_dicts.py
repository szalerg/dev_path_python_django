# test_dicts.py
import pytest
from week02.tasks import dicts

def test_zadanie_1():
    assert dicts.zadanie_1({"brand": "Ford","model": "Mustang","year": "1964"}) == ["brand","model","year"]

def test_zadanie_2():
    assert dicts.zadanie_2({"a":1}) == 1
    assert dicts.zadanie_2({"a": 1, "b": 2, "c": 3}) == 6

def test_zadanie_3():
    # 1. Przygotowanie danych testowych
    example_dict = {"brand": "Ford", "model": "Mustang", "year": "1964"}
    
    # 2. Spodziewany wynik
    expected = {"Ford": "brand", "Mustang": "model", "1964": "year"}
    
    # 3. Porównanie
    assert dicts.zadanie_3(example_dict) == expected
