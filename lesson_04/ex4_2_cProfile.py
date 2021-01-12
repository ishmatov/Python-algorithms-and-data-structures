import cProfile


def get_len(lst):
    return len(lst)


def get_sum(lst):
    s = 0
    for item in lst:
        s += item
    return s


def main(n):
    array = [i for i in range(n)]
    len_ = get_len(array)
    sum_ = get_sum(array)
    sum_ = get_sum(array)
    sum_ = sum(array)


cProfile.run('main(1_000_000)')
