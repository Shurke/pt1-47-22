"""Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы
 нужно выводить в том порядке, в котором они встречаются в списке.
"""

a = str(input())
b = []
for i in a:
    if a.count(i) == 1:
        b.append(i)
print(b)