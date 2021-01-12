# Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых
# трех уроков.

# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…

import timeit
import cProfile


def total_t(t: float, a: int) -> float:
    if a == 1:
        return t
    if a > 1:
        return t + total_t(t / 2 * -1, a - 1)


def sum_sequence_while(n: int) -> float:
    i = 1
    total = 1.0
    s = 1
    while i < n:
        s = s / 2 * -1
        total += s
        i += 1
    return total


def sum_sequence_inner_fun(n: int) -> float:
    total = [1]
    z = -1
    for i in range(1, n):
        total.append((2 ** -i) * z)
        z *= -1
    return sum(total)


# ------------------------------- timeit -------------------------------
start_sequence = 1
for i in range(1, 1001):
    print(timeit.timeit(f'total_t({start_sequence}, {i})', number=1000, globals=globals()))

for i in range(1, 1001):
    print(timeit.timeit(f'sum_sequence_while({i})', number=1000, globals=globals()))

for i in range(1, 1001):
    print(timeit.timeit(f'sum_sequence_inner_fun({i})', number=1000, globals=globals()))
# Результаты:
# https://docs.google.com/spreadsheets/d/e/2PACX-1vSR6rBkmOPOXXZeakZRrZwLR0cuYcQuvUJCNICCORGi-_XPFRxDuD1leUJM_I3D_h93SPman4rNErpS/pubhtml

# ------------------------------- cProfile -------------------------------
start_sequence = 1
cProfile.run(f'total_t({start_sequence}, 950)')
#       953 function calls (4 primitive calls) in 0.001 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#  950/1    0.001    0.000    0.001    0.001 04_task_01.py:10(total_t)
#      1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#      1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run(f'sum_sequence_while(1_000_000)')
#       4 function calls in 0.251 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.251    0.251    0.251    0.251 04_task_01.py:17(sum_sequence_while)
#      1    0.000    0.000    0.251    0.251 <string>:1(<module>)
#      1    0.000    0.000    0.251    0.251 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run(f'sum_sequence_inner_fun(1_000_000)')
#       1000004 function calls in 0.812 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.684    0.684    0.805    0.805 04_task_01.py:28(sum_sequence_inner_fun)
#      1    0.007    0.007    0.812    0.812 <string>:1(<module>)
#      1    0.000    0.000    0.812    0.812 {built-in method builtins.exec}
#      1    0.008    0.008    0.008    0.008 {built-in method builtins.sum}
# 999999    0.114    0.000    0.114    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
Линейная асимптотика
Вывод: По результатам замеров видно, что скорость выполнения возрастает линейно в зависимости от увеличения длинны 
строки.
Быстрее всего выполняется альгоритм написанный на уроке и использующий цикл while. Алгоритмы использующие рекурсию 
и встроеную функцию sum работают примерно одинаково, но при некоторых значениях имеются значительные пики с просадкой
времени выполнения, возможно это происходит из-за загрузки рабочей станции.
В дополнение к этому можем увидеть что алгоритм использующий рекуссию более не стабилен и производительность как падает,
так и возрастает на различных значениях, и на значении 995 рекусия наткнулась на ограничение.
Вывод вывода: Не каждый красиво написаный (короткий) алгоритм более оптимальный!
"""
