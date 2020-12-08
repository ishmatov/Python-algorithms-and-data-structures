import random

SIZE = 10_000
MIN_ITEM = 0
MAX_ITEM = 100_000_000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
array.sort()  # только для этой задачи, а не для практикических задач
print(array)

find = int(input("Введите целое число для поиска: "))
pos = len(array) // 2
left = 0
right = len(array) - 1
count = 1
while array[pos] != find and left <= right:
    count += 1
    if find > array[pos]:
        left = pos + 1
        # pos = (left + right) // 2
    elif find < array[pos]:
        right = pos - 1
    pos = (left + right) // 2

print('Элемент отсутствует' if left > right else f'Позиция искомого элемента {pos}')
print(f'{count=}')
