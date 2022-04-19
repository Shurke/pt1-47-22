"""Каждый химический элемент из таблицы Менделеева характеризуется
своим обозначением, состоящим из одного, двух или трех символов.
Есть такая игра – пытаться выразить то или иное слово через химические
элементы. Например, слово silicon может быть записано при помощи
следующих химических элементов: Si, Li, C, O и N. В то же время слово
hydrogen не может быть составлено из названий элементов.
Напишите рекурсивную функцию, способную определять, можно ли выразить
переданное ей слово исключительно через обозначения химических элементов.
Ваша функция должна принимать два параметра: слово, которое нужно
проверить, и список символов, которые можно при этом использовать.
Возвращать функция должна строку, состоящую из использованных символов,
если собрать искомое слово можно, и пустую строку в противном случае.
При этом регистры символов учитываться не должны.
В основной программе должна быть использована ваша функция для
проверки всех элементов таблицы Менделеева на возможность составить их
названия из обозначений химических элементов. Отобразите на экране
названия элементов вместе с обозначениями, которые были использованы для
их написания. Например, одна из строчек может выглядеть так:
Silver может быть представлен как SiLvEr
Для решения задачи используйте набором данных с химическими элементами,
который находится в файле elements.txt. """


def get_element(word, table_file, result=[]):
    """Функция производит поиск элементов таблицы Менделеева в заданном слове"""

    if word != "":
        if len(word) >= 3 and word[:3] in table_file:
            elem_word = word[:3]
            word = word[3:]
            result.append(elem_word)
            return get_element(word, table_file)
        elif len(word) >= 2 and word[:2] in table_file:
            elem_word = word[:2]
            word = word[2:]
            result.append(elem_word)
            return get_element(word, table_file)
        elif len(word) >= 1 and word[0] in table_file:
            elem_word = word[:2]
            word = word[1:]
            result.append(elem_word)
            return get_element(word, table_file)
        else:
            return "Данное слово нельзя записать таблицей Менделеева"
    else:
        return f"Ваше слово можно записать следующими элементами " \
               f"таблицы Менделеева \n{result}"


def table_mendeleev():

    """Функция обрабатывает текстовый файл с таблицей Менделеева. Создает список элементов"""

    table_list = []
    try:
        file = open("elements.txt")
    except FileNotFoundError:
        print("Фаил не найден")
    else:
        for lines in file:
            table_elem = lines.split(',')
            table_list.append(table_elem[1].upper())
        file.close()
    return table_list


my_word = input("Введите слово которое хотите проверить\n").upper()
print(get_element(my_word, table_mendeleev()))
