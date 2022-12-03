import string
priority = {(string.ascii_lowercase + string.ascii_uppercase)[c]:c+1 for c in range(len(string.ascii_lowercase) + len(string.ascii_uppercase))}

total_sum = 0
with open("day3/input2.txt", "r") as file:
    lines = file.read().split("\n")
    groups = [lines[i:i+3] for i in range(0, len(lines), 3)]
    
    for group in groups:
        common = set(group[0])
        for items in group[1:]:
            common = common.intersection(items)

        total_sum += sum([priority[c] for c in common])

print(total_sum)