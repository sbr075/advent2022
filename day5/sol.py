import string
import re

stack = {}
with open("day5/input.txt", "r") as file:
    inp = file.read().split("\n\n")
    stacks = inp[0].split("\n")
    instructions = inp[1].split("\n")

    for layer in stacks:
        for pos, char in enumerate(layer):
            if char in string.ascii_uppercase:
                stack[pos] = stack[pos] + [char] if pos in stack else [char]

    keys = sorted(list(stack.keys()))
    for idx, key in enumerate(keys):
        stack[idx + 1] = stack.pop(key)[::-1]

    for instruction in instructions:
        ins = list(map(int, re.findall(r'\d+', instruction)))
        amount = ins[0]
        prev = ins[1]
        curr = ins[2]

        stack[curr].extend(stack[prev][-amount:][::-1])
        del stack[prev][-amount:]

    msg = ""
    for _, val in stack.items():
        msg += val[-1]
    
    print(msg)

# remove [::-1] from line 25 to get puzzle 2 solution