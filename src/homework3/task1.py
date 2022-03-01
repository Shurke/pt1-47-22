"""
Создайте словарь с помощью генератора словарей, так чтобы его ключами были числа от 1 до 20, а
значениями кубы этих чисел
"""

create_dict = {element: element ** 3 for element in range(1, 21)}
print(f'Result of created dict comprehensions: {create_dict}')
