"""
Уникальные элементы в списке
Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""


input_list = [n for n in input('Введите список элементов: ').split()]
final_list = []
for item in input_list:
    if item not in final_list:
        print(item)
        final_list.append(item)
