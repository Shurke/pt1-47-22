""" 7. Анаграммы
Анаграммами называются слова, образованные путем взаимной перестановки букв.
В английском языке, например, анаграммами являются слова «live» и «evil»,
а в русском – «выбор» и «обрыв».
Напишите программу, которая будет запрашивать у пользователя два слова,
определять, являются ли они анаграммами, и выводить на экран ответ.
"""


input_lst = [w for w in input("Введите слова через пробел: ").lower().split()]
is_anagramm = sorted(input_lst[0]) == sorted(input_lst[1])
result_msg = f"'{input_lst[0]}' и '{input_lst[1]}' {'НЕ' if not is_anagramm else ''}анаграммы"
print(result_msg)
