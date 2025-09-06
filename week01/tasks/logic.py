# 2_logic.py
"""
Zadania logiczne i algorytmiczne.
"""

def is_anagram(s1, s2):
    """⭐⭐ Sprawdza czy s1 i s2 są anagramami"""
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

def is_palindrome(s):
    """⭐⭐ Sprawdza czy s jest palindromem"""
    if s == s[::-1]:
        return True
    else:
        return False

def prime_numbers(n):
    """⭐⭐⭐ Zwraca listę liczb pierwszych <= n"""
    primes = []
    for j in range(2, n+1):             # zmienna petli j
        prime = True
        for i in range(2, j):           # sprawdzam dzielniki
            if j % i == 0:
                prime = False
                break
        if prime:
            primes.append(j)
    return primes