from geo.calc import Calc, Distance


def test_add():
    assert Calc().add(2, 3) == 5, 'Should be 5'


def test_mul():
    assert Calc().multiply(2, 3) == 6, 'Should be 6'


def test_power():
    assert Distance(2).power(2) == 4, 'Should be 4'
