# test_logic.py
"""
Testy automatyczne dla zadań logicznych
"""
import pytest
from tasks import 2_logic

def test_is_anagram():
    assert 2_logic.is_anagram('kot', 'tok') is None

def test_is_palindrome():
    assert 2_logic.is_palindrome('kajak') is None

def test_prime_numbers():
    assert 2_logic.prime_numbers(10) is None
