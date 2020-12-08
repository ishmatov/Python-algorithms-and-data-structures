import random

SIZE_M = 4
SIZE_N = 6
MIN_ITEM = 0
MAX_ITEM = 1000
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_N)] for _ in range(SIZE_M)]
print(*matrix, sep='\n')

sum_col = [0] * len(matrix[0])
print(sum_col)
print('*' * 50)

for line in matrix:
    sum_line = 0
    for i, item in enumerate(line):
        sum_line += item
        sum_col[i] += item
        print(f'{item:>5}', end='')
    print(f'\t|{sum_line}')

for item in sum_col:
    print(f'{item:>5}', end='')