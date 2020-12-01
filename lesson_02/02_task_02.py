# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3 четные
# цифры (4, 6 и 0) и 2 нечетные (3 и 5).
# https://drive.google.com/file/d/1FPnd5F3LxH1CDb9UhmSlhPxJ5mPaxDr5/view?usp=sharing


def even(n):
    if n % 2 == 0:
        return 1
    return 0


num = int(input("Введите натуральное число: "))
tmp = num
len_d = len(str(num))
e = 0
while tmp != 0:
    d = tmp % 10
    e += even(d)
    tmp //= 10

print(f'В числе {num} четных цифр - {e}, не чётных - {len_d - e}')


