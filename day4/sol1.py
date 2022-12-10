def contains(s1, s2):
    return s1[0] >= s2[0] and s1[1] <= s2[1] 

fully_contained = 0
with open("input.txt", "r") as file:
    lines = [line.split(",") for line in file.readlines()]
    for line in lines:
        s1, s2 = [[int(s) for s in l.split("-")] for l in line]

        if contains(s1, s2) or contains(s2, s1):
            fully_contained += 1

print(fully_contained)