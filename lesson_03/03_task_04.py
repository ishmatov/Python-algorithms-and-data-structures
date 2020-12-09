# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 15
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
count = 0
num = array[0]
i = j = 0
for i in range(0, SIZE - 1):
    spam = 0
    for j in range(0, SIZE - 1):
        if array[i] == array[j]:
            spam += 1
            if spam > count:
                num = array[i]
                count = spam
                break  # Требуется найти число в массиве, а не кол-во вхождений, поэтому инициируем выход, если нашли
                # число вхождений больше, чем было найдено ранее

print(num)
