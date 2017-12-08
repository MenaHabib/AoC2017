import numpy as np
import itertools
#---------------------------------------------------
#Part One
sum1 = 0
sum2 = 0
matrix = np.loadtxt('Day_2_input.txt',dtype=int)
for row in matrix:
    sum1 += max(row) - min(row)
print sum1
#---------------------------------------------------
#Part Two
for rows in matrix:
    l = list(itertools.combinations(rows, 2))
    for item in l:
        maxi = max(item)
        mini = min(item)
        if maxi%mini == 0:
            sum2 += maxx//minn
print sum2