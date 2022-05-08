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
    with open(file_name, 'r') as open_file:
        reading_file = open_file.read().split()
    words_dict = {reading_file[i]: len(reading_file[i]) for i in range(len(reading_file))}
    max_len_word = max(words_dict.values())
    longest_words = {word: word_len for word, word_len in words_dict.items()
                     if word_len == max_len_word}

    return f'The length of the longest word in file is {max_len_word} and all words of that' \
           f' length are {", ".join(longest_words)}'


if __name__ == '__main__':
    print(longest_word('words.txt'))
