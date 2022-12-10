import string
priority = {string.ascii_letters[c]:c+1 for c in range(len(string.ascii_letters))}

total_sum = 0
with open("input.txt", "r") as file:
    for line in file.readlines():
        half = len(line) // 2
        comp1, comp2 = line[:half], line[half:]
        both = set(comp1).intersection(comp2)
        total_sum += sum([priority[c] for c in both])

print(total_sum)