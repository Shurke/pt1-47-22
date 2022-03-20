"""
В данном упражнении вы должны написать программу, которая будет находить самое длинное слово в
файле. В качестве результата программа должна выводить на экран длину самого длинного слова и все
слова такой длины. Для работы используйте файл words.txt.
"""


def get_max_word(file_name='words.txt'):
    """Find most longest words in database and print them.
    Pass into filename (default = words.txt)"""

    with open(f'{file_name}', 'r') as opened_file:
        string = opened_file.readline()
        words = []
        while string:
            words.append(string[:-1])
            string = opened_file.readline()

    words_len = {}

    for word in words:
        if len(word) not in words_len:
            words_len[len(word)] = {word, }
        else:
            words_len[len(word)].update({word, })

    print(f'The longest words: {", ".join(words_len[max(words_len)])}')


get_max_word()
