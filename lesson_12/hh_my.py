import json
import pprint
from collections import Counter
import requests
from pycbrf import ExchangeRates
import time

total_vacancies = 0
# salary = [[], []]
# wages = {'from': 0, 'to': 0}
sal = {'from': [], 'to': []}

result = []
schedule = []
area = {}

url = 'https://api.hh.ru/vacancies'
rate = ExchangeRates()

area_code = requests.get('https://api.hh.ru/areas/113').json()

for dict in area_code['areas']:
    area[dict['name'].lower()] = dict['id']
    for i in dict['areas']:
        area[i['name'].lower()] = i['id']

text = input('Введите вакансию : ')
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
                  # 'salary': wages,
                  'sal' : sal,
                  'schedule': []
                  }

    print('Идёт загрузка', information['found'], 'вакансий в -', area_persons.upper())
    # Проходим по страницам
    for page in range(pages):
        params = {'text': text, 'area': area[area_persons], 'page': page}
        information = requests.get(url, params=params).json()
        total_vacancies += len(information['items'])
        time.sleep(0.5)

        for inf in information['items']:
            # условия работы
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
                k = 1 if code == 'RUR' else float(rate[code].value)
                sal['from'].append(k * inf['salary']['from'] if info['salary']['from'] else k * inf['salary']['to'])
                sal['to'].append(k * inf['salary']['to'] if info['salary']['to'] else k * inf['salary']['from'])
                # if info['salary']['from']:
                #     salary[0].append(k * inf['salary']['from'])
                #
                # if info['salary']['to']:
                #     salary[1].append(k * inf['salary']['to'])

    # wages['from'] = (int((min(salary[0]))))
    # wages['to'] = (int((max(salary[1]))))
    # sal['from'] = (int((min(sal[0]))))
    # sal['to'] = (int((max(sal[1]))))


    conclusion['count'] = total_vacancies

    meter = Counter(result)
    for i in meter.most_common(10):
        conclusion['requirements'].append(i)

    schedule_count = Counter(schedule)
    for i in schedule_count.most_common():
        conclusion['schedule'].append(i)

    pprint.pprint(conclusion)

    # сохраняем в файл
    with open('conclusion.json', 'w') as f:
        json.dump(conclusion, f)

except KeyError:
    print('Что-то пошло не так, проверьте вводимые данные')
except ZeroDivisionError:
    print('Вакансий не найдено!')