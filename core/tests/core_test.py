from main.core import Core

def test_add():
    assert 55 + 66 == Core().add(55,66)

def test_sub():
    assert 55-66 == Core().sub(55,66)