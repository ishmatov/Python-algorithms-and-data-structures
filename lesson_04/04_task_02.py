# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена». Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из
# прошлых уроков. Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
#
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.
# Пример работы программ:
#
# sieve(2)
# 3
# prime(4)
# 7
# sieve(5)
# 11
# prime(1)
# 2
import math


def sieve(index: int):
    if index in (1, 2):
        n = index + 2
    else:
        n = 2
        while (n / math.log(n)) <= index:
            n += 1
    # n += 1
    a = [0] * n  # создание массива с n количеством элементов
    for i in range(n):  # заполнение массива ...
        a[i] = i  # значениями от 0 до n-1

        # вторым элементом является единица, которую не считают простым числом
        # забиваем ее нулем.
    a[1] = 0
    m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)

    while m < n:  # перебор всех элементов до заданного числа
        if a[m] != 0:  # если он не равен нулю, то
            j = m * 2  # увеличить в два раза (текущий элемент - простое число)
            while j < n:
                a[j] = 0  # заменить на 0
                j = j + m  # перейти в позицию на m больше
        m += 1

    return max(a)


def prime(n: int) -> int:
    i = 2
    count = 0
    while i < float('inf'):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            count += 1
            if count == n:
                return i
        i += 1


index_ = int(input("Введите индекс порядковый номер простого числа: \n"))
print(f'№{index_} в последовательности простых числе - это число {sieve(index_)}')
print(prime(index_))