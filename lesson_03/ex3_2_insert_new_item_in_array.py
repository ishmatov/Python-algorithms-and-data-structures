import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
# [94, 56, 22, 16, 7, 70, 23, 13, 42, 88]
# [94, 56, 777, 16, 7, 70, 23, 13, 42, 88]  - Замена
# [94, 56, 777, 22, 16, 7, 70, 23, 13, 42, 88]  - Вставка
num = 777
pos = 2
# array.insert(pos, num)
# print(array)

array.append(None)
print(array)
i = len(array) - 1
while i > pos:
    array[i], array[i - 1] = array[i - 1], array[i]
    i -= 1
    print(array)

array[pos] = num
print(array)

num = 999
pos = 4
array_new = array[:pos] + [num] + array[pos:]
print(array)
print(array_new)