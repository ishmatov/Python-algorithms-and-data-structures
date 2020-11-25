# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# https://drive.google.com/file/d/1Ej_8Z0JNDy3FwYY_Xv4ThGMDIPg00KnN/view?usp=sharing


a = int(input("Введите трехзначное число: "))
n1 = a // 100
n2 = (a - n1 * 100) // 10
n3 = a % 10
sum = n1 + n2 + n3
op = n1 * n2 * n3
print(f'Сумма цифр в числе {a} = {sum}')
print(f'Произведение цифр в числе {a} = {op}')
