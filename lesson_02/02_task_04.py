# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
# https://drive.google.com/file/d/1FPnd5F3LxH1CDb9UhmSlhPxJ5mPaxDr5/view?usp=sharing


def total_t(t: float, a: int) -> float:
    if a == 1:
        print(t, end=' ')
        return t
    if a > 1:
        print(t, end=' ')
        return t + total_t(t/2 * -1, a-1)


i = 1
total = 1.0
s = 1
n = int(input("Введите кол-во элементов последовательности: "))
print(s, end=' ')
while i < n:
    s = s/2 * -1
    print(s, end=' ')
    total += s
    i += 1
print(f'\nИтого: {total}')

start_sequence = 1
tt = total_t(start_sequence, n)
print(f'\nИтого: {tt}')
