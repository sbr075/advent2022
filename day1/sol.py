with open("input.txt", "r") as file:
    calories_split = [s.split() for s in file.read().split("\n\n")]
    calories_sum   = [sum([int(c) for c in l]) for l in calories_split]
    calories_top   = sum(sorted(calories_sum, key=lambda x: -x)[:3])

print(calories_top)