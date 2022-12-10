import string
priority = {string.ascii_letters[c]:c+1 for c in range(len(string.ascii_letters))}

total_sum = 0
with open("input2.txt", "r") as file:
    lines = file.read().splitlines()
    groups = [[set(l) for l in lines[i:i+3]] for i in range(0, len(lines), 3)]
    total_sum = sum([priority[set.intersection(*group).pop()] for group in groups])

print(total_sum)