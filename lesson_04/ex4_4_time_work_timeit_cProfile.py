import timeit
import cProfile


def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def myfun_timeit(ff):
    timeit.timeit(ff, number=100, globals=globals())


def myfun_cProfile(ff):
    cProfile.run(ff)


# print(timeit.timeit('myfun_timeit("fib(2)")', number=1, globals=globals()))
# print(timeit.timeit('myfun_timeit("fib(4)")', number=1, globals=globals()))
# print(timeit.timeit('myfun_timeit("fib(8)")', number=1, globals=globals()))
print(timeit.timeit('myfun_timeit("fib(16)")', number=1, globals=globals()))
#
#
# cProfile.run('myfun_cProfile("fib(2)")')
# cProfile.run('myfun_cProfile("fib(4)")')
# cProfile.run('myfun_cProfile("fib(8)")')
cProfile.run('myfun_cProfile("fib(16)")')
