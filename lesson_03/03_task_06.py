# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами
# минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
min_ = 0
max_ = 0

for i, item in enumerate(array):
    if item <= array[min_]:
        min_ = i
    if item >= array[max_]:
        max_ = i

print(array[min_])
print(array[max_])

sum_ = 0
if min_ < max_:
    start, finish = min_, max_
else:
    start, finish = max_, min_

for i in range(start + 1, finish):
    sum_ += array[i]

print(f'Сумма элементов = {sum_}' if sum_ > 0 else f'Максимальный и минимальные элементы стоят рядом')
