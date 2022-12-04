import json
import pprint
from collections import Counter
import requests
from pycbrf import ExchangeRates
import time

# Готовим переменные
total_vacancies = 0
salary = [[], []]
wages = {'from': 0, 'to': 0}
result = []
schedule = []
area = {}

# поиск городов
url = 'https://api.hh.ru/vacancies'
rate = ExchangeRates()

area_code = requests.get('https://api.hh.ru/areas/113').json()

for dict in area_code['areas']:
    area[dict['name'].lower()] = dict['id']
    for i in dict['areas']:
        area[i['name'].lower()] = i['id']

# Вводим вакансию
text = input('Введите вакансию : ')
# вводим город
try:
    area_persons = input('Введите город для поиска: ').lower()

    params = {'text': text, 'area': area[area_persons]}

    information = requests.get(url, params=params).json()

    pages = information['pages']

    # итоговый вывод сюда
    conclusion = {'keywords': text.capitalize(),
                  'count': 0,
                  'area': area_persons.capitalize(),
                  'requirements': [],
                  'salary': wages,
                  'schedule': []
                  }

    print('Идёт загрузка', information['found'], 'вакансий в -', area_persons.upper())
    # Проходим по страницам
    for page in range(pages):
        # if page > 10:
        #     break


        params = {'text': text, 'area': area[area_persons], 'page': page}
        information = requests.get(url, params=params).json()
        total_vacancies += len(information['items'])
        time.sleep(0.5)

        for inf in information['items']:
            # график работы
            schedule.append(inf['schedule']['name'])

            info = requests.get(inf['url']).json()
            # навыки
            for skill in info['key_skills']:
                result.append(skill['name'].lower())
            # зарплата
            if info['salary']:
                code = info['salary']['currency']
                if rate[code] is None:
                    code = 'RUR'
                k = 1 if code == 'RUR' else float(rate[code].value)  # С переводом валют, мне не очень понятно
                if info['salary']['from']:
                    salary[0].append(k * inf['salary']['from'])

                if info['salary']['to']:
                    salary[1].append(k * inf['salary']['to'])

    # print(result)
    wages['from'] = (int((sum(salary[0])) / len(salary[0])))
    wages['to'] = (int((sum(salary[1])) / len(salary[1])))
    conclusion['count'] = total_vacancies

    # pprint.pprint(information['items'])

    meter = Counter(result)
    for i in meter.most_common(7):
        conclusion['requirements'].append(i)

    schedule_count = Counter(schedule)
    for i in schedule_count.most_common():
        conclusion['schedule'].append(i)

    pprint.pprint(conclusion)

    # print(information['found'])
    # сохраняем в файл
    with open('conclusion.json', 'w') as f:
        json.dump(conclusion, f)

except KeyError:
    print('Город не найден')
except ZeroDivisionError:
    print('Выкансий не найдено!')

