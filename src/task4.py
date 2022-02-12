"""
Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
Учитывать только английские буквы.
"""

str_1 = input('Please enter string text: ')
let_lower = 0
let_upper = 0
for i in str_1:
    if 'a' <= i <= 'z':
        let_lower += 1
    else:
        if 'A' <= i <= 'Z':
            let_upper += 1
print('lower =', let_lower)
print('upper =', let_upper)
