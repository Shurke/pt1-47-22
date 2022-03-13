"""
Найти самое длинное слово в введенном предложении.Учтите что в предложении есть знаки препинания.
Подсказки:
- my_string.split([chars]) возвращает список строк.
- len(list) - количество элементов в списке
"""
import string

str_1 = input("Введите предложение")
for p in string.punctuation:
    if p in str_1:
        str_1 = str_1.replace(p, "")
max_slovo = max(str_1.split(), key=len,)
print(f"Самое длинное слово в предложении: {max_slovo}.")
