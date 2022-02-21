import re
'''Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
Подсказки:
- my_string.split([chars]) возвращает список строк.
- len(list) - количество элементов в списке'''

sentence = input("Введите предложение:")
my_list = re.sub(r'[^\w\s]', '', sentence)
max_string = max(my_list, key=len)
print("Самое длинное слово в списке: " + max_string)
