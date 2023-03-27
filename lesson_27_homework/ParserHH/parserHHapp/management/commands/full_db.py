# __________________________
from pprint import pprint
from pickle import dump, load
from os.path import exists
import re
from collections import Counter
from django.core.management.base import BaseCommand
from requests import get
from pycbrf import ExchangeRates
from django.core.exceptions import ObjectDoesNotExist
from parserHHapp.models import Word, Wordskill, Skill, Vacancy


class Command(BaseCommand):
    def __init__(self, vacancy, pages, where):
        super().__init__()
        self.vac = vacancy
        self.pages = pages
        self.where = where

    def handle(self, *args, **options):
        res = start(self.vac, pages=self.pages, where=self.where)
        print(res)
        add_words(res)
        add_skills(res)
        add_ws(res)

def start(vacancy, pages='3', where='all'):
    sk2 = parce(url='https://api.hh.ru/vacancies', vacancy=vacancy, pages=pages, where=where)
    sk3 = parce(url='https://api.zarplata.ru/vacancies', vacancy=vacancy, pages=pages, where=where)
    result = {'keywords': vacancy}
    res = (it for it in (sk2, sk3) if it)
    sk = {}
    for item in res:
        result['count'] = result.get('count', 0) + item['count']
        result['down'] = item['down'] if not result.get('down', None) else (result['down'] + item['down']) / 2
        result['up'] = item['up'] if not result.get('up', None) else (result['up'] + item['up']) / 2
        for it in item['requirements']:
            if sk.get(it['name'], {}):
                sk[it['name']] = {'count': sk[it['name']]['count'] + it['count'],
                                  'percent': round((sk[it['name']]['percent'] + it['percent']) / 2, 2)}
            else:
                sk[it['name']] = {'count': it['count'],
                                  'percent': it['percent']}
    # print(sk)
    result['requirements'] = sorted([{'name': it,
                                      'count': sk[it]['count'],
                                      'percent': sk[it]['percent']} for it in sk.keys() if it],
                                    key=lambda x: x['percent'],
                                    reverse=True)
    return result

def add_words(res):
    try:
        obj = Word.objects.get(word=res['keywords'])
        print(obj)
        if obj.count < res['count']:
            obj.count = res['count']
            obj.up = res['up']
            obj.down = res['down']
            obj.save()
            print('Edit')
        else:
            print('Not edit')
    except ObjectDoesNotExist:
        Word.objects.create(word=res['keywords'], count=res['count'], up=res['up'], down=res['down'])


def add_skills(res):
    for item in res['requirements']:
        try:
            r = Skill.objects.get(name=item['name'])
            print('skill not added')
        except ObjectDoesNotExist:
            Skill.objects.create(name=item['name'])


def add_ws(res):
    word = Word.objects.get(word=res['keywords'])
    for item in res['requirements']:
        skill = Skill.objects.get(name=item['name'])
        print(word, skill)
        r = Wordskill.objects.filter(id_word=word, id_skill=skill).first()
        if not r:
            Wordskill.objects.create(id_word=word, id_skill=skill, count=item['count'], percent=item['percent'])
            print('ws done')
        elif word.count < res['count']:
            r.count = item['count']
            r.percent = item['percent']
            print('ws edit')
        else:
            print('ws not edit')

def parce(url, vacancy, pages='3', where='all'):
        """
        Получение данных о средней максимальной и минимальной величине суммы в вакансии и 5 самых упоминаемых навыков
        :param vacancy: текст для поиска
        :param pages: количество страниц для анализа
        :param where: место, где будет искать текст
        :return: словарь с навыками
        """
        # url = 'https://api.hh.ru/vacancies'
        rate = ExchangeRates()
        if exists('area.pkl'):
            with open('area.pkl', mode='rb') as f:
                area = load(f)
        else:
            area = {}
        # получение первого запроса
        p = {
            'text': vacancy if where == 'all' else f'NAME: {vacancy}' if where == 'name' else f'COMPANY_NAME: {vacancy}'}
        r = get(url=url, params=p).json()
        # pprint(r)
        count_pages = r['pages']
        all_count = len(r['items'])
        result = {
            'keywords': vacancy,
            'count': all_count}
        sal = {'from': [], 'to': [], 'cur': []}
        skillis = []
        # перебор страниц в рамках ограничения
        for page in range(count_pages):
            if page > int(pages):
                break
            else:
                print(f"Обрабатывается страница {page}")
            p = {'text': vacancy,
                 'page': page}
            ress = get(url=url, params=p).json()
            all_count = len(ress['items'])
            result['count'] += all_count
            # перебор каждой вакансии
            for res in ress['items']:
                # pprint(res)
                skills = set()
                city_vac = res['area']['name']
                if city_vac not in area:
                    area[city_vac] = res['area']['id']
                ar = res['area']
                res_full = get(res['url']).json()
                # pprint(res_full)
                pp = res_full['description']
                # print(pp)
                pp_re = re.findall(r'\s[A-Za-z-?]+', pp)
                # print(pp_re)
                its = set(x.strip(' -').lower() for x in pp_re)
                # print(its)
                for sk in res_full['key_skills']:
                    skillis.append(sk['name'].lower())
                    skills.add(sk['name'].lower())
                # skills |= sk1
                for it in its:
                    if not any(it in x for x in skills):
                        skillis.append(it)
                if res_full['salary']:
                    code = res_full['salary']['currency']
                    if rate[code] is None:
                        code = 'RUR'
                    k = 1 if code == 'RUR' else float(rate[code].value)
                    sal['from'].append(
                        k * res_full['salary']['from'] if res['salary']['from'] else k * res_full['salary']['to'])
                    sal['to'].append(
                        k * res_full['salary']['to'] if res['salary']['to'] else k * res_full['salary']['from'])
        # создание словаря-счетчика для навыков
        sk2 = Counter(skillis)
        # pprint(sk2)
        up = sum(sal['from']) / len(sal['from'])
        down = sum(sal['to']) / len(sal['to'])
        # формирование результирующего словаря
        result.update({'down': round(up, 2),
                       'up': round(down, 2)})
        add = []
        for name, count in sk2.most_common(5):
            add.append({'name': name,
                        'count': count,
                        'percent': round((count / result['count']) * 100, 2)})
        result['requirements'] = add
        with open('area.pkl', mode='wb') as f:
            dump(area, f)
        return result


if __name__ == '__main__':
    parce('python', pages='0')