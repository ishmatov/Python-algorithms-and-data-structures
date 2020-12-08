# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

SIZE_M = 5
SIZE_N = 5
MIN_ITEM = 0
MAX_ITEM = 100
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_N)] for _ in range(SIZE_M)]
print(*matrix, sep='\n')
max_ = None

for line in matrix:
    min_line = line[0]
    for i, item in enumerate(line):
        if item < min_line:
            min_line = item
    if max_ is None or min_line > max_:
        max_ = min_line

print(max_)
