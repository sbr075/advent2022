import string
all_chars = string.ascii_lowercase + string.ascii_uppercase
priority = {all_chars[c]:c+1 for c in range(all_chars)}

total_sum = 0
with open("day3/input.txt", "r") as file:
    for line in file.read().split("\n"):
        half = int(len(line) / 2)
        comp1, comp2 = line[:half], line[half:]
        both = set(comp1).intersection(comp2)
        total_sum += sum([priority[c] for c in both])

print(total_sum)