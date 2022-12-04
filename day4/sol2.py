def overlaps(s1, s2):
    return not(s1[0] > s2[1] or s1[1] < s2[0])

overlap = 0
with open("day4/input.txt", "r") as file:
    for line in file.readlines():
        s1, s2 = [[int(s) for s in section.split("-")] for section in line.split(",")]

        if overlaps(s1, s2) or overlaps(s2, s1):
            overlap += 1

print(overlap)