#  2. Найти самое длинное слово в введенном предложении. Учтите что в предложении
#  есть знаки препинания.
#  Подсказки:
#  - my_string.split([chars]) возвращает список строк.
#  - len(list) - количество элементов в списке


text = input('Пожалуйста, введите текст: ')

newText = text.replace(',', '')
newText = newText.replace('.', '')
newText = newText.replace(':', '')
newText = newText.replace(';', '')
newText = newText.replace('!', '')
newText = newText.replace('?', '')
print(newText)

text = newText.split()
s = 0
word = ''

for i in range(len(text)):
    if len(text[i]) > len(word):
        word = text[i]
print('Самое длинное слово - ', word)
