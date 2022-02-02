from main.reg import Reg

def test_updating_reg_value():
    reg = Reg()
    reg.update_value(50)
    reg.update_value(100)
    assert reg.get_value() == 100