# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве. Примечание к
# задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.

import random

SIZE = 15
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_ = None
max_pos = 0
for i, item in enumerate(array):
    if item < 0:
        if max_ is None:
            max_ = item
        if item > max_:
            max_ = item
            max_pos = i

print(f'"{max_}" - максимальное из отрицательных чисел на позиции {max_pos}')
