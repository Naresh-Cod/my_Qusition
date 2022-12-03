# python program to add two Matrices

import numpy as np
x = np.arange(20).reshape(5, 4)
y = np.arange(20).reshape(5, 4)

print(x + y)

# program to add two matrices using nested loop

x = [[33, 66, 5],
     [5, 33, 99],
     [99, 4, 33]]

y = [[4, 7, 4],
     [3, 8, 9],
     [3, 5, 8]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# iterate through rows
for i in range(len(x)):
     for j in range(len(x[0])):
          result[i][j] = x[i][j] + y[i][j]

for r in result:
     print(r)
