class CPU():
    def __init__(self) -> None:
        self.cycle = 0
        self.register = 1
        self.signal_strength = 0
        self.crt = [["." for _ in range(40)] for _ in range(6)]

        self.cycles = [20 + 40 * i for i in range(6)]
    
    def update_crt(self):
        sprite_pos = [self.register + i for i in range(1, -2, -1)]
        row = self.cycle // 40
        col = self.cycle % 40

        if col in sprite_pos:
            self.crt[row][col] = "#"
    
    def update_cycle(self, n):
        for _ in range(n):
            self.update_crt()

            self.cycle += 1

            if self.cycle in self.cycles:
                self.signal_strength += self.cycle * self.register
    
    def update_register(self, value):
        self.register += int(value)
    
    def execute_instruction(self, instruction):
        if "noop" in instruction:
            self.update_cycle(1)
        
        elif "addx" in instruction:
            self.update_cycle(2)

            _, value = instruction.split()
            self.update_register(value)


def sol(instructions : list[str]):
    cpu = CPU()

    for instruction in instructions:
        cpu.execute_instruction(instruction)
    
    for row in cpu.crt:
        for col in row:
            print(col, end="")
        print()
    
    return cpu.signal_strength


with open("input.txt", "r") as file:
    instructions = file.readlines()

print(sol(instructions))