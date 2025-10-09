from week04.tasks import modules

def test_square_root():
    assert modules.square_root(9) == 3.0
    assert modules.square_root(25) == 5.0
    assert round(modules.square_root(2), 5) == 1.41421

def test_rng():
    for _ in range(100):
        result = modules.rng(1, 10)
        assert 1 <= result <= 10
