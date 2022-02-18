""" 5. Текстовые сообщения
Кодирование/декодирование сообщения в/из последовательность цифр для мобильных телефонов
"""


KEY_CHARS = {
    1: ".,?!:",
    2: "ABC",
    3: "DEF",
    4: "GHI",
    5: "JKL",
    6: "MNO",
    7: "PQRS",
    8: "TUV",
    9: "WXYZ",
    0: " ",
}


def encode_mobile_sequence(message):
    """Кодирует сообщение в последовательность кнопок согласно словарю KEY_CHARS

    :param message: сообщение которое необходимо перевести в последовательность цифр
    :returns: строку последовательности цифр
    :rtype: str
    """
    result = []
    for char in message.upper():
        for k, v in KEY_CHARS.items():
            if char in v:
                result.append(str(k) * (v.index(char) + 1))
    return " ".join(result)


def decode_mobile_sequence(sequence):
    """Декодирует последовательность кнопок в текст согласно словарю KEY_CHARS

    :param sequence: последовательность кнопок
    :returns: декодированное сообщение
    :rtype: str
    """
    result = []
    for s in sequence.split():
        key = int(s[0])
        pos = len(s) - 1
        result.append(KEY_CHARS[key][pos])
    return "".join(result)


input_str = input("Введите сообщение или последовательность цифр: ")
is_num_sequnce = "".join(input_str.split()).isdigit()
if is_num_sequnce:
    print(f"сообщение: {decode_mobile_sequence(input_str)}")
else:
    print(f"последовательность кнопок: {encode_mobile_sequence(input_str)}")
