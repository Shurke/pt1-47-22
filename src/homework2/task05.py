"""
Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""

input_data = [s for s in input('Введите данные через пробел: ').split()]
output_data = []
for elmnt in range(len(input_data)):
    for elmnt_2 in range(len(input_data)):
        if elmnt != elmnt_2 and input_data[elmnt] == input_data[elmnt_2]:
            break
    else:
        output_data.append(input_data[elmnt])

print(f"Неповторяющиеся символы: {', '.join(output_data)}")
