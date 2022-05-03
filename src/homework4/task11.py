"""
Детские имена
Набор данных, содержащий детские имена, состоит более чем из 200 файлов, в каждом из которых,
помимо сотни имен, указано количество названных тем или иным именем детей. При этом файлы
отсортированы по убыванию популярности имен. Для каждого года присутствует по два файла:
в одном перечислены мужские имена, в другом – женские. Совокупный набор данных содержит
информацию для всех лет, начиная с 1900-го и заканчивая 2012-м.
Напишите программу, которая будет считывать данные (baby_names.zip) и предоставлять следующие
результаты: имена, которые были лидерами (топ-10) по частоте использования как минимум в одном году.
На выходе должно получиться два списка: в одном из них будут присутствовать наиболее популярные
имена для мальчиков, во втором – для девочек. При этом списки не должны содержать повторяющиеся
имена. имена, использованные для мальчиков и девочек (универсальные имена). Если в этом году
универсальных имен не было, нужно известить об этом пользователя. Кроме того, если за указанный
пользователем год не было данных по именам, выведите соответствующее сообщение об ошибке.
Предусмотреть возможность работать с каким-то ограниченным периодом времени или с конкретным годом.
Например, ваша программа должна корректно вывести данные, если пользователь ввел “1990-1995” или
просто “1996”. Если пользователем на вход программы не передал никаких данных,
то необходимо вывести все данные за все время.
"""

import zipfile
import glob


def read_zip() -> list:
    """Распаковывает архив с .txt файлами и указывает путь к ним

    :return: Возвращает отсортированный список, хранящий пути к .txt файлам из распакованного архива
    """
    baby_names = zipfile.ZipFile('baby_names.zip')
    baby_names.extractall()
    files = glob.glob("./BabyNames/*")

    return sorted(files)


def find_top_by_one_year(files: list, years: str) -> tuple:
    """Находит топ 10 имён из ввёденного года

    :param files: Список, хранящий пути к .txt файлам из распакованного архива
    :param years: Год, по которому ведём поиск топ 10 имён
    :return: Возвращает кортеж из двух вложенных списков, а точнее список топ-10 имён для
    мальчиков и девочек
    """
    boys = []
    girls = []
    universal_names = []
    find_year = []

    for item in files:
        find_year.append(item.find(years))

    with open(files[find_year.index(12)], 'rt') as file:
        boys_names = file.read().split()
    with open(files[find_year.index(12) + 1], 'rt') as file:
        girls_names = file.read().split()

    for boy in boys_names[0::2]:
        if boy in girls_names:
            universal_names.append(boy)
        else:
            boys.append(boy)

    for girl in girls_names[0::2]:
        if girl not in universal_names:
            girls.append(girl)

    top_boys = boys[0:10]
    top_girls = girls[0:10]

    if len(universal_names) == 0:
        print('Универсальных имён нет')
    else:
        print(f'Универсальные имена: {universal_names}')

    return top_boys, top_girls


def find_top_by_range_of_year(files: list, years: str) -> tuple:
    """Находит топ 10 имён из ввёденного диапазона лет

    :param files: Список, хранящий пути к .txt файлам из распакованного архива
    :param years: Года, по которым ведём поиск топ 10 имён
    :return: Возвращает кортеж из двух вложенных списков, а точнее список топ-10 имён для
    мальчиков и девочек
    """
    boys = []
    girls = []
    boys_temp = []
    girls_temp = []
    dict_boys = {}
    dict_girls = {}
    universal_names = []

    years = years.replace('-', ' ').split()
    years = [int(i) for i in years]
    years = [str(i) for i in range(years[0], years[1] + 1)]

    for year in years:
        for item in files:
            if item.find(year + '_B') == 12:
                with open(item, 'rt') as file:
                    boys_names = file.read().split()
                    boys.append(boys_names)
            if item.find(year + '_G') == 12:
                with open(item, 'rt') as file:
                    girls_names = file.read().split()
                    girls.append(girls_names)

    for i in boys:
        for j in i:
            boys_temp.append(j)
    for i in girls:
        for j in i:
            girls_temp.append(j)

    for i in range(0, len(boys_temp) - 1, 2):
        dict_boys[boys_temp[i]] = int(boys_temp[i + 1])
    for i in range(0, len(girls_temp) - 1, 2):
        dict_girls[girls_temp[i]] = int(girls_temp[i + 1])

    sorted_boys = {}
    sorted_keys = sorted(dict_boys, key=dict_boys.get, reverse=True)
    for v in sorted_keys:
        sorted_boys[v] = dict_boys[v]

    sorted_girls = {}
    sorted_keys = sorted(dict_girls, key=dict_girls.get, reverse=True)
    for v in sorted_keys:
        sorted_girls[v] = dict_girls[v]

    boys_temp.clear()
    for k in sorted_boys:
        boys_temp.append(k)

    girls_temp.clear()
    for k in sorted_girls:
        girls_temp.append(k)

    boys.clear()
    for boy in boys_temp:
        if boy in girls_temp:
            universal_names.append(boy)
        else:
            boys.append(boy)

    girls.clear()
    for girl in girls_temp:
        if girl not in universal_names:
            girls.append(girl)

    top_boys = boys[0:10]
    top_girls = girls[0:10]

    if len(universal_names) == 0:
        print('Универсальных имён нет')
    else:
        print(f'Универсальные имена: {universal_names}')

    return top_boys, top_girls


def main():
    files = read_zip()
    print('Доступен период с 1900 по 2012 года')
    years = input('Введите год или диапазон лет для поиска топ 10 имён: ')

    if len(years) == 4:
        top_boys, top_girls = find_top_by_one_year(files, years)
        print(f'Список популярных имён для мальчиков: {top_boys}\n'
              f'Список популярных имён для девочек: {top_girls}')
    elif len(years) == 9:
        top_boys, top_girls = find_top_by_range_of_year(files, years)
        print(f'Список популярных имён для мальчиков: {top_boys}\n'
              f'Список популярных имён для девочек: {top_girls}')
    elif len(years) == 0:
        years = '1900-2012'
        top_boys, top_girls = find_top_by_range_of_year(files, years)
        print(f'Список популярных имён для мальчиков: {top_boys}\n'
              f'Список популярных имён для девочек: {top_girls}')


if __name__ in '__main__':
    main()
