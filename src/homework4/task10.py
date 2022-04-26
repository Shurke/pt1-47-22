"""
В данном упражнении вы должны написать программу,которая будет находить самое длинное слово в файле.
В качестве результата программа должна выводить на экран длину самого длинного слова и все слова
такой длины. Для работы используйте файл words.txt.
"""


def longest_word(file_name):
    """Find the longest words in file

    :param file_name: file from user
    :return: the length of the longest word and all words of that length
    """
    with open(file_name, 'r') as user_file:
        open_file = user_file.read().split()
    max_len_word = 0
    all_longest_word = []
    for word in open_file:
        if len(word) >= max_len_word:
            max_len_word = len(word)
            all_longest_word.append(word)
            for words in all_longest_word[:-1]:
                if len(words) < max_len_word:
                    all_longest_word.remove(words)

    return f'The length of the longest word in file is {max_len_word} and all words of that' \
           f' length are {", ".join(all_longest_word)}'


print(longest_word('words.txt'))
