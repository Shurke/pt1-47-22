"""
В данном упражнении вы должны написать программу, которая будет находить самое
длинное слово в файле. В качестве результата программа должна выводить на экран
длину самого длинного слова и все слова такой длины. Для работы используйте файл
words.txt.
"""


def get_long_word(file):
    """Находит самое длинное слово в файле

    :param file: Имя файла
    :return: Длина самого длинного слова и все слова такой длины

    """
    try:
        with open(file) as f:
            str_input = f.read().split()
    except FileNotFoundError:
        return "Файл не найден"
    dict_word_len = {str_input[i]: len(str_input[i]) for i in range(len(str_input))}
    max_len = max(dict_word_len, key=lambda x: dict_word_len[x])
    list_output = [x for x in dict_word_len if len(x) == dict_word_len[max_len]]
    return f"Это следующие слова: {''.join(list_output)}"


if __name__ == "__main__":
    print(get_long_word('words.txt'))
