# Analizator tekstu
from collections import Counter

def analyze_text(text: str) -> dict:

    # Krok 1: Liczba znaków bez spacji
    chars_no_space = len(text.replace(" ", ""))

    # Krok 2: Liczba słów
    words = text.split()
    word_count = len(words)

    # Krok 3: Najczęściej występujący znak i słowo
    char_counter = Counter(text.replace(" ", ""))
    most_common_char = char_counter.most_common(1)[0][0]

    word_counter = Counter(words)
    most_common_word = word_counter.most_common(1)[0][0]

    # Krok 4: Samogłoski i spółgłoski
    vowels = "aeiouyąęó"
    vowel_count = sum(1 for c in text.lower() if c in vowels and c.isalpha())
    consonant_count = sum(1 for c in text.lower() if c.isalpha() and c not in vowels)

    # Krok 5: Zwróć słownik wyników
    return {
        "chars_no_space": chars_no_space,
        "word_count": word_count,
        "most_common_char": most_common_char,
        "most_common_word": most_common_word,
        "vowel_count": vowel_count,
        "consonant_count": consonant_count
    }

def main():

    while True:
        text = input("Podaj tekst (lub 'exit' aby zakończyć): ")
        if text.lower() == "exit":
            print("Do zobaczenia")
            break
        
        results = analyze_text(text)
        print("Statystyki:", results)

if __name__ == "__main__":
    main() 