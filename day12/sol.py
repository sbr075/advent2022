import numpy as np

def parse_input():
    start, end = None, None
    
    with open("day12/input.txt", "r") as file:
        elevations = []
        for y, row in enumerate(file.readlines()):
            values = []
            for x, col in enumerate(row):
                if col == "\n": continue

                if col.islower():
                    values.append(ord(col) - 96)
                
                elif col == "S":
                    values.append(1)
                    start = (y, x)
                
                elif col == "E":
                    values.append(26)
                    end = (y, x)
            
            elevations.append(values)
    
    return elevations, start, end


def get_neighbors(elevations : np.array, y : int, x : int, v : set, opposite : bool = False):
    neighbors = []
    for p in [(y - 1, x),(y + 1, x),(y, x - 1),(y, x + 1)]:
        if p in v: continue
        if not(0 <= p[0] < elevations.shape[0] and 0 <= p[1] < elevations.shape[1]): continue
        
        if not opposite:
            if elevations[p] - elevations[y, x] > 1: continue

        else:
            if elevations[y, x] - elevations[p] > 1: continue

        neighbors.append(p)
    
    return neighbors


def sol(elevations : np.array, start : tuple, end : tuple):
    stack = [[0, start]]
    v = set([(0,0)])
    while True:
        c = stack[0][0]
        p = stack[0][1]

        if end:
            if p == end: break
        else:
            if elevations[p] == 1: break

        vs = get_neighbors(elevations, p[0], p[1], v, end is None)
        v|=set(vs)

        del stack[0]
        stack += [[c+1, p] for p in vs]
        stack = sorted(stack, key=lambda x: x[0])
    
    print(stack[0][0])


elevations, start, end = parse_input()
sol(np.array(elevations), start, end)
sol(np.array(elevations), end, None)