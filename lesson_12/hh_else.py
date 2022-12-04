import requests
import pprint
from json import dump

DOMAIN = 'https://api.hh.ru/'
url = f'{DOMAIN}vacancies'
area = {}
text = input('Введите вакансию : ')
params = {'text': text }
information = requests.get(url, params=params).json()
pages = information['pages']
for i in range(pages):
    # if pages > 2:
    #     break

    params = {
            'text': text,
            'page': i+1
    }
    vacancies = requests.get(url, params=params).json()
    items = vacancies['items']

    skills = []
    for inf in information['items']:

        info = requests.get(inf['url']).json()
        # навыки
        for skill in info['key_skills']:
            skills.append(skill['name'].lower())


    skills_stats = [{'name': i, 'count': skills.count(i), 'percent': skills.count(i)*len(skills)/100}
                         for i in set(skills)]
    skills_stats.sort(key=lambda d: d['count'], reverse=True)

    pprint.pprint(skills_stats[:10])

    with open('vacancies_info.json', mode='w') as f:
        dump([skills_stats], f)



