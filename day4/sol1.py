def contains(s1, s2):
    return s1[0] >= s2[0] and s1[1] <= s2[1] 

fully_contained = 0
with open("day4/input.txt", "r") as file:
    for line in file.read().split("\n"):
        s1, s2 = [[int(s) for s in section.split("-")] for section in line.split(",")]

        if contains(s1, s2) or contains(s2, s1):
            fully_contained += 1

print(fully_contained)