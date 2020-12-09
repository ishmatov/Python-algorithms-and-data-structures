# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

SIZE_L = 5
SIZE_C = 4
MIN_ITEM = 0
MAX_ITEM = 100
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_C)] for _ in range(SIZE_L)]
print(*matrix, sep='\n')
max_ = None

for i in range(0, SIZE_C):
    min_col = matrix[0][i]
    for j in range(0, SIZE_L):
        if matrix[j][i] < min_col:
            min_col = matrix[j][i]
    print(min_col)
    if max_ is None or min_col > max_:
        max_ = min_col

print(max_)
