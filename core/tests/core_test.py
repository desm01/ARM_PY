from main.core import Core
from main.reg import Reg

def test_add():
    reg1 = Reg()
    reg1.update_value(100)

    reg2 = Reg()
    reg2.update_value(200)

    core = Core()
    core.add("R1", reg1, reg2)
    
    assert core.get_value("R1") == 100 + 200

def test_sub():
    reg1 = Reg()
    reg1.update_value(100)

    reg2 = Reg()
    reg2.update_value(200)

    core = Core()
    core.sub("R1", reg1, reg2)
    
    assert core.get_value("R1") == 100 - 200

def test_rsb():
    core = Core()
    reg1 = Reg()
    reg1.update_value(20)

    reg2 = Reg()
    reg2.update_value(230)

    core.rsb("R1", reg1, reg2)

    assert core.get_value("R1") == 230 - 20

