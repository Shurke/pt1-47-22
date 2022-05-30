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


import glob
import zipfile


def read_zip() -> list:
    """Распаковывает архив с .txt файлами и указывает путь к ним

    :return: Возвращает отсортированный список, хранящий пути к .txt файлам из распакованного архива
    """
    baby_names = zipfile.ZipFile('baby_names.zip')
    baby_names.extractall()
    files = glob.glob("./BabyNames/*")

    return sorted(files)


def find_top(boys: list, girls: list) -> tuple:
    """Находит топ имён мальчиков и девочек

    :param boys: Список имён мальчиков
    :param girls: Список имён девочек
    :return: Возвращает кортеж топ имён мальчиков, девочек и универсальные имена
    """
    universal_names = [name for name in boys if name in girls]
    temp_boys = [boy for boy in boys if boy not in girls]
    temp_girls = [girl for girl in girls if girl not in universal_names]

    top_boys = temp_boys[:10]
    top_girls = temp_girls[:10]

    return top_boys, top_girls, universal_names


def find_top_by_gender(names: list) -> list:
    """Находит претендентов топ имён мальчиков или девочек

    :param names: Принимает список имён
    :return: Возвращает преобразованный список имён
    """
    list_of_names = []
    dict_names = {}

    for single_list in names:
        for string in single_list:
            list_of_names.append(string)

    for i in range(0, len(list_of_names) - 1, 2):
        dict_names[list_of_names[i]] = int(list_of_names[i + 1])

    sorted_names = {}
    sorted_keys = sorted(dict_names, key=dict_names.get, reverse=True)
    for value in sorted_keys:
        sorted_names[value] = dict_names[value]

    list_of_names.clear()
    for key in sorted_names:
        list_of_names.append(key)

    return list_of_names


def find_top_by_one_year(files: list, years: str) -> tuple:
    """Находит топ 10 имён из ввёденного года

    :param files: Список, хранящий пути к .txt файлам из распакованного архива
    :param years: Год, по которому ведём поиск топ 10 имён
    :return: Возвращает кортеж из двух вложенных списков, а точнее список топ-10 имён для
    мальчиков и девочек
    """
    find_year = []

    for item in files:
        find_year.append(item.find(years))

    index_of_desired_year = find_year.index(12)

    with open(files[index_of_desired_year], 'rt') as file:
        boys_names = file.read().split()
    with open(files[index_of_desired_year + 1], 'rt') as file:
        girls_names = file.read().split()

    boys = boys_names[0::2]
    girls = girls_names[0::2]
    top_boys, top_girls, universal_names = find_top(boys, girls)

    return top_boys, top_girls, universal_names


def find_top_by_range_of_year(files: list, years: str) -> tuple:
    """Находит топ 10 имён из ввёденного диапазона лет

    :param files: Список, хранящий пути к .txt файлам из распакованного архива
    :param years: Года, по которым ведём поиск топ 10 имён
    :return: Возвращает кортеж из двух вложенных списков, а точнее список топ-10 имён для
    мальчиков и девочек
    """
    boys = []
    girls = []

    for year in years:
        for item in files:
            index_of_desired_year = 12
            desired_year_for_boys = item.find(year + '_B')
            if desired_year_for_boys == index_of_desired_year:
                with open(item, 'rt') as file:
                    boys_names = file.read().split()
                    boys.append(boys_names)
            desired_year_for_girls = item.find(year + '_G')
            if desired_year_for_girls == index_of_desired_year:
                with open(item, 'rt') as file:
                    girls_names = file.read().split()
                    girls.append(girls_names)

    boys = find_top_by_gender(boys)
    girls = find_top_by_gender(girls)
    top_boys, top_girls, universal_names = find_top(boys, girls)

    return top_boys, top_girls, universal_names


def user_input():
    years_flag = 'Not defined yet'
    allowed_years = [str(i) for i in range(1900, 2013)]
    while True:
        flag = 'in process'
        print('Доступен период с 1900 по 2012 года, диапазон вводить в формате XXXX-XXXX')
        years = input('Введите год или диапазон лет для поиска топ 10 имён: ')

        if len(years) == 0:
            years_flag = 'not input'
            years = '1900-2012'
            years = years.split('-')
            years = [int(i) for i in years]
            years = [str(i) for i in range(years[0], years[1] + 1)]
        elif len(years) == 4:
            years_flag = 'year'
            years = [years]
        elif len(years) == 9:
            years_flag = 'period of years'
            years = years.split('-')
            years = [int(i) for i in years]
            years = [str(i) for i in range(years[0], years[1] + 1)]

        for year in years:
            if year not in allowed_years:
                flag = 'failed'
            else:
                flag = 'success'

        if flag == 'success':
            break

    return years, years_flag


def main():
    years, years_flag = user_input()
    files = read_zip()
    universal_names = []

    if years_flag == 'year':
        top_boys, top_girls, universal_names = find_top_by_one_year(files, years[0])
        print(f'Список популярных имён для мальчиков: {top_boys}\n'
              f'Список популярных имён для девочек: {top_girls}')
    elif years_flag == 'period of years':
        top_boys, top_girls, universal_names = find_top_by_range_of_year(files, years)
        print(f'Список популярных имён для мальчиков: {top_boys}\n'
              f'Список популярных имён для девочек: {top_girls}')
    elif years_flag == 'not input':
        top_boys, top_girls, universal_names = find_top_by_range_of_year(files, years)
        print(f'Список имён с 1900 по 2012 года.\n'
              f'Список популярных имён для мальчиков: {top_boys}\n'
              f'Список популярных имён для девочек: {top_girls}')

    if len(universal_names) == 0:
        print('Универсальных имён нет')
    else:
        print(f'Универсальные имена: {universal_names}')


if __name__ in '__main__':
    main()
