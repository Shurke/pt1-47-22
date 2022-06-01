"""Каждый химический элемент из таблицы Менделеева характеризуется своим обозначением,
состоящим из одного, двух или трех символов. Есть такая игра – пытаться выразить то
или иное слово через химические элементы. Например, слово silicon может быть записано
при помощи следующих химических элементов: Si, Li, C, O и N. В то же время слово hydrogen
не может быть составлено из названий элементов.
Напишите рекурсивную функцию, способную определять, можно ли выразить переданное ей слово
исключительно через обозначения химических элементов. Ваша функция должна принимать два
параметра: слово которое нужно проверить и список символов которые можно при этом использовать.
Возвращать функция должна строку, состоящую из использованных символов, если собрать искомое
слово можно, и пустую строку в противном случае. При этом регистры символов учитываться не должны.
В основной программе должна быть использована ваша функция для проверки всех элементов таблицы
Менделеева на возможность составить их названия из обозначений химических элементов.
Отобразите на экране названия элементов вместе с обозначениями, которые были использованы
для их написания. Например, одна из строчек может выглядеть так:
Silver может быть представлен как SiLvEr
Для решения задачи используйте набором данных с химическими элементами,
который находится в файле elements.txt."""


def matching_with_elements(word, elem_list, result=[]):
    """Checks the possibility of writing the entered word using elements from the list"""

    if word != "":
        for i in range(3, 0, -1):
            if len(word) >= i and word[:i].capitalize() in elem_list:
                elem_word = word[:i].capitalize()
                word = word[i:]
                result.append(elem_word)
                return matching_with_elements(word, elem_list)
        else:
            return
    else:
        return ''.join(result)


def input_open_output():
    """Accepts user input, generates a list from a file, generates a response"""

    input_word = input("Введите слово которое хотите проверить: ")

    with open('elements.txt') as file:
        elements = file.read().split(",")
    elements_list = elements[1::2]
    output_word = matching_with_elements(input_word, elements_list)

    if output_word:
        print(f'"{input_word}" может быть представлен как {output_word}.')
    else:
        print(f'"{input_word}" невозможно представить в виде элементов таблицы Менделеева')


if __name__ in '__main__':
    input_open_output()
