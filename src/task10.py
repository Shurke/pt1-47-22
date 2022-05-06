"""Самое длинное слово в файле
В данном упражнении вы должны написать программу, которая будет находить самое длинное слово в
файле. В качестве результата программа должна выводить на экран длину самого длинного слова и все
слова такой длины. Для работы используйте файл words.txt.
"""


def long_word():
    """Функция создает список из самых длинных слов в фаиле"""
    with open('words.txt', 'r') as file:
        list_word = file.read().split('\n')
    len_word = 0
    for i in list_word:
        if len(i) >= len_word:
            len_word = len(i)

    list_long_words = [i for i in list_word if len(i) == len_word]

    print(f'Самое длинное слово состоит из {len_word} букв.'
          f' Самые длинные слова в фаиле: {", ".join(list_long_words)}')


if __name__ == '__main__':
    long_word()
