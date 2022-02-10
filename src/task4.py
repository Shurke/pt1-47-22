"""
Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
Учитывать только английские буквы
"""

str_1 = input('Введите строку:')
letter_low = 0
letter_up = 0
for word in str_1:
    if 'a' <= word <= 'z':
        letter_low = letter_low + 1
    elif 'A' <= word <= 'Z':
        letter_up = letter_up + 1
print('Сумма строчных букв =', letter_low)
print('Сумма прописных букв =', letter_up)
