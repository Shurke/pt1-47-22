'''
Во входной строке записан текст. Словом считается последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом пробелов или символами конца строки. Определите,
сколько различных слов содержится в этом тексте.
'''


import string
input_text = input('Введите текст: ')
new_list = input_text.lower().split()
unique_words = set()
for word in new_list:
    if word[-1] in string.punctuation:
        unique_words.add(word[:-1])
    else:
        unique_words.add(word)
print(f'Количество уникальных слов в тексте равно {len(unique_words)}')
