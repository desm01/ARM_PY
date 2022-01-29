class Core:

    def __init__(self):
        self.r1 = None
        self.r2 = None
        self.r3 = None

    def add(self, reg, reg2):
        return reg.get_value() + reg2.get_value()
    
    def sub(self, reg, reg2):
        return reg.get_value() - reg2.get_value()

    def rsb(self, reg, number):
        return number - reg.get_value()
