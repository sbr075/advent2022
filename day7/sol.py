def get_dir_size(file):
    size = 0
    while (line := file.readline()):
        if "$" in line:
            file.seek(x)
            return size

        cmd = line.split()
        if cmd[0].isnumeric():
            size += int(cmd[0])
        
        x = file.tell()
    
    return size


def update_dirs(dirs, dir, size):
    if dir in dirs:
        addon = 1
        while f"{dir}_{addon}" in dirs:
            addon += 1
        
        dir = f"{dir}_{addon}"

    dirs[dir] = size


def get_dirs(file, dirs):
    size = 0
    while (line := file.readline()):
        if "ls" in line:
            size += get_dir_size(file)
        
        elif ".." in line:
            return size

        elif "cd" in line:
            cmd = line.split()
            dir_size = get_dirs(file, dirs)

            update_dirs(dirs, cmd[-1], dir_size)
            size += dir_size
    
    return size


with open("day7/input.txt", "r") as file:
    dirs = {}
    get_dirs(file, dirs)

    space_req = dirs["/"] - 40000000

    print(sum([size for size in dirs.values() if size <= 100000]))
    print(min([size for size in dirs.values() if size >= space_req]))