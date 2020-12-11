import timeit
import cProfile


def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


print(timeit.timeit('fib(2)', number=100, globals=globals()))
print(timeit.timeit('fib(4)', number=100, globals=globals()))
print(timeit.timeit('fib(8)', number=100, globals=globals()))
print(timeit.timeit('fib(16)', number=100, globals=globals()))

cProfile.run('fib(2)')
cProfile.run('fib(4)')
cProfile.run('fib(8)')
cProfile.run('fib(16)')


# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.001    0.001 <string>:1(<module>)
# 3193/1    0.001    0.000    0.001    0.001 ex4_3_task3.py:5(fib)
#      1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Вариан через цикл


def fib_loop(n):
    if n < 2:
        return n
    first = 0
    second = 1
    for i in range(n):
        first, second = second, first + second
    return first


print(timeit.timeit('fib_loop(2)', number=100, globals=globals()))  # 5.940000000000112e-05
print(timeit.timeit('fib_loop(20)', number=100, globals=globals()))  # 0.00017300000000000648
print(timeit.timeit('fib_loop(200)', number=100, globals=globals()))  # 0.0019930999999999977
print(timeit.timeit('fib_loop(2000)', number=100, globals=globals()))  # 0.0716981


cProfile.run('fib_loop(100_000)')


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')

# test_fib(fib)
# test_fib(fib_loop)
