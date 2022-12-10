import re

stack = {}
with open("input.txt", "r") as file:
    inp = file.read().split("\n\n")
    stacks = inp[0].split("\n")
    instructions = inp[1].split("\n")

    for layer in stacks:
        for pos, char in enumerate(layer):
            if char.isalpha():
                pos = (pos - 1) // 4 + 1
                stack[pos] = [char] + stack[pos] if pos in stack else [char]
    
    for instruction in instructions:
        ins = re.findall(r'\d+', instruction)
        amount = int(ins[0])
        prev = int(ins[1])
        curr = int(ins[2])

        stack[curr].extend(stack[prev][-amount:][::-1])
        del stack[prev][-amount:]

    msg = ''.join([stack[key][-1] for key in sorted(stack.keys())])
    print(msg)