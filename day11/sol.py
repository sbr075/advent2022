import re

def parse_input():
    with open("day11/input.txt", "r") as file:
        lines = file.readlines()
        data = [lines[i:i+6] for i in range(0, len(lines), 7)]

        monkeys = {}
        for nr, monkey in enumerate(data):
            items     = monkey[1]
            operation = monkey[2].split()
            divisor   = int(monkey[3].split()[-1])
            throws    = [int(m) for m in re.findall(r"\d+", monkey[4] + monkey[5])]

            monkeys[nr] = {
                "worries": [int(worry) for worry in re.findall(r"\d+", items)],
                "operation": {
                    "operator": operation[-2],
                    "value": operation[-1]
                },
                "divisor": divisor,
                "throws": throws,
                "inspected": 0
            }

    return monkeys

def sol(rounds : int, mod : int = None):
    monkeys = parse_input()

    for _ in range(rounds):
        for _, b in monkeys.items():
            worries  = b["worries"]
            operator = b["operation"]["operator"]
            value    = b["operation"]["value"]
            divisor  = b["divisor"]

            b["inspected"] += len(worries)
            
            while len(worries) > 0:
                worry = worries.pop()

                if value == "old":
                    if operator == "*":
                        worry *= worry
                    else:
                        worry += worry
                else:
                    if operator == "*":
                        worry *= int(value)
                    else:
                        worry += int(value)
                
                if mod is not None:
                    worry %= mod
                
                else:
                    worry //= 3
                
                throw = b["throws"][0] if worry % divisor == 0 else b["throws"][1]
                monkeys[throw]["worries"].append(worry)

    inspections = sorted([b["inspected"] for _, b in monkeys.items()])[-2:]
    return inspections[0] * inspections[1]

print(sol(rounds=20))
print(sol(rounds=10000, mod=9699690))