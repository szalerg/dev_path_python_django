# 3_dicts.py
"""
Zadania związane ze słownikami (dict).
"""

def zadanie_1(d):
    # ⭐ Napisz funkcję, która zwraca listę kluczy
    d = {
        "brand": "Ford",
        "model": "Mustang",
        "year": "1964"
    }

    return list(d.keys())

def zadanie_2(d):
    # ⭐⭐ Napisz funkcję, która zwraca sumę wartości
    return sum(d.values())

def zadanie_3(d):
    # ⭐⭐⭐ Napisz funkcję, która odwraca klucze z wartościami
    reversed_dict = {}
    for key, value in d.items():
        reversed_dict[value] = key
    return reversed_dict
