"""
Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
Учитывать только английские буквы.
"""

str_1 = input('Please enter string text: ')
L_LOWER = 0
L_UPPER = 0
for i in str_1:
    if 'a' <= i <= 'z':
        L_LOWER += 1
    else:
        if 'A' <= i <= 'Z':
            L_UPPER += 1
print('lower =', L_LOWER)
print('upper =', L_UPPER)
