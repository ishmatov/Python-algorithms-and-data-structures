# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
min_ = 0
max_ = 0

for i, item in enumerate(array):
    if item < array[min_]:
        min_ = i
    if item > array[max_]:
        max_ = i

array[min_], array[max_] = array[max_], array[min_]

print(array)
