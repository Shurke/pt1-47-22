"""
Анаграммами называются слова, образованные путем взаимной перестановки букв.
В английском языке, например, анаграммами являются слова «live» и «evil», а в русском – «выбор» и
«обрыв». Напишите программу, которая будет запрашивать у пользователя два слова, определять,
являются ли они анаграммами, и выводить на экран ответ.
"""

# 1-ый вариант решения задачи

FIRST_WORD = sorted(input('Введите первое слово: ').lower())
SECOND_WORD = sorted(input('Введите второе слово: ').lower())

if FIRST_WORD == SECOND_WORD and len(FIRST_WORD) == len(SECOND_WORD):
    print('Слова анаграммы')
else:
    print('Слова не анаграммы')

# 2-ой вариант решения задачи
# import collections
# FIRST_WORD = input('Введите первое слово: ').lower()
# SECOND_WORD = input('Введите второе слово: ').lower()
# if collections.Counter(FIRST_WORD) == collections.Counter(SECOND_WORD):
#     print(f'Слова {FIRST_WORD} и {SECOND_WORD} анаграммы.')
# else:
#     print(f'Слова {FIRST_WORD} и {SECOND_WORD} не анаграммы.')
