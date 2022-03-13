"""
Города
"""
list_1 = ("Moscow", "Petersburg", "Novgorod", "Kaluga")
list_2 = ("Kiev", "Donetsk", "Odessa")

while True:
    x = (input("Input names of cities for get name of country"))
    if x in list_2:
        print("Ukraine")
    elif x in list_1:
        print("Russia")
    else:
        print("not Ukraine and not Russia, or incorrect name")
