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


def get_year_dict(period=None) -> dict:
    """Print period and return dict with data for this period"""
    def get_period_dict() -> dict:
        """Return prepared data for period"""
        import zipfile
        z = zipfile.ZipFile('baby_names.zip', 'r')
        name_dict = {}

        for file_name in z.namelist():
            if period != '':
                period_list = period.split('-')
                if len(period_list) == 1:
                    _1_year, _2_year = int(period_list[0]), int(period_list[0])
                else:
                    _1_year, _2_year = int(period_list[0]), int(period_list[1])
            else:
                _1_year, _2_year = 1900, 2050

            if int(file_name[10:14]) in range(_1_year, _2_year + 1):
                with z.open(file_name, 'r') as opened_file:
                    file_content = opened_file.readlines()
                    name_dict[tuple(file_name[10:16].split('_'))] = file_content

        years_dict = {}

        for year_gender, names in name_dict.items():

            name_dict = {}

            for name in names:
                name_data = name[:-2].decode().split()
                name_dict[name_data[0]] = int(name_data[1])
            gender_dict = {}
            gender_dict[year_gender[1]] = name_dict

            if year_gender[0] not in years_dict.keys():
                years_dict[year_gender[0]] = gender_dict
            else:
                years_dict[year_gender[0]].update(gender_dict)

        return years_dict

    clear_years_dict = get_period_dict()

    if period == '':
        time_stamp = 'all time'
    else:
        time_stamp = f'{period}'
    result = clear_years_dict

    print(f'Data for {time_stamp}:')

    return result


def print_popular_name(input_dict: dict):
    """Print lists with most popular names in period"""
    g_pop_names = []
    b_pop_names = []
    for year, genders_dicts in input_dict.items():
        for gender, name_dict in genders_dicts.items():
            import heapq
            most_popular_in_num = heapq.nlargest(10, name_dict.values())
            for name, num in name_dict.items():
                if num in most_popular_in_num:
                    if gender == 'G':
                        g_pop_names.append(name)
                    else:
                        b_pop_names.append(name)
    print(f'Most popular boy names is: {", ".join(set(b_pop_names))}')
    print(f'Most popular girl names is: {", ".join(set(g_pop_names))}')


def print_generic_name(input_dict: dict):
    """Print lists with generic names in period"""
    g_name_list = []
    b_name_list = []
    for year, genders_dicts in input_dict.items():
        for gender, name_dict in genders_dicts.items():
            for name in name_dict.keys():
                if gender == 'G':
                    g_name_list.append(name)
                else:
                    b_name_list.append(name)
    g_name_set = set(g_name_list)
    b_name_set = set(b_name_list)
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
                y_dict = get_year_dict(per)
                print_popular_name(y_dict)
                print_generic_name(y_dict)
            except KeyError:
                print('In my opinion you made a mistake in year.')
            except ValueError:
                print('In my opinion you made a mistake in date.')
            except Exception as exc:  # debug
                print(type(exc))
                print('In my opinion you made a mistake... Somewhere.')
        else:
            exit('Closed by user')
