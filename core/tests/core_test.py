from main.core import Core
from main.reg import Reg

def test_add():
    assert 55 + 66 == Core().add(Reg(55), Reg(66))

def test_sub():
    assert 55-66 == Core().sub(Reg(55), Reg(66))

def test_rsb():
    assert 120-80 == Core().rsb(Reg(80), Reg(120))