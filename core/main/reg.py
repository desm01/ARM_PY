class Reg:

    def __init__(self, value):
        self.__value = value

    def update_value(self, new_value):
        self.__value = new_value

    def get_value(self):
        return self.__value