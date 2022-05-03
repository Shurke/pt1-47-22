"""
 Самое длинное слово в файле
В данном упражнении вы должны написать программу, которая будет находить самое длинное слово
в файле. В качестве результата программа должна выводить на экран длину самого длинного слова
и все слова такой длины. Для работы используйте файл words.txt.
"""


import os


def find_the_longest_word(string_from_file: str) -> list:
    """Находит самое длинное слово из строки

    :param string_from_file: Строка текста из прочитанного файла
    :return: Самое длинное слово из прочитанного текста
    """

    longest_word = max(string_from_file.split(), key=len)
    words_list = [str(i) for i in string_from_file.split() if len(i) == len(longest_word)]

    return words_list


def main():
    if not os.path.exists('words.txt'):
        with open('words.txt', 'w'):
            pass

    switch = input('Выберите одно из действий (1 или 2):\n'
                   '1 - Сделать дозапись нового слова в файл words.txt\n'
                   '2 - Найти самое длинное слово из файла words.txt\n'
                   'Решение: ')

    if switch == '1':
        user_string = input('Введите любое слово: ')
        with open('words.txt', 'at') as file:
            file.write(user_string + ' \n')
    elif switch == '2':
        with open('words.txt', 'rt') as file:
            string_from_file = file.read()

        result = find_the_longest_word(string_from_file)
        print(f'Самые длинные слова из файла: {result}, их длинна = {len(result[0])}')


if __name__ in '__main__':
    main()
