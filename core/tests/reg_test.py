from main.reg import Reg

def test_setting_reg():
    reg = Reg(50)
    assert reg.get_value() == 50