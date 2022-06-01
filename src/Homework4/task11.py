"""
Набор данных, содержащий детские имена, состоит более чем из 200 файлов, в каждом из которых,
помимо сотни имен, указано количество названых тем или иным именем детей. При этом файлы
отсортированы по убыванию популярности имен. Для каждого года присутствует по два файла:
в одном перечислены мужские имена, в другом – женские. Совокупный набор данных содержит
информацию для всех лет, начиная с 1900-го и заканчивая 2012-м.
Напишите программу, которая будет считывать данные (baby_names.zip) и предоставлять
следующие результаты:

Имена, которые были лидерами (топ-10) по частоте использования как минимум в одном году.
На выходе должно получиться два списка: в одном из них будут присутствовать наиболее популярные
имена для мальчиков, во втором – для девочек. При этом списки не должны содержать
повторяющиеся имена.

Имена, использованные для мальчиков и девочек (универсальные имена). Если в этом году
универсальных имен не было, нужно известить об этом пользователя. Кроме того, если за
указанный пользователем год не было данных по именам, выведите соответствующее сообщение об ошибке.

Предусмотреть возможность работать с каким-то ограниченным периодом времени или с конкретным годом.
Например, ваша программа должна корректно вывести данные, если пользователь ввел “1990-1995”
или просто “1996”. Если пользователем на вход программы не передал никаких данных, то необходимо
вывести все данные за все время.
"""
import shutil
import zipfile


def get_final_top10(result_list):
    """Generates a final list of 10 names"""

    dict_top = {x[0]: x[1] for x in result_list[:10]}
    result_top = [x for x in dict_top]
    return result_top


def period_of_year(full_list):
    """Performs sorting by popularity of names in the general list for a given period"""

    result_list = []
    temp_result = {}
    for item in full_list:
        name, count = item
        for itm in full_list:
            if name == itm[0]:
                if itm[1] > count:
                    count = itm[1]
                    temp_result.update({name: count})
    sorted_dict = {}
    sorted_keys = sorted(temp_result, key=temp_result.get, reverse=True)
    for w in sorted_keys:
        sorted_dict[w] = temp_result[w]
    for name, count in sorted_dict.items():
        result_list.append([name, count])
    return get_final_top10(result_list)


def get_full_list(start_year, finish_year, gender):
    """Forming of a list of names from a file for a given period of years"""

    with zipfile.ZipFile('baby_names.zip', 'r') as baby_names:
        baby_names.extractall()
    full_list = []
    for year in range(start_year, finish_year + 1):
        with open(f'BabyNames/{year}_{gender}Names.txt', 'r') as file:
            year_full_list = [next(file) for x in range(10)]
        cleared_list = []
        for line in year_full_list:
            cleared_list.append(line.rstrip().split())
        full_list.extend(cleared_list)
    for elem in full_list:
        elem[1] = int(elem[1])
    if start_year == finish_year:
        return get_final_top10(full_list)
    else:
        return period_of_year(full_list)


def get_list_for_set(start_year, finish_year, gender):
    """Forming a set to obtain universal names"""

    list_for_set = []
    for year in range(start_year, finish_year + 1):
        with open(f'BabyNames/{year}_{gender}Names.txt', 'r') as file:
            for i in file.readlines():
                list_for_set.append(i.rstrip().split())
    dict_for_set = {x[0]: x[1] for x in list_for_set}
    year_full_set = set(dict_for_set)
    return year_full_set


def get_result(start_year, finish_year):
    """Deleting the unzipped directory. Result Output"""

    boys_names = get_full_list(start_year, finish_year, 'Boys')
    girls_names = get_full_list(start_year, finish_year, 'Girls')
    set_boys_names = get_list_for_set(start_year, finish_year, 'Boys')
    set_girls_names = get_list_for_set(start_year, finish_year, 'Girls')
    set_general_names = set_boys_names & set_girls_names
    shutil.rmtree('BabyNames')
    if start_year == finish_year:
        years = f'{start_year}г'
    else:
        years = f'{start_year} - {finish_year}гг'
    result_string_top = f'10 самых популярных имён мальчиков за ' \
                        f'{years}: {", ".join(boys_names)} \n' \
                        f'10 самых популярных имён девочек за ' \
                        f'{years}: {", ".join(girls_names)} \n'
    if set_general_names:
        result_string = f'{result_string_top}' \
                        f'Универсальные имена в {years}: {", ".join(set_general_names)}'
    else:
        result_string = f'{result_string_top}' \
                        f'Универсальных имён в {years} нет.'
    return result_string


def get_years():
    """Accepts and validates user input"""

    period = input("Введите года:")
    message = 'Нет данных по введённым годам'

    if len(period) == 4:
        start_year = int(period)
        finish_year = start_year
        if 2013 < start_year or start_year < 1900:
            print(message)
        else:
            print(get_result(start_year, finish_year))
    elif len(period) == 9:
        start_year = int(period[:4])
        finish_year = int(period[5:])
        if 2013 < finish_year or start_year < 1900:
            print(message)
        else:
            print(get_result(start_year, finish_year))
    elif len(period) == 0:
        start_year = 1900
        finish_year = 2012
        print(get_result(start_year, finish_year))


if __name__ == "__main__":
    get_years()
