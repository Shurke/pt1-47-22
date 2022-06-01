"""Самое длинное слово в файле
В данном упражнении вы должны написать программу, которая будет находить
самое длинное слово в файле. В качестве результата программа должна выводить
на экран длину самого длинного слова и все слова такой длины. Для работы используйте
файл words.txt.
"""


def longest_words(input_data):
    with open(input_data) as file:
        list_of_words = file.read().split()

    max_len = len(max(list_of_words, key=len))
    output_list = [word for word in list_of_words if len(word) == max_len]
    return f'Длина самого длинного слова {max_len} символов.' \
           f' Слова такой длины: {", ".join(output_list)}'


print(longest_words('words.txt'))
