import pytest
from week03.tasks import loops

def test_zadanie_1(capsys):
    loops.zadanie_1(3)
    captured = capsys.readouterr()
    assert captured.out.strip() == "1\n2\n3"

def test_zadanie_2():
    assert loops.zadanie_2(5) == 15

def test_zadanie_3():
    assert loops.zadanie_3(5) == 120
