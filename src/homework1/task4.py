"""
4. Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
Учитывать только английские буквы.
"""


string = input('Введите строку: ')
string = string.replace(' ', '')
count_high = 0
count_low = 0
index = 0

for char in string:
    if char == string[index].upper():
        count_high += 1
    elif char == string[index].lower():
        count_low += 1
    index += 1

print('Больших букв:', count_high, 'Маленьких букв:', count_low)
