"""
Набор данных, содержащий детские имена, состоит более чем из 200 файлов, в
каждом из которых, помимо сотни имен, указано количество названных тем или иным
именем детей. При этом файлы отсортированы по убыванию популярности имен. Для
каждого года присутствует по два файла: в одном перечислены мужские имена, в
другом – женские. Совокупный набор данных содержит информацию для всех лет,
начиная с 1900-го и заканчивая 2012-м.
Напишите программу, которая будет считывать данные (baby_names.zip) и
предоставлять следующие результаты:
имена, которые были лидерами (топ-10) по частоте использования как минимум в
одном году. На выходе должно получиться два списка: в одном из них будут
присутствовать наиболее популярные имена для мальчиков, во втором – для девочек.
При этом списки не должны содержать повторяющиеся имена.
имена, использованные для мальчиков и девочек (универсальные имена). Если в этом
году универсальных имен не было, нужно известить об этом пользователя. Кроме
того, если за указанный пользователем год не было данных по именам, выведите
соответствующее сообщение об ошибке.
Предусмотреть возможность работать с каким-то ограниченным периодом времени или
с конкретным годом. Например, ваша программа должна корректно вывести данные,
если пользователь ввел “1990-1995” или просто “1996”. Если пользователем на вход
программы не передал никаких данных, то необходимо вывести все данные за все
время.
"""
import zipfile
import shutil


def open_file(year, name):
    """Открывает файл, читает строки, преобразовывает в список"""

    try:
        with open(f'BabyNames/{year}_{name}Names.txt') as t:
            list_res = []
            for i in t.readlines():
                list_res.append(i.rstrip().split())
    except FileNotFoundError:
        raise "Файл не найден"
    return list_res


def get_dict_top(year, name):
    """Преобразовывает слисок в словарь, состоящий из 10 элементов, где ключ -

    имя, a значение - количество названных детей этим именем

    """
    list_open = open_file(year, name)
    dict_top = {x[0]: x[1] for x in list_open[:10]}
    return dict_top


def get_general(year):
    """Формирует список универсальных имён"""

    list_boy = open_file(year, "Boys")
    dict_boy = {x[0]: x[1] for x in list_boy}
    set_boy = set(dict_boy)
    list_girl = open_file(year, "Girls")
    dict_girl = {x[0]: x[1] for x in list_girl}
    set_girl = set(dict_girl)
    list_generic = list(set_boy & set_girl)
    return list_generic


def get_list_top(year, name):
    """Формирует список из топ-10 имён за все года"""

    if len(year) == 4:
        dict_top = get_dict_top(year, name)
        result_top = [x for x in dict_top]
        return result_top
    else:
        res_dict = {}
        for item in range(int(year.split("-")[0]), int(year.split("-")[1]) + 1):
            res_new = get_dict_top(item, name)
            for i in res_new:
                if i not in res_dict or i in res_dict and res_dict[i] < res_new[i]:
                    res_dict[i] = res_new[i]
                else:
                    continue
        sorted_tuple = sorted(res_dict.items(), key=lambda x: x[1],
                              reverse=True)
        dict_top = {x[0]: x[1] for x in sorted_tuple[:10]}
        result_top = [x for x in dict_top]
        return result_top


def get_list_top_without_general(year):
    """Удаляет универсальные имена в списках топ-10 для мальчиков и девочек"""

    result_boy_top = get_list_top(year, "Boys")
    result_girl_top = get_list_top(year, "Girls")
    if len(year) == 4:
        res_general_list = get_general(year)
    else:
        res_general = []
        for item in range(int(year.split("-")[0]), int(year.split("-")[1]) + 1):
            res_general.append(get_general(item))
        res_general_list = list(set(sum(res_general, list())))
    boy_top_without_general = list(set(result_boy_top) - set(result_girl_top))
    girl_top_without_general = list(set(result_girl_top) - set(result_boy_top))
    return get_output(year, boy_top_without_general,
                      girl_top_without_general,
                      res_general_list)


def get_output(year, boy, girl, general):
    """Выполняет вывод, удаляет разархивированный файл"""

    shutil.rmtree('BabyNames')
    print(f"Топ-10 имён для мальчиков в {year}: {boy}")
    print(f"Топ-10 имён для девочек в {year}: {girl}")
    if general:
        return f"Универсальные имена в {year}: {general}"
    else:
        return f"Универсальных имён в {year} нет"


def get_name_top_10(year):
    """Осуществляет поиск наиболее популярных имен для мальчиков и девочек"""

    with zipfile.ZipFile('baby_names.zip', 'r') as file:
        file.extractall()

    if year == "":
        return get_list_top_without_general("1900-2012")
    return get_list_top_without_general(year)


def main():
    """Проверяет, удовлетворяет ли введённый год условиям"""

    year_input = input(
        "Введите год в диапазоне [1900-2012], например, 1996 или 1900-1995: ")
    start_date = 0
    end_date = 0
    year_one = 0
    if len(year_input) == 4:
        year_one = int(year_input) in range(1900, 2013)
    elif len(year_input) == 9:
        start_date, end_date = year_input.split("-")
    elif year_input == "":
        start_date, end_date = 1900, 2012
    else:
        return print("Введены неверные года")
    is_valid_start_date = int(start_date) in range(1900, 2013)
    is_valid_end_date = int(end_date) in range(1900, 2013)
    if is_valid_start_date and is_valid_end_date or year_one:
        return print(get_name_top_10(year_input))
    else:
        return print("По данным годам нет информации")


if __name__ == "__main__":
    main()
