# Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции
# вводятся пользователем. После выполнения вычисления программа не завершается, а запрашивает новые данные для
# вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если
# пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), программа должна сообщать об ошибке и снова
# запрашивать знак операции. Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его
# в качестве делителя.
# https://drive.google.com/file/d/1FPnd5F3LxH1CDb9UhmSlhPxJ5mPaxDr5/view?usp=sharing


import sys


def calc(x, y, operand):
    if operand == "+":
        return x + y
    if operand == "-":
        return x - y
    if operand == "*":
        return x * y
    if operand == "/":
        return x / y


while True:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    while True:
        op = input("Введите знак операции над числами ('+', '-', '*', '/'). Для выхода '0': ")
        if len(op) == 1 and op in "+-*/0":
            if op == "0":
                print("До свидания!")
                sys.exit()
            elif op == "/" and b == 0:
                print("На ноль делить нельзя")
            else:
                print(f'{a} {op} {b} = {calc(a, b, op)}')
            break
        else:
            print("Вы ввели не верный знак операции, попробуйте ещё раз")
