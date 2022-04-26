"""
Каждый химический элемент из таблицы Менделеева характеризуется своим обозначением, состоящим из
одного, двух или трех символов. Есть такая игра – пытаться выразить то или иное слово через
химические элементы. Например, слово silicon может быть записано при помощи следующих химических
элементов: Si, Li, C, O и N. В то же время слово hydrogen не может быть составлено из названий
элементов.
Напишите рекурсивную функцию, способную определять, можно ли выразить переданное ей слово
исключительно через обозначения химических элементов. Ваша функция должна принимать два параметра:
слово, которое нужно проверить, и список символов, которые можно при этом использовать. Возвращать
функция должна строку, состоящую из использованных символов, если собрать искомое слово можно, и
пустую строку в противном случае. При этом регистры символов учитываться не должны.
В основной программе должна быть использована ваша функция для проверки всех элементов таблицы
Менделеева на возможность составить их названия из обозначений химических элементов. Отобразите на
экране названия элементов вместе с обозначениями, которые были использованы для их написания.
Например, одна из строчек может выглядеть так:
Silver может быть представлен как SiLvEr
Для решения задачи используйте набором данных с химическими элементами, который находится
в файле elements.txt.
"""


def chemistry_output(word_from_user, func_from_chem):
    """Output message about the possibility or impossibility to
    change the word with the chemical elements

    :param word_from_user: word from user
    :param func_from_chem: result of function chemistry_word
    :return: possibility or impossibility to change the word
    """
    result = func_from_chem
    if result is None:
        return f'The word {word_from_user} cannot be converted with chemical elements'
    else:
        return f'The word {word_from_user} can be represented with chemical elements as {result}'


def chemistry_word(word, chem_list):
    """determines if words can be expressed with the use of chemical elements

    :param word: word to check
    :param chem_list: list of symbols that can be used in this case
    :return: string of used characters
    """

    for item in range(3, 0, -1):
        start_word = word[:item]
        if start_word not in chem_list:
            continue
        if len(word) == item:
            return start_word
        end_word = chemistry_word(word[item:], chem_list)
        if end_word:
            return start_word + end_word


def mendeleev_list():
    """file processing with chemical elements

    :return: list with elements
    """
    mendeleev_elements = []
    with open('elements.txt', 'r') as elements:
        for elem in elements.read().split():
            mendeleev_elements.append(elem.lower().split(',')[1])
    return mendeleev_elements


user_word = input('Enter the word which you would like to convert: ').lower()
convert_for_chemistry = chemistry_word(user_word, mendeleev_list())
print(chemistry_output(user_word, convert_for_chemistry))
