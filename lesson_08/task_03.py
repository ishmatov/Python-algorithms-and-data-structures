import hashlib
import hmac

print(hash('sldfgjl;skdfj;sldfj;slkdf'))
print(hash('sldfgjl;skdfj;sldfj;slkdf'))
print(hash('sldfgjl;skdfj;sldfj;slkdf'))
# 473784867
# hash - работает быстро, но при разных запусках даёт разный результат,
# поэтому можно использовать только в рамках одной сессии

print(hashlib.sha256(b'Hello world'))  # Функция принимает не строку а набор байт
print(hashlib.sha256(b'Hello world') == hashlib.sha256(
    b'Hello world'))  # Вернёт False потому что сравнивается два объекта в оперативной памяти


print(hashlib.sha256(b'Hello world').hexdigest())  # 16-ти ричное представление
print(hashlib.sha256(b'Hello world').hexdigest() == hashlib.sha256(b'Hello world').hexdigest())  # True

print(hashlib.sha256('Привет мир'.encode('utf-8')).hexdigest())

print(hmac.new(key=b'dsgwrvwev', msg='Привет мир'.encode('utf-8'), digestmod=hashlib.sha512).hexdigest())
