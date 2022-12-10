dirs = []
with open("input.txt", "r") as file:
    depth = 0
    for line in file.readlines():
        if ".." in line:
            depth -= 1
            dirs[-2] += dirs[-1]
            dirs.insert(0, dirs.pop())

        elif "cd " in line:
            depth += 1
            dirs.append(0)

        else:
            cmd = line.split()
            if cmd[0].isnumeric():
                dirs[-1] += int(cmd[0])

    for _ in range(depth-1):
        dirs[-2] += dirs[-1]
        dirs.insert(0, dirs.pop())

print(sum([size for size in dirs if size <= 100000]))
print(min([size for size in dirs if size >= dirs[-1] - 40000000]))