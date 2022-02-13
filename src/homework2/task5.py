"""
Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке
"""

lst_ = input('Введите список значений через пробел: ')
lst_ = lst_.split()
lst_ = list(lst_)
NEW_lst = []
for i in lst_:
    if i in NEW_lst:
        NEW_lst.remove(i)
    elif i not in NEW_lst:
        NEW_lst.append(i)
print(NEW_lst)
