"""
Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
Учитывать только английские буквы
"""

str_1 = input('Введите строку:')
LETTER_LOW = 0
LETTER_UP = 0
for word in str_1:
    if 'a' <= word <= 'z':
        LETTER_LOW += 1
    elif 'A' <= word <= 'Z':
        LETTER_UP += 1
print('Сумма строчных букв =', LETTER_LOW)
print('Сумма прописных букв =', LETTER_UP)
