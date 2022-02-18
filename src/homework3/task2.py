""" 2. Города
Дан список стран и городов каждой страны.
Затем даны названия городов. Для каждого города укажите, в какой стране он находится.
Входные данные
Программа получает на вход количество стран N.
Далее идет N строк, каждая строка начинается с названия страны,
затем идут названия городов этой страны. В следующей строке записано число M,
далее идут M запросов — названия каких-то M городов, перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны, в котором находится данный город.
"""


def update_cities_dict(country_str, country_dict):
    """Генератор словаря по строке данных формата СТРАНА город1 город2 город3 ...

    :param country_str: строка данных в формате "СТРАНА город1 город2 город3"
    :param country_dict: словарь в которые необходимо добавить или обновить значения
    :returns: словарь {страна: [города..]}
    :rtype: dict
    """
    country_list = country_str.split()
    country_dict.update({country_list[0]: country_list[1:]})
    return country_dict


def get_country(city_name, country_dict):
    """Получение названия страны по введенному городу

    :param city_name: имя города для поиска
    :param country_dict: словарь содержащий соответствия {страна1: [города1], страна2: [города2]}
    :returns: страна в которой находится город или None если такого нет
    :rtype: str
    """
    for k, v in country_dict.items():
        if city_name in v:
            return k
    return None


country_cities_match_dict = {}
country_input_count = int(input("Введите количество стран: "))
for i in range(0, country_input_count):
    country_input_str = input(f"Введите данные страны #{i+1} (формат: СТРАНА город1 город2 ...): ")
    country_cities_match_dict = update_cities_dict(country_input_str, country_cities_match_dict)

result = []
citiest_input_count = int(input("Введите количество запросов городов: "))
for i in range(0, citiest_input_count):
    city_input_str = input(f"Введите город #{i}: ")
    result.append(get_country(city_input_str, country_cities_match_dict))

for r in result:
    print(r)
