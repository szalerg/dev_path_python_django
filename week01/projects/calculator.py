# calculator.py
"""
Projekt tygodnia: prosty kalkulator tekstowy.
Obsługuje: +, -, *, /, mod, ^, sqrt, nawiasy, błędy dzielenia przez 0
"""
import math

def kalkulator():
    """
    Prosty kalkulator tekstowy.
    Kalkulator obsługej działania: +, -, *, /, mod, ^, sqrt
    Cały program działa w pętli, aż użytkownik wpuisze 'exit'.
    """
    while True:
        expression = input("Podaje działanie (np. 2 + 3, 4 * 5, sqrt(9)): ")    # Pobierania wyrażeń od użytkownika


        if expression.lower() == "exit":                                        # Warunek wyjścia z pętli
            print("Wyłączony")
            break

        expression = expression.replace("mod", "%")                             # Dzielenie
        expression = expression.replace("^", "**")                              # Potęgowanie
        expression = expression.replace("sqrt", "math.sqrt")                    # Pierwiastek kwadratowy

        try:                                                                            
                                                                                # Liczenie wyniku wyrażeń
            result = eval(expression)

            print("Wynik:", round(result, 2))

        except ZeroDivisionError:
            print("Błąd dzielenia przez zero!")                                 # Obsługa dzielenia przez zero

        except Exception as e: 

            print("Błąd w wyrażeniu:", e)                                       # Obsługa innych błędów 