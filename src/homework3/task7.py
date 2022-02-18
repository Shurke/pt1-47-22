'''
Анаграммами называются слова, образованные путем взаимной перестановки букв. В английском языке,
например, анаграммами являются слова «live» и «evil», а в русском – «выбор» и «обрыв». Напишите
программу, которая будет запрашивать у пользователя два слова, определять, являются ли они
анаграммами, и выводить на экран ответ.
'''

WORD_1 = input('Введите первое слово: ').lower()
WORD_2 = input('Введите второе слово: ').lower()
DICT_WORD_1 = {}
DICT_WORD_2 = {}

for CHAR in WORD_1:
    DICT_WORD_1[CHAR] = WORD_1.count(CHAR)
for CHAR in WORD_2:
    DICT_WORD_2[CHAR] = WORD_2.count(CHAR)

TRUE = 0
FALSE = 0

for CHAR_1, COUNT_1 in DICT_WORD_1.items():
    for CHAR_2, COUNT_2 in DICT_WORD_2.items():
        if CHAR_1 == CHAR_2 and COUNT_1 == COUNT_2:
            TRUE += 1
        else:
            FALSE += 1

if TRUE == len(WORD_1) and TRUE == len(WORD_2):
    print('Слова являются анаграммами!')
else:
    print('Слова не являются анаграммами!')
