# conditions.py

def zadanie_1(x):
    # ⭐ Napisz funkcję, która sprawdza, czy liczba jest dodatnia, ujemna czy zero
    if x > 0:
        return("dodatnia")
    elif x == 0:
        return("zero")
    else:
        return("ujemna")


def zadanie_2(year):
    # ⭐⭐ Napisz funkcję, która sprawdza, czy rok jest przestępny
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def zadanie_3(a, b, c):
    # ⭐⭐⭐ Napisz funkcję, która sprawdza, czy z boków a, b, c można zbudować trójkąt
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
        
    
        
    
       
