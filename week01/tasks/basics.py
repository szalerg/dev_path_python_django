# 1_basics.py
"""
Proste zadania z Pythona: zmienne, warunki, pętle, funkcje.
Każde zadanie ma poziom trudności: ⭐, ⭐⭐, ⭐⭐⭐
"""

def zadanie_1(a, b):
    # ⭐ Napisz funkcję, która zwraca sumę dwóch liczb    
    return a + b

def zadanie_2(num):
    # ⭐⭐ Napisz funkcję, która sprawdza, czy liczba jest parzysta
    if num % 2 == 0:
        return True         # wartość logiczna
    else:
        return False
    
def zadanie_3(a, b):
    # ⭐⭐⭐ Napisz funkcję, która zwraca największy wspólny dzielnik dwóch liczb
    max_divisor = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            max_divisor = i
    return max_divisor