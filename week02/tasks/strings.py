# 1_strings.py
"""
Zadania związane z napisami (strings).
Każde zadanie ma poziom trudności: ⭐, ⭐⭐, ⭐⭐⭐
"""

def zadanie_1(text):
    # ⭐ Napisz funkcję, która zwraca długość napisu
    return len(text)

def zadanie_2(text):
    # ⭐⭐ Napisz funkcję, która odwraca napis
    turned = text[::-1]
    return turned

def zadanie_3(text):
    # ⭐⭐⭐ Napisz funkcję, która liczy liczbę samogłosek
    vowels = "aeiouAEIOU"
    count = 0

    for c in text:
        if c in vowels:
            count += 1
    return count