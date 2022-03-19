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
Для решения задачи используйте набором данных с химическими элементами, который находится в файле
elements.txt.
"""


def word_with_elem(word, sequence):
    try_list = [False for x in range(0, len(word) + 1)]
    try_list[0] = []

    for i in range(1, len(word) + 1):

        variants = []

        for n in range(max(i - 3, 0), i):

            if try_list[n] is False:  # variability
                continue
            potential_element = word[n:i].title()  # for search in seq

            if potential_element in sequence:
                variants.append(try_list[n] + [potential_element])

        if variants:
            try_list[i] = min(variants, key=len)

    if try_list[-1] is False:
        result = ''
    else:
        result = "".join(try_list[-1])

    return result


def get_sequence():
    with open('elements.txt', 'r') as opened_file:
        elements_native = opened_file.readlines()
        elements = {}
        for string in elements_native:
            string_list = string.split(',')
            elements[string_list[1]] = string_list[2][:-1]
    return elements


while True:
    what_to_do = input('Please, type word or p_table for table validation: ')
    if what_to_do == 'p_table':
        seq = get_sequence()
        for value in seq.values():
            received_word = word_with_elem(value, seq.keys())
            if received_word != '':
                print(f'{value} can be written like {received_word}')

    else:
        print(word_with_elem(what_to_do, get_sequence().keys()))
