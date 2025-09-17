# loops.py

def zadanie_1(n):
    # ⭐ Napisz funkcję, która wypisuje liczby od 1 do n
    for i in range(1, n + 1):
        print(i)


def zadanie_2(n):
    # ⭐⭐ Napisz funkcję, która zwraca sumę liczb od 1 do n
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def zadanie_3(n):
    # ⭐⭐⭐ Napisz funkcję, która zwraca n! (silnię)
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
