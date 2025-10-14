"""
Mini Notatnik
Stwórz program, który:

pozwala użytkownikowi dodać notatkę (zapis do pliku),

wyświetli wszystkie notatki (odczyt pliku),

umożliwia zakończenie programu wpisując "exit".
"""

def mini_notebook():

    while True:
        user_input = input("Wpisz notatkę ('show' aby wyświetlić, 'exit' aby zakończyć): ")

        if user_input == "exit":
            break

        elif user_input == "show":
            try:
                with open("notes.txt", "r") as file:
                    for line in file:
                        print(line.strip())
            except FileNotFoundError:
                print("Brak notatek.")            
            
        else:
            with open("notes.txt", "a") as file:
                file.write(user_input + "\n")