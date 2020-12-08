# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

numbers = [_ for _ in range(2, 10)]
array = [_ for _ in range(2, 100)]
print(array)
arr_total = [0] * 8

for item in array:
    for i, el in enumerate(numbers):
        if item % el == 0:
            arr_total[i] += 1

for i in numbers:
    print(f'{i} -> {arr_total[i - 2]}')
