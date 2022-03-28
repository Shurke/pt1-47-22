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


def open_file(year, name):
    with open(f'BabyNames/{year}_{name}Names.txt') as t:
        list_input = t.readlines()
    list_input = [line.rstrip() for line in list_input]
    list_res = [x.split(" ") for x in list_input]
    return list_res


def get_one_year(year, name):
    list_open = open_file(year, name)
    dict_top = {x[0]: x[1] for x in list_open[:10]}
    list_top = [x for x in dict_top]
    return list_top


def get_dict_top(year, name):
    list_open = open_file(year, name)
    dict_top = {x[0]: x[1] for x in list_open[:10]}
    return dict_top


def get_general(year):
    list_boy = open_file(year, "Boys")
    dict_boy = {x[0]: x[1] for x in list_boy}
    set_boy = set(dict_boy)
    list_girl = open_file(year, "Girls")
    dict_girl = {x[0]: x[1] for x in list_girl}
    set_girl = set(dict_girl)
    list_generic = list(set_boy & set_girl)
    return list_generic


def get_list_top(year, name):
    res_dict = {}
    for item in range(int(year.split("-")[0]), int(year.split("-")[1]) + 1):
        res_new = get_dict_top(item, name)
        for i in res_new:
            if i not in res_dict or i in res_dict and res_dict[i] < res_new[i]:
                res_dict[i] = res_new[i]
            else:
                continue
    sorted_tuple = sorted(res_dict.items(), key=lambda x: x[1], reverse=True)
    dict_top = {x[0]: x[1] for x in sorted_tuple[:10]}
    result_top = [x for x in dict_top]
    return result_top


def get_some_year_top(year):
    result_boy_top = get_list_top(year, "Boys")
    result_girl_top = get_list_top(year, "Girls")
    res_general = []
    for item in range(int(year.split("-")[0]), int(year.split("-")[1]) + 1):
        res_general.append(get_general(item))

    boy_top_without_general = list(set(result_boy_top) - set(result_girl_top))
    girl_top_without_general = list(set(result_girl_top) - set(result_boy_top))
    res_general_list = list(set(sum(res_general, list())))
    return get_output(year, boy_top_without_general,
                      girl_top_without_general,
                      res_general_list)


def get_output(year, boy, girl, general):
    return (f"Топ-10 имён для мальчиков в {year}: {boy}\n"
            f"Топ-10 имён для девочек в {year}: {girl}\n"
            f"Универсальные имена в {year}: {general}")


def get_name_top_10(year):
    with zipfile.ZipFile('baby_names.zip', 'r') as file:
        file.extractall()

    if len(year) == 4:
        if int(year) in range(1900, 2013):
            return get_output(year, get_one_year(year, "Boys"),
                              get_one_year(year, "Girls"), get_general(year))
        else:
            return "Нет данных по этому году"
    elif len(year) == 9:
        if int(year.split("-")[0]) and int(
                year.split("-")[1]) in range(1900, 2013):
            return get_some_year_top(year)
        else:
            return "Нет данных по этим годам"
    elif year == "":
        return get_some_year_top("1900-2012")
    else:
        return "Введены неверные года"


year_input = input(
    "Введите год в диапазоне [1900-2012], например, 1996 или 1900-1995: ")
print(get_name_top_10(year_input))
