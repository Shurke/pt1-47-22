# 1. Используйте генератор списков чтобы получить следующий: [ab;ac;
# ad;bb;bc;bd;].
# 2. Используйте на предыдущий список slice чтобы получить следующий:
# [ab;ad;bc;].
# 3. Используйте генератор списков чтобы получить следующий [1a;2a;
# 3a;4a;].
# 4. Одной строкой удалите элемент 2a; из прошлого списка и
# напечатайте его.
# 5. Скопируйте список и добавьте в него элемент 2a; так чтобы в
# исходном списке этого элемента не было.

list_of_items = [a + b for a in "ab" for b in "bcd"]
print(list_of_items)
list_of_items = list_of_items[1::2]
print(list_of_items)
list_of_items2 = [a + b for a in "1234" for b in "a"]
print(list_of_items2)
print(list_of_items2.pop(1))
print(list_of_items2)
list_of_items3 = list_of_items2.copy()
list_of_items3.insert(1, "2a")
print(list_of_items3)
