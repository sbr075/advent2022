def convert_to_range(section):
    section = [int(s) for s in section.split("-")]
    return range(section[0], section[1]+1)

overlap = 0
with open("day4/input.txt", "r") as file:
    for line in file.read().split("\n"):
        section1, section2 = [convert_to_range(section) for section in line.split(",")]

        if set(section1).intersection(section2):
            overlap += 1

print(overlap)