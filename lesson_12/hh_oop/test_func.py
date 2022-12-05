import pytest
import vacancy_func as vac
import search_func as search

class TestDictionaries:

    def test_get_areas(self):
        dictionary = vac.Dictionaries()
        list = [{'id': 1, 'name': 'N1', 'areas':[{'id': 11, 'name':'N11','areas':[]}, {'id':12, 'name':'N12', 'areas':[{'id':121, 'name':'N121', 'areas':[]}]}]}, {'id':2, 'name':'N2', 'areas':[]}]
        dictionary.get_areas(list)
        assert dictionary.areas == {'N1': 1, 'N11':11, 'N12':12, 'N121':121, 'N2':2}

class TestVacancy:

    def test_get_salary(self):
        vacancy = vac.Vacancy()
        vacancy.currency = {'usd': 0.016, 'rur': 1, 'kzt': 7 }
        salary = {'salary':{'from': 200000, 'to': 'null', 'gross': True , 'currency':'rur'}}
        vacancy.get_salary(salary)
        assert vacancy.salary_list == [{'low':174000, 'high':174000}]
        salary = {'salary': {'from': 3000, 'to': 5000, 'gross': False, 'currency': 'usd'}}
        vacancy.get_salary(salary)
        assert vacancy.salary_list == [{'low':174000, 'high':174000}, {'low': 187500, 'high': 312500}]
        salary = {}
        with pytest.raises(KeyError):
            vacancy.get_salary(salary)
        assert vacancy.salary_list == [{'low': 174000, 'high': 174000}, {'low': 187500, 'high': 312500}]
        salary = {'salary': {'from': 1050000, 'to': 1400000, 'gross': False, 'currency': 'kzt'}}
        vacancy.get_salary(salary)
        assert vacancy.salary_list == [{'low': 174000, 'high': 174000}, {'low': 187500, 'high': 312500}, {'low': 150000, 'high': 200000}]

    def test_get_skills(self):
        vacancy = vac.Vacancy()
        skill_dict = {'key_skills':[{'name':'s1'}, {'name':'s2'}, {'name':'s3'}]}
        vacancy.get_skills(skill_dict)
        assert vacancy.skills == {'s1':1, 's2':1, 's3':1}
        skill_dict = {'key_skills': [{'name': 's2'}, {'name': 's3'}, {'name': 's4'}]}
        vacancy.get_skills(skill_dict)
        assert vacancy.skills == {'s1': 1, 's2': 2, 's3': 2, 's4':1}

class TestSearch:

    def test_get_result(self):
        search_res = search.Search()
        search_res.vacancies_data.skills = {'s1': 1, 's2': 2, 's3': 2, 's4':1}
        search_res.vacancies_data.salary_list = [{'low': 130500, 'high': 174000}, {'low': 187500, 'high': 312500}, {'low': 150000, 'high': 200000}]
        search_res.search_count = 2908
        search_res.requirement_count = 2000
        search_res.search_vacancy = 'ttt'
        search_res.get_result()
        assert search_res.result ==  {'keywords': 'ttt', 'search_strict': False, 'area': 'None', 'count': 2908, 'salary': {'from': 156000, 'to': 228833, 'vacancy_with_salary': 3}, 'vacancy_for_requirements': 2000, 'requirements': [{'count': 2, 'name': 's2', 'percent': 33.3},{'count': 2, 'name': 's3', 'percent': 33.3},{'count': 1, 'name': 's1', 'percent': 16.7}, {'count': 1, 'name': 's4', 'percent': 16.7}]}
