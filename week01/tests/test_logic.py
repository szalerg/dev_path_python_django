# test_logic.py
"""
Testy automatyczne dla zadań logicznych
"""
import pytest
from week01.tasks import logic

def test_is_anagram():
    assert logic.is_anagram('kot', 'tok') == True
    assert logic.is_anagram('kot', 'pies') == False

def test_is_palindrome():
    assert logic.is_palindrome('kajak') == True
    assert logic.is_palindrome('kot') == False

def test_prime_numbers():
    assert logic.prime_numbers(10) == [2, 3, 5, 7]
    assert logic.prime_numbers(5) == [2, 3, 5]
    assert logic.prime_numbers(1) == []