from pprint import pprint

from requests import get


url = 'https://api.hh.ru/vacancies'
params = {'text': 'python'}
res = get(url, params=params).json()
print(res['found'])
pprint(res['items'])



#
# import requests
# import pprint

# url = 'https://api.hh.ru/vacancies'
#
# params = {
#     'text': 'java developer',
#     # есть страницы т.к. данных много
#     'page': 1
# }
#
# result = requests.get(url, params=params).json()
#
# pprint.pprint(result)
#
# items = result['items']
#
# first = items[0]
#
# print(first['url'])
#
# result = requests.get(first['url'], params=params).json()
#
# print(result)
#
# url = 'https://api.hh.ru/vacancies'
#
# params = {
#     'text': 'NAME:(Python OR Java) AND COMPANY_NAME:(1 OR 2 OR YANDEX) AND (DJANGO OR SPRING)',
#     # есть страницы т.к. данных много
#     'page': 1
# }
#
# result = requests.get(url, params=params).json()
#
# pprint.pprint(result)
# print(result['items'][0]['url'])
# print(result['items'][0]['alternate_url'])