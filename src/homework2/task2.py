"""List practice
Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
Скопируйте список и добавьте в него элемент '2a' так
чтобы в исходном списке этого элемента не было.

"""
import copy

GENERATED_LIST = [x + y for x in 'ab' for y in 'bcd']
print('Сгенерированный список: ', GENERATED_LIST)
print('Новый список с применение slice: ', GENERATED_LIST[::2])
GENERATED_LIST_2 = [z + 'a' for z in '1234']
print('Сгенерированный список: ', GENERATED_LIST_2)
print('Одной строкой удаляем элемент "2a" и печатаем его: ', GENERATED_LIST_2.pop(1))

COPIED_LIST = copy.copy(GENERATED_LIST_2)
print('Скопированный исходный список: ', COPIED_LIST)
UPDATED_LIST = COPIED_LIST.append('2a')
print('Скопированный обновленный список: ', COPIED_LIST)
