"""
4. Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке. Учитывать только английские
буквы.
"""


str_1 = input('Исходная строка: ')
big_count = 0
small_count = 0

for char in str_1:
    if char.isupper():
        big_count += 1
    elif char.islower():
        small_count += 1

print(f'Заглавных букв {big_count}, а строчных - {small_count}!')
