import timeit

a = [i for i in range(1000)]
print(timeit.timeit('a = [i for i in range(100)]', number=100))
print(timeit.timeit('a = [i for i in range(1000)]', number=100))
print(timeit.timeit('a = [i for i in range(10000)]', number=100))
print(timeit.timeit('a = [i for i in range(100000)]', number=100))


def func(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                a = i * j * k


s = """
def func(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                a = 1

func(5)
"""

print(timeit.timeit(s, number=100))
print(timeit.timeit('func(2)', number=100, globals=globals()))
print(timeit.timeit('func(4)', number=100, globals=globals()))
print(timeit.timeit('func(8)', number=100, globals=globals()))
print(timeit.timeit('func(16)', number=100, globals=globals()))