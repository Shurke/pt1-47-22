"""Текстовые сообщения"""
dictionary = {".": 1, ",": 11, "?": 111, "!": 1111, ":": 11111,
              "A": 2, "B": 22, "C": 222, "D": 3, "E": 33, "F": 333,
              "G": 4, "H": 44, "I": 444, "J": 5, "K": 55, "L": 555,
              "M": 6, "N": 66, "O": 666, "P": 7, "Q": 77, "R": 777,
              "S": 7777, "T": 8, "U": 88, "V": 888, "W": 9,
              "X": 99, "Y": 999, "Z": 9999, " ": 0
              }
string = input("Введите слово: ").upper()
list1 = list()
for char in string:
    demi_result = dictionary.get(char)
    list1.append(demi_result)
print("".join(map(str, list1)))


