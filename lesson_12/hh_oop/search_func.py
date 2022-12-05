import requests
import vacancy_func as vac

class Search:

    DOMAIN = 'https://api.hh.ru/'
    url_vacancies = f'{DOMAIN}vacancies'

    def __init__(self):
        self.per_page = 100
        self.areas_dict = dict()
        self.vacancies_data = vac.Vacancy()
        self.search_strict = False
        self.search_area = 'None'
        self.search_vacancy = ''
        self.search_count = 0
        self.requirement_count = 0
        self.result = dict()


    def get_search_data(self, params):
        params['per_page'] = self.per_page
        self.search_result = requests.get(self.url_vacancies, params=params).json()

    def get_vacancies_data(self):
        items = self.search_result['items']
        for i in range(len(items)):
            url_vacancy = items[i]['url']
            result_vacancy = requests.get(url_vacancy).json()
            self.vacancies_data.get_skills(result_vacancy)
            self.vacancies_data.get_salary(result_vacancy)

    def get_result(self):
        cnt = 0
        for skill in self.vacancies_data.skills:
            cnt += self.vacancies_data.skills[skill]
        list_skill = [{'name': skill, 'count': self.vacancies_data.skills[skill],
                       'percent': round(self.vacancies_data.skills[skill] * 100 / cnt, 1)} for skill in
                      self.vacancies_data.skills]
        list_skill = sorted(list_skill, key=lambda x: x['count'], reverse=True)

        cnt_salary = len(self.vacancies_data.salary_list)
        low = 0
        high = 0
        if cnt_salary > 0:
            for salary in self.vacancies_data.salary_list:
                low += salary['low']
                high += salary['high']
        else:
            cnt_salary = 1 #чтобы уйти от деления на 0
        self.result['keywords'] = self.search_vacancy
        self.result['search_strict'] = self.search_strict
        self.result['area'] = self.search_area
        self.result['count'] = self.search_count
        self.result['salary'] = {'from': round(low / cnt_salary), 'to': round(high / cnt_salary), 'vacancy_with_salary': cnt_salary}
        self.result['vacancy_for_requirements'] = self.requirement_count
        self.result['requirements'] = list_skill
