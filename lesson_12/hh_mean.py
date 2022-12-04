"""
делаем запрос на hh, считаем среднюю зарплату и выделяем самые востребованные навыки
"""
import json
import re
import statistics
from collections import Counter
from pprint import pprint
from langdetect import detect
import requests

# делаем запрос на hh и сохраняем данные в переменную
url = 'https://api.hh.ru/vacancies'
params = {'text': 'junior machine learning', 'area': '1'}
res = requests.get(url, params=params).json()
# # pprint(res)
# with open('res.pkl', 'rb') as f:
#     res = pickle.load(f)
# списки для навыков и зарплаты
skills_list = []
total_salary = []

items = res['items']
# считаем зарплату,
salary_not_none = [item['salary'] for item in items if item['salary'] is not None]  # выделяем непустые элементы,
salary_value = [list(s.values()) for s in salary_not_none]  # создаем список со значениями словаря данных по з/п
# из полученного списка выделяем числовые данные, если з/п номинирована в долларах, умножаем на примерный курс рубля
for s in salary_value:
    for i in s:
        if type(i) is int and 'USD' in s:
            total_salary.append(i * 60)
        elif type(i) is int and 'RUR' in s:
            total_salary.append(i)
# считаем среднее по всем полученным значениям зарплаты
salary_mean = int(statistics.mean(total_salary))
print(salary_mean)
# выделяем необходимые навыки
# для простоты ищем только в описаниях на русском
requirement_ru = [item['snippet']['requirement'] for item in items if detect(item['snippet']['requirement']) == 'ru']
for r in requirement_ru:
    skills_requirement = re.findall(r'\s[A-Za-z]+', r)  # отбираем английские слова в русском тексте
    for i in skills_requirement:
        skills_reg_low_strip = i.strip(' -').lower()  # убираем пробелы и черточки и заглавные буквы
        skills_list.append(skills_reg_low_strip)  # создаем список навыков

skills_list_7 = Counter(skills_list).most_common(7) # считаем количество элементов в списке и отбираем 7 самых частых
pprint(skills_list_7)
# сохраняем полученные данные в json
with open('res.json', mode='w') as f:
    json.dump([skills_list_7], f)
    json.dump([salary_mean], f)