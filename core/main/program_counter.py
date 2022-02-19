class ProgramCounter:

    def __init__(self) -> None:
        self.instructions = []
        self.pointer = float

    def get_next_instruction(self):
        self.pointer = self.pointer + 1
        return self.instructions[self.pointer]

    def get_current_instruction(self):
        return self.instructions[self.pointer]

    def set_instructions(self, instructions):
        self.instructions = instructions
        self.pointer = 0
