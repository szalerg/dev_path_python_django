# explain_code.md
"""
Zadanie: przeanalizuj powyższy kod i opisz, co jest źle, jak naprawić, co można ulepszyć
"""
Błąd: Funkcji dodaj wykonuje odejmowanie zamiast dodawania.
Poprawka: Zmienić 'return a - b' na 'return a + b'.
Ulepszenie: Dodać docstring i typy argumentów:
def dodaj(a: int, b: int) -> int:
    """Zwraca sumę dwóch liczb całkowitych."""

Błąd: Brak obsługi dzielenia przez zero.
Poprawka: Dodać warunek:
if b == 0:
    raise ValueError("Nie można dzielić przez zero")
return a / b
Ulepszenie: Dodać docstring i typy argumentów.
