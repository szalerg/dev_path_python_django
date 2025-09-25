# guess_the_number.py
"""
Projekt tygodnia: Gra "Zgadnij liczbę"

1. Komputer losuje liczbę z zakresu 1–100.
2. Użytkownik zgaduje, a program podpowiada:
   - "Za dużo!"
   - "Za mało!"
   - "Zgadłeś!"
3. Gra trwa do odgadnięcia liczby.
"""
import random

def mini_game():
   while True:  # pętla główna gry
      RNG = random.randint(1, 100)
      number_of_trials = 0
      
      while True:  # pętla zgadywania
         print("Zgadnij liczbę od 1 do 100")
         guess = int(input("Wpisz liczbę: "))
         number_of_trials += 1
         
         if guess < RNG:
            print("Za mało!")
         elif guess > RNG:
            print("Za dużo!")
         else:
            print("Zgadłeś!")
            print(f"Udało Ci się w {number_of_trials} próbach.")
            break
      
      play_again = input("Czy chcesz zagrać ponownie? (tak/nie): ")
      if play_again.lower() != "tak":
         print("Dzięki za grę! 👋")
         break

mini_game()         
