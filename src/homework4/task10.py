"""
В данном упражнении вы должны написать программу, которая будет находить самое длинное слово в
файле. В качестве результата программа должна выводить на экран длину самого длинного слова и все
слова такой длины. Для работы используйте файл words.txt.
"""


def max_word(file_name='words.txt'):
    with open(f'{file_name}', 'r') as opened_file:
        words_native = opened_file.readlines()
        words = []
        for elem in words_native:
            words.append(elem[:-1])
        max_len = len((max(words, key=len)))
        for word in words:
            if len(word) == max_len:
                print(word)


max_word()
