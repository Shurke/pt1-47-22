"""
Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
Учитывать только английские буквы
"""

str_1 = input('Введите строку:')
sum_small = 0
sum_big = 0
for word in str_1:
    if 'a' <= word <= 'z':
        sum_small = sum_small + 1
    elif 'A' <= word <= 'Z':
        sum_big = sum_big + 1
print('Сумма строчных букв =', sum_small)
print('Сумма прописных букв =', sum_big)
