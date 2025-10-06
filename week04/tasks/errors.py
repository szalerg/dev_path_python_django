# Dzielenie z błędem
# Napisz funkcję, która przyjmuje dwie liczby i zwraca wynik ich dzielenia. Obsłuż przypadek dzielenia przez zero (zwróć "Nie można dzielić przez zero").
def division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Nie dziel przez zero!"
    else:
        return result
    finally:
        print("Koniec działania")
# Konwersja liczby
# Napisz funkcję, która próbuje zamienić string na liczbę całkowitą. Jeśli się nie uda, zwróć "Błąd konwersji".
def conversion(text):
    try:
        return int(text)
    except ValueError:
        return "Błąd konwersji"