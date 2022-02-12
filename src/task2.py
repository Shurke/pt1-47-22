"""
2. Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
Подсказки:
- my_string.split([chars]) возвращает список строк.
- len(list) - количество элементов в списке
"""

my_str = input('Please enter text: ')
my_str = my_str.replace(",", "", 1)
my_str = my_str.replace(":", "", 1)
my_str = my_str.replace(";", "", 1)
my_str = my_str.replace("-", "", 1)
my_str = my_str.replace(".", "", 1)
words = my_str.split()
print(max(words, key=len))
