#Odczyt pliku
#Napisz funkcję, która wczyta cały plik tekstowy i zwróci jego zawartość jako string.
def reading():
    with open("file.txt", "r", encoding="utf-8") as file:
        txt = file.read()
    return txt

#Zapis do pliku
#Napisz funkcję, która przyjmie tekst i zapisze go do pliku output.txt.
def save(text):
    with open("output.txt", "w", encoding="utf-8") as file:
        file.write(text)
    
#Liczba linii
#Napisz funkcję, która policzy, ile linii znajduje się w podanym pliku.
def number():
    with open("number.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    return len(lines)
