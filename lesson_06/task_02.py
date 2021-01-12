import sys

a = 42
b = a
c = b
del b
print(sys.getrefcount(a))

print(sys.getsizeof(c))
c = 420
print(sys.getsizeof(c))
c = 42000000
print(sys.getsizeof(c))
# Для разных интерпритаторов Python цифры будут разные и так для x64 пямяти для хранения int переменной будет тратися
# в 2 два раза больше

f = 5.5
print(sys.getsizeof(f))
f = 56546432132165.564654646546464
print(sys.getsizeof(f))
print(f)
# Тип float занимает фиксированное кол-во байт и при выходе за пределы памяти просто огругляет его,
# Это может привести к потере данных и не точности при вычислении


