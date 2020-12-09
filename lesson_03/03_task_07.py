# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба
# являться минимальными), так и различаться.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

first_min = array[0]
first_min_pos = 0

second_min_pos = 0

for i, item in enumerate(array):
    if item <= array[first_min_pos]:
        first_min_pos = i

for i, item in enumerate(array):
    if item <= array[second_min_pos] and i != first_min_pos:
        second_min_pos = i

print(array[first_min_pos])
print(array[second_min_pos])
