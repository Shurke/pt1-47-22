'''
Во входной строке записан текст. Словом считается последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом пробелов или символами конца строки. Определите,
сколько различных слов содержится в этом тексте.
'''


import string

STR_1 = input('Введите исходную строку: ').lower()
for CHAR in string.punctuation:
    STR_1 = STR_1.replace(CHAR, ' ')
STR_1 = set(STR_1.split())
print(f'Количество уникальных слов в исходной строке: {len(STR_1)}')
