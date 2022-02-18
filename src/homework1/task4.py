"""
4. Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
Учитывать только английские буквы.
"""


import string

user_string = input('Введите строку: ')
user_string = user_string.replace(' ', '')
count_high = 0
count_low = 0

for char in user_string:
    if char in string.ascii_uppercase:
        count_high += 1
    elif char in string.ascii_lowercase:
        count_low += 1

print(f'В введенной строке больших букв: {count_high}, маленьких букв: {count_low}')
