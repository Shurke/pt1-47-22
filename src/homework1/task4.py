"""
Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
Учитывать только английские буквы.
"""
import string

strng = input('Введите строку: ')
print(string.ascii_lowercase)
lwr = 0
upr = 0
for x in strng:
    if x in string.ascii_lowercase:                             # Counting char in lower case
        lwr += 1
    elif x in string.ascii_uppercase:                           # Counting char in upper case
        upr += 1
    else:                                                       # To display a message about
        print(f'{x} - не является английским символом')         # an unsuitable char as a result

print(f'Символов в нижнем регистре: {lwr}')
print(f'Символов в верхнем регистре: {upr}')
