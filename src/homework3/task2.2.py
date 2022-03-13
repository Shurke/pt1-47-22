"""
Города_2
"""
list_1 = ("Moscow", "Petersburg", "Novgorod", "Kaluga")
list_2 = ("Kiev", "Donetsk", "Odessa")
cities_input = input("Введите название городов через пробел на английском").split()
count_name = []
name_1 = "Russia"
name_2 = "Ukraine"
name_3 = "Other"
for i in cities_input:
    if i not in list_1:
        count_name.append(name_2)
    elif i not in list_2:
        count_name.append(name_1)
    else:
        count_name.append(name_3)
print("Последовательность стран, введеных вами:", count_name)
