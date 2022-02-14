"""
Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания.
"""


import string

str_in = input('Введите предложение со всеми знаками препинания: ').split()
s_clear = [s.strip(string.punctuation) for s in str_in]
l_max = max([len(s) for s in s_clear])
print(f'Самое длинное слово (слова) в предложении это:\n {[i for i in s_clear if len(i) == l_max]}'
      f'\n  состоит (-ят) из {l_max} символов!')
