"""
7. (МОДУЛЬ 4) В проекте создать новый модуль victory.py. Задание
Написать или улучшить программу Викторина из предыдущего дз (Для тренировки предлагаю не пользоваться никакими библиотеками кроме random)
Есть 10 известных людей и их даты рождения в формате '02.01.1988' ('dd.mm.yyyy') - предлагаю для тренировки пока использовать строку
Программа выбирает из этих 10-и 5 случайных людей, это можно реализовать с помощью модуля random и функции sample
Пример использования sample:
import random
numbers = [1, 2, 3, 4, 5]

# 2 - количество случайных элементов
result = random.sample(numbers, 2)

print(result) # [5, 1]

После того как выбраны 5 случайных людей, предлагаем пользователю ввести их дату рождения
пользователь вводит дату в формате 'dd.mm.yyyy'

Например 03.01.2009, если пользователь ответил неверно, то выводим правильный ответ, но уже в следующем виде: третье января 2009 года, склонением можно пренебречь

В конце считаем количество правильных и неправильных ответов и предлагаем начать снова
"""
def victory():

    dict_pop = {'a': ['Алекса́ндр Серге́евич Пу́шкин', '26.05.1799', 'Двадцать шестое мая 1799 года'],
                'b': ['Лев Никола́евич Толсто́й', '09.09.1828', 'Девятое сентября 1828 года'],
                'c': ['Анто́н Па́влович Че́хов', '29.01.1860', 'Двадцать девятое января 1860 года'],
                'd': ['Фёдор Миха́йлович Достое́вский', '11.11.1821', 'Одиннадцатое ноября 1821 года'],
                'e': ['Никола́й Васи́льевич Го́голь', '01.04.1809', 'Первое апреля 1809 года'],
                'f': ['Ива́н Серге́евич Турге́нев', '09.11.1818', 'Девятое ноября 1818 года'],
                'g': ['Михаи́л Ю́рьевич Ле́рмонтов', '15.10.1814', 'Пятнадцатое октября 1814 года'],
                'h': ['Макси́м Го́рький', '28.03.1868', 'Двадцать восьмое марта 1868 года'],
                'i': ['Серге́й Алекса́ндрович Есе́нин', '03.10.1895', 'Третье октября 1895 года'],
                'j': ['Ива́н Алексе́евич Бу́нин', '22.10.1870', 'Двадцать второе октября 1870 года']}

    import random

    result = random.sample(dict_pop.keys(), 5)
    true_answear = 0
    for i in result:
        if i in dict_pop.keys():
            print()
            data = input(str(dict_pop[i][0]) + '   Введите дату его рождения в формате \'dd.mm.yyyy\' :')
            if data == dict_pop[i][1]:
                print('Верно')
                true_answear = true_answear + 1
            else:
                print(dict_pop[i][2])
    print('Верных ответов: ', true_answear)
    print('Неверных ответов: ', 5 - true_answear)
    print("Попробуйте снова.")


