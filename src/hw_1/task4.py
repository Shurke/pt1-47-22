"""
4. Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
Учитывать только английские буквы.
"""


string = input('Введите предложение: ')
a = 0
b = 0
for i in string:
    if 'a' <= i <= 'z':
        a += 1
    else:
        if 'A' <= i <= 'Z':
            b += 1
print(a)
print(b)
# a - small letters
# b - big letters
