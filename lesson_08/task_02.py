h_list = [None] * 26


def my_hash(value):
    m_hash = ord(value[0]) - ord('a')
    h_list[m_hash] = value
    print(h_list)


a = 'apple'
my_hash(a)

b = 'banana'
my_hash(b)

c = 'bear'
my_hash(c)

print(9876 == 9*10**3 + 8*10**2 + 7*10**1 + 6*10**0)


def my_hash_2(value):
    letter = 26
    m_hash = 0
    size = 10_000
    for index, char in enumerate(value):
        m_hash += (ord(char) - ord('a') + 1) * letter ** index
    return m_hash % size


print(my_hash_2(a))
print(my_hash_2(b))
print(my_hash_2(c))
print(my_hash_2('verybigstring'))
