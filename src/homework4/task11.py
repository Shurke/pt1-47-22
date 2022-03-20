"""
Набор данных, содержащий детские имена, состоит более чем из 200 файлов, в каждом из которых, помимо
сотни имен, указано количество названных тем или иным именем детей. При этом файлы отсортированы по
убыванию популярности имен. Для каждого года присутствует по два файла: в одном перечислены мужские
имена, в другом – женские. Совокупный набор данных содержит информацию для всех лет, начиная с
1900-го и заканчивая 2012-м.

Напишите программу, которая будет считывать данные (baby_names.zip) и предоставлять следующие
результаты:
    имена, которые были лидерами (топ-10) по частоте использования как минимум в одном году. На
    выходе должно получиться два списка: в одном из них будут присутствовать наиболее популярные
    имена для мальчиков, во втором – для девочек. При этом списки не должны содержать повторяющиеся
    имена.

    имена, использованные для мальчиков и девочек (универсальные имена). Если в этом году
    универсальных имен не было, нужно известить об этом пользователя. Кроме того, если за указанный
    пользователем год не было данных по именам, выведите соответствующее сообщение об ошибке.

Предусмотреть возможность работать с каким-то ограниченным периодом времени или с конкретным годом.
Например, ваша программа должна корректно вывести данные, если пользователь ввел “1990-1995” или
просто “1996”. Если пользователем на вход программы не передал никаких данных, то необходимо вывести
все данные за все время.
"""


def get_data_from_file(file_name='baby_names.zip', period=''):
    """Print search period and return dict with data for period or False"""
    import zipfile
    z = zipfile.ZipFile(file_name, 'r')

    if period == '':
        date_list = tuple(range(1800, 2051))
        period = 'all time'
    elif len(period) == 4:
        date_list = (int(period)),
    elif len(period) == 9:
        date_list = tuple(range(int(period[:4]), int(period[5:]) + 1))
    else:
        print('Some trouble with period')
        return False
    print(f'Search data for {period}:')

    name_in_years_dict = {}

    for file_name in z.namelist():
        if int(file_name[10:14]) in date_list:
            with z.open(file_name, 'r') as opened_file:
                file_content = opened_file.readlines()
                file_dict_with_name_frequency = {}
                for elem in file_content:
                    elem_list = elem.decode()[:-2].split()
                    file_dict_with_name_frequency[elem_list[0]] = int(elem_list[1])
                name_in_years_dict[tuple(file_name[10:
                                                   16].split('_'))] = file_dict_with_name_frequency

    return name_in_years_dict


def print_popular_name(input_dict: dict):
    """Print lists with most popular (top 10) names"""
    g_pop_names = set()
    b_pop_names = set()
    for year_gender, names in input_dict.items():
        import heapq
        most_popular_in_num = heapq.nlargest(10, names.values())
        for name, num in names.items():
            if num in most_popular_in_num:
                if year_gender[1] == 'G':
                    g_pop_names.update({name})
                else:
                    b_pop_names.update({name})
    print(f'Most popular boy names is: {", ".join(b_pop_names)}')
    print(f'Most popular girl names is: {", ".join(g_pop_names)}')


def print_generic_name(input_dict: dict):
    """Print lists with generic names"""
    g_name_set = set()
    b_name_set = set()
    for year_gender, names in input_dict.items():
        for name in names.keys():
            if year_gender[1] == 'G':
                g_name_set.update({name})
            else:
                b_name_set.update({name})
    generic_set = g_name_set.intersection(b_name_set)
    if generic_set:
        print(f'Generic names: {", ".join(generic_set)}')
    else:
        print('No generic names.')


if __name__ == '__main__':
    while True:
        per = input('Please type an interval, leave empty if you would like to see the data for'
                    ' all time, or exit: ')
        if per != 'exit':
            try:
                y_dict = get_data_from_file(period=per)
                print_popular_name(y_dict)
                print_generic_name(y_dict)
            except KeyError:
                print('In my opinion you made a mistake in year.')
            except (ValueError, AttributeError):
                print('In my opinion you made a mistake in date.')
            except Exception as exc:  # debug
                print(type(exc))
                print('In my opinion you made a mistake... Somewhere.')
        else:
            exit('Closed by user')
