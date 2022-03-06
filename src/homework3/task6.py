"""
Во входной строке записан текст. Словом считается последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом пробелов или символами конца строки.
Определите, сколько различных слов содержится в этом тексте.
"""

import string

INPUT_STR = input('Введите входную строку: ')
for element in string.punctuation:
    INPUT_STR = INPUT_STR.replace(element, '')

OUTPUT_STR = []
for word in INPUT_STR.split():
    if word not in OUTPUT_STR:
        OUTPUT_STR.append(word)
    else:
        OUTPUT_STR.remove(word)

print(f'Количество уникальных слов во входной строке: {len(OUTPUT_STR)}')
