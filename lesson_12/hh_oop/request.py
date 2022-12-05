import search_func as search
import vacancy_func as vac
import json

search_res = search.Search()
search_res.search_vacancy = input('Введите вакансию для поиска: ')
params = dict()


# точный поиск
if ' ' in search_res.search_vacancy:
    strict_search = ''
    while strict_search not in ['y', 'n']:
        strict_search = input('Строгий поиск: y/n ').lower()
    if strict_search == 'y':
        params['text'] = f'\"{search_res.search_vacancy}\"'
        search_res.search_strict = True
    else:
        params['text'] = search_res.search_vacancy
        search_res.search_strict = False
else:
    params['text'] = search_res.search_vacancy

hh_dict = vac.Dictionaries()

# поиск по региону
search_by_area = ''
while search_by_area not in ['y','n']:
    search_by_area = input('Нужен поиск по региону? y/n ').lower()
search_by_area_res = True if search_by_area == 'y' else False
if search_by_area_res:
    area_str = ''
    hh_dict.init_areas()
    search_res.areas_dict = hh_dict.areas
    while area_str not in search_res.areas_dict:
        area_str = input('Введите регион поиска: ')
    params['area'] = search_res.areas_dict[area_str]
    search_res.search_area = area_str
params['page'] = 0

search_res.get_search_data(params)
search_res.search_count = search_res.search_result['found']
search_res.requirement_count = 2000 if search_res.search_count > 2000 else search_res.search_count
pages = search_res.search_result['pages']

print('Всего найдено вакансий', search_res.search_count)

if search_res.search_count == 0:
    print('Вакансии не найдены, измените критерии')
else:
    hh_dict.init_currency()
    search_res.vacancies_data.currency = hh_dict.currency
    search_res.get_vacancies_data()
    print(f'обработано {min(search_res.search_count, search_res.per_page)}')
    if pages > 1:
        for page in range(1, pages):
            params['page'] = page
            search_res.get_search_data(params)
            search_res.get_vacancies_data()
            print(f'обработано {min(search_res.search_count, search_res.per_page * (page + 1))}')

search_res.get_result()
res = json.dumps(search_res.result)
with open('search_result.json', 'a') as f:
    f.write(f'{res}\n')