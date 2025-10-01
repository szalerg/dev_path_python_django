import pytest
from week04.tasks import files

def test_reading():
    files.save("Cześć Gacek!")                      # zapisujemy do pliku
    assert files.reading() == "Cześć Gacek!"        # odczytujemy i porównujemy

def test_save_and_read():
    files.save("Testowy zapis")
    assert files.reading() == "Testowy zapis"

def test_number():
    assert files.number() == 3
