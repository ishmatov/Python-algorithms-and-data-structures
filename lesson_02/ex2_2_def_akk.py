import  sys


def akk(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return akk(m - 1, 1)
    elif m > 0 and n > 0:
        return akk(m - 1, akk(m, n - 1))


def akk_shot(m, n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return akk(m - 1, 1)
    return akk(m - 1, akk(m, n - 1))


sys.setrecursionlimit(10000)
a = int(input("Введите целое положительное число: "))
b = int(input("Введите целое положительное число: "))
z = akk(a, b)
print(z)
