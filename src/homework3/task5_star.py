'''
Если помните, на старых мобильных телефонах текстовые сообщения набирались при помощи цифровых
кнопок. При этом одна кнопка была ассоциирована сразу с несколькими буквами, а выбор зависел от
количества нажатий на кнопку. Однократное нажатие приводило к появлению первой буквы в
соответствующем этой кнопке списке, последующие нажатия меняли ее на следующую. Список символов,
ассоциированных с цифровой панелью, приведен в таблице

Кнопка - Символы
1 - .,?!:
2 - A B C
3 - D E F
4 - G H I
5 - J K L
6 - M N O
7 - P Q R S
8 - T U V
9 - W X Y Z
0 - Пробел


Напишите программу, отображающую последовательность кнопок, которую необходимо нажать, чтобы на
экране телефона появился текст, введенный пользователем. Создайте словарь, сопоставляющий символы с
кнопками, которые необходимо нажать, а затем воспользуйтесь им для вывода на экран
последовательности кнопок в соответствии с введенным пользователем сообщением по запросу.
Например, на ввод строки Hello, World! ваша программа должна откликнуться следующим выводом:
4433555555666110966677755531111.
Удостоверьтесь, что ваша программа корректно обрабатывает строчные и прописные буквы. При
преобразовании букв в цифры игнорируйте символы, не входящие в указанный перечень, такие как точка с
запятой или скобки.

* обратное преобразование.
'''


SYMBOLS_ON_KEYBOARD = [' ', '.,?!:', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
SYMBOL_BOOK = {}

for ELEM in SYMBOLS_ON_KEYBOARD:
    ADDRESS = {}
    for CHAR in ELEM:
        ADDRESS[ELEM.index(CHAR) + 1] = CHAR
    SYMBOL_BOOK[SYMBOLS_ON_KEYBOARD.index(ELEM)] = ADDRESS

INPUT = input(
    'Что нажимали? Пожалуйста, для разделения '
    'идущих подряд букв на одной кнопке используйте пробел!\n').lower()
OUTPUT = ''
NORMAL_INPUT = INPUT[0]
REG_INPUT = []
INPUT_BOOK = {}

for CHAR_IND in range(1, len(INPUT)):
    if INPUT[CHAR_IND] != INPUT[CHAR_IND - 1]:
        NORMAL_INPUT += f' {INPUT[CHAR_IND]}'
    else:
        NORMAL_INPUT += INPUT[CHAR_IND]

REG_INPUT = (NORMAL_INPUT.split())

for ELEM_IND in range(len(REG_INPUT)):
    SYMBOL_DICT = {}
    SYMBOL_DICT[int(REG_INPUT[ELEM_IND][0])] = len(REG_INPUT[ELEM_IND])
    INPUT_BOOK[ELEM_IND] = SYMBOL_DICT

for TRASH, BUTTON_INFO in INPUT_BOOK.items():
    for BUTTON, NUM_OF_PRESS in BUTTON_INFO.items():
        SEARCH_DICT = SYMBOL_BOOK[BUTTON]

        OUTPUT += SEARCH_DICT[NUM_OF_PRESS]

print(f'Вероятно, вы хотели написать "{OUTPUT}"')
