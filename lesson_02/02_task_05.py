# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
# https://drive.google.com/file/d/1FPnd5F3LxH1CDb9UhmSlhPxJ5mPaxDr5/view?usp=sharing


start_code = 32
end_code = 127
tab = 0

while start_code <= end_code:
    if tab == 10:
        print()
        tab = 0
    print(f'{start_code} | {chr(start_code)}', end='\t || \t')
    start_code += 1
    tab += 1
