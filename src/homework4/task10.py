"""
В данном упражнении вы должны написать программу, которая будет находить самое
длинное слово в файле. В качестве результата программа должна выводить на экран
длину самого длинного слова и все слова такой длины. Для работы используйте файл
words.txt.
"""


def get_long_word(file):
    """Находит самое длинное слово в файле

    :param file: Имя файла
    :return: Длина самого длинного слова и все слова такой длины ввиде списка

    """
    try:
        with open(file) as f:
            str_input = f.read().split()

        dict_1 = {str_input[i]: len(str_input[i]) for i in
                  range(len(str_input))}
        result = max(dict_1, key=lambda x: dict_1[x])
        list_output = [x for x in dict_1 if len(x) == dict_1[result]]
        return f"Самое длинное слово состоит из {dict_1[result]} букв." \
               f"Это следующие слова: {list_output}"
    except FileNotFoundError:
        return "Ошибка при работе с файлом"


print(get_long_word('words.txt'))
