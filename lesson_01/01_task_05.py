# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
# https://drive.google.com/file/d/1Ej_8Z0JNDy3FwYY_Xv4ThGMDIPg00KnN/view?usp=sharing


a = input("Введите первую букву: ")
b = input("Введите вторую букву: ")
na = ord(a) - 96
nb = ord(b) - 96
print(f'Порядковый номер буквы {a} - {na}')
print(f'Порядковый номер буквы {b} - {nb}')
c = abs(na-nb) - 1
print(f'Количество букв между буквами {a} и {b}: {c}')
