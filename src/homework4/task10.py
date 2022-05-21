"""
 Самое длинное слово в файле
В данном упражнении вы должны написать программу, которая будет находить самое длинное слово
в файле. В качестве результата программа должна выводить на экран длину самого длинного слова
и все слова такой длины. Для работы используйте файл words.txt.
"""


def find_the_longest_word(string_from_file: str) -> list:
    """Находит самое длинное слово из строки

    :param string_from_file: Строка текста из прочитанного файла
    :return: Самое длинное слово из прочитанного текста
    """

    longest_word = max(string_from_file.split(), key=len)
    words_list = [str(i) for i in string_from_file.split() if len(i) == len(longest_word)]

    return words_list


def main():
    with open('words.txt', 'rt') as file:
        string_from_file = file.read()

    result = find_the_longest_word(string_from_file)
    print(f'Самые длинные слова из файла: {result}, их длинна = {len(result[0])}')


if __name__ in '__main__':
    main()
