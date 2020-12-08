# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
# если введено число 3486, надо вывести 6843
# https://drive.google.com/file/d/1FPnd5F3LxH1CDb9UhmSlhPxJ5mPaxDr5/view?usp=sharing


def turn_over(n):
    if n < 10:
        return n
    if n >= 10:
        return f'{n % 10}{turn_over(n // 10)}'


num = int(input("Введите натуральное число: "))
tmp = num
s = ""
while tmp != 0:
    d = tmp % 10
    s += str(d)
    tmp //= 10

print(s)

f = turn_over(num)
print(f)
