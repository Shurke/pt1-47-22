"""
Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""


input_data = [s for s in input('Введите данные через пробел: ').split()]
output_data = []
for elmnt in input_data:
    if input_data.count(elmnt) == 1:
        output_data.append(elmnt)

print(f"Неповторяющиеся символы: {', '.join(output_data)}")
