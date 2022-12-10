import numpy as np

with open("input.txt", "r") as file:
    heights = np.array([[int(c) for c in s if c.isnumeric()] for s in file.readlines()])
    score = np.zeros(heights.shape)

    for y in range(1, heights.shape[0] - 1):
        for x in range(1, heights.shape[1] - 1):
            col1, col2 = heights[:y, x][::-1], heights[y+1:, x]
            row1, row2 = heights[y, :x][::-1], heights[y, x+1:]

            s = 1
            height = heights[y, x]
            for trees in [col1, col2, row1, row2]:
                for i in range(len(trees)):
                    if trees[i] >= height: break
                
                s *= i+1

            score[y, x] = s

    print(score.max())
