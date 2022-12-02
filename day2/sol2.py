conv1 = {"A": 0, "B": 1, "C": 2}
conv2 = {"X": 0, "Y": 3, "Z": 6}

total_score = 0
with open("day2/input.txt", "r") as file:
    for line in file.read().split("\n"):
        vals = line.split()
        val1 = conv1[vals[0]]
        val2 = conv2[vals[1]]
        total_score += val2 + 1

        if val2 == 0: total_score += (val1 - 1) % 3
        elif val2 == 6: total_score += (val1 + 1) % 3
        else: total_score += val1

print(total_score)