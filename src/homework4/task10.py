"""
В данном упражнении вы должны написать программу, которая будет находить самое длинное слово в
файле. В качестве результата программа должна выводить на экран длину самого длинного слова и все
слова такой длины. Для работы используйте файл words.txt.
"""


def print_max_word_from_file(file_name='words.txt'):
    """Find most longest words in database and print them.

    :param file_name: name of database with words, default = words.txt
    """

    words = []

    with open(f'{file_name}', 'r') as opened_file:

        while True:
            line = opened_file.readline()
            if not line:
                break
            words.append(line[:-1])

    words_len = {}

    for word in words:
        if len(word) not in words_len:
            words_len[len(word)] = {word, }
        else:
            words_len[len(word)].add(word)

    print(f'The longest words: {", ".join(words_len[max(words_len)])}')


print_max_word_from_file()
