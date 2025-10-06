from week04.tasks import errors

def test_division():
    assert errors.division(10, 2) == 5
    assert errors.division(5, 0) == "Nie dziel przez zero!"

def test_conversion():
    assert errors.conversion("123") == 123
    assert errors.conversion("abc") == "Błąd konwersji"
    assert errors.conversion("12.5") == "Float, a nie int"