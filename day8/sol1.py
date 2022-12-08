import numpy as np

with open("day8/input.txt", "r") as file:
    heights = np.array([[int(c) for c in s if c.isnumeric()] for s in file.readlines()])
    visible = np.ones(heights.shape)
    visible[1:-1, 1:-1] = 0

    for _ in range(2):
        for y in range(1, heights.shape[0] - 1):
            largest = heights[y, 0]
            
            for x in range(1, heights.shape[1] - 1):
                if heights[y, x] > largest:
                    visible[y, x] = 1
                    largest = heights[y, x]
                
        for y in range(1, heights.shape[0] - 1):
            largest = heights[y, heights.shape[1] - 1]
            
            for x in range(heights.shape[1] - 2, 0, -1):
                if heights[y, x] > largest:
                    visible[y, x] = 1
                    largest = heights[y, x]
        
        heights = heights.T
        visible = visible.T
    
    print(visible.sum())