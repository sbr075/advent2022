def overlaps(s1, s2):
    return not(s1[0] > s2[1] or s1[1] < s2[0])

overlap = 0
with open("input.txt", "r") as file:
    lines = [line.split(",") for line in file.readlines()]

    for line in lines:
        s1, s2 = [[int(s) for s in l.split("-")] for l in line]

        if overlaps(s1, s2):
            overlap += 1

print(overlap)