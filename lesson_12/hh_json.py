from pprint import pprint
from pickle import dump, load
from os.path import exists
import re
from collections import Counter
from json import dump as jdump

from requests import get
from pycbrf import ExchangeRates

#  ввод интерисующей вакансии
vacancy = input('Введите интересующую вакансию: ')
url = 'https://api.hh.ru/vacancies'
rate = ExchangeRates() # загрузка текущих курсов валют
# загрузка файла с цифровыми кодами
if exists('area.pkl'):
    with open('area.pkl', mode='rb') as f:
        area = load(f)
else:
    area = {}
p = {'text': vacancy }
r = get(url=url, params=p).json()
count_pages = r['pages']
all_count = len(r['items'])
result = {
        'keywords': vacancy,
        'count': all_count}
sal = {'from': [], 'to': []}
skillis = []
# сначала выявляем сколько будет получено страниц
# и готовим нужные переменные. А затем проходим по каждой из полученных страниц.
for page in range(count_pages):
    if page > 2:
        break
    else:
        print(f"Обрабатывается страница {page}")
    p = {'text': vacancy,
         'page': page}
    ress = get(url=url, params=p).json()
    all_count = len(ress['items'])
    result['count'] += all_count
    for res in ress['items']:
        skills = set()
        res_full = get(res['url']).json()
        #  обработка описания вакансии
        pp = res_full['description']
        pp_re = re.findall(r'\s[A-Za-z-?]+', pp)
        its = set(x.strip(' -').lower() for x in pp_re)
        for sk in res_full['key_skills']:
            skillis.append(sk['name'].lower())
            skills.add(sk['name'].lower())
        for it in its:
            if not any(it in x for x in skills):
                skillis.append(it)
        #окончание формирования списка навыков
        # # обработка заплаты
        if res_full['salary']:
            code = res_full['salary']['currency']
            if rate[code] is None:
                code = 'RUR'
            k = 1 if code == 'RUR' else float(rate[code].value)
            sal['from'].append(k * res_full['salary']['from'] if res['salary']['from'] else k * res_full['salary']['to'])
            sal['to'].append(k * res_full['salary']['to'] if res['salary']['to'] else k*res_full['salary']['from'])
sk2 = Counter(skillis)
up = sum(sal['from']) / len(sal['from'])
down = sum(sal['to']) / len(sal['to'])
result.update({'down': round(up, 2),
               'up': round(down, 2)})
add = []
for name, count in sk2.most_common(5):
    add.append({'name': name,
                'count': count,
                'percent': round((count / result['count'])*100, 2)})
result['requirements'] = add
pprint(result)
# сохранение файла с результами работы
with open('result.json', mode='w') as f:
    jdump([result], f)
with open('area.pkl', mode='wb') as f:
    dump(area, f)