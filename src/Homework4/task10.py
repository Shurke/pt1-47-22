"""В данном упражнении вы должны написать программу,
которая будет находить самое длинное слово в файле.
В качестве результата программа должна выводить на экран
длину самого длинного слова и все слова такой длины.
Для работы используйте файл words.txt."""


def long_word():
    """Данная функция находит самое длинное слово в файле
    words.txt, файл должен находиться в одной директории
    с файлом программы."""

    longest_word = []
    len_word = ""
    try:
        file = open("words.txt")
    except FileNotFoundError:
        print("Фаил не найден")
    else:
        inter_list = file.readlines()
        file.close()
        inter_list = [line.rstrip() for line in inter_list]
        for word in inter_list:
            if len(len_word) < len(word):
                len_word = word
        for word in inter_list:
            if len(len_word) == len(word):
                longest_word.append(word)
        return print(f"Длинна самого длинного слова {len(len_word)} "
                     f"букв, вот слова такой длинны {longest_word}")


long_word()
