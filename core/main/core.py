
from main.stack_pointer import StackPointer
from main.link_register import LinkRegister
from main.program_counter import ProgramCounter
from main.reg import Reg

class Core:

    def __init__(self):
        self.registers = {
            "R1": Reg(),
            "R2": Reg(),
            "R3": Reg(),
            "R4": Reg(),
            "R5": Reg(),
            "R6": Reg(),
            "R7": Reg(),
            "R8": Reg(),
            "R9": Reg(),
            "R10": Reg(),
            "R11": Reg(),
            "R12": Reg(),
            "SP": StackPointer(),
            "LR": LinkRegister(),
            "PC": ProgramCounter()
        }

    def get_value(self, regReference):
        return self.registers.get(regReference).get_value()

    def set_value(self, regReference, value):
        return self.registers.get(regReference).update_value(value)

    def add(self, store, reg, reg2):
        return self.registers.get(store).update_value(reg.get_value() + reg2.get_value())
    
    def sub(self, store, reg, reg2):
        return self.registers.get(store).update_value(reg.get_value() - reg2.get_value())

    def rsb(self, store, reg, reg2):
        return self.sub(store, reg2, reg)
