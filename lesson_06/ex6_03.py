import sys
import ctypes
import struct

a = 42
print(id(a))  # адрес а памяти
print(sys.getsizeof(a))  # кол-во памяти
print(ctypes.string_at(id(a), sys.getsizeof(a)))  # берём область памяти начиная с _ и кол-вом _
# счётчик           | указатель типа | значение
# b'\n\x00\x00\x00(\x91+`\x01\x00\x00\x00*\x00'
print(chr(42))

#                   'HHLHHH' - шаблон байт который нужно взять (см. документацию)
print(struct.unpack('HHLHHH', ctypes.string_at(id(a), sys.getsizeof(a))))
# (11, 0, 1613467944, 1, 0, 42)
print(id(int))
# 1613467944

