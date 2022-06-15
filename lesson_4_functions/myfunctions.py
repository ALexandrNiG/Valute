"""
МОДУЛЬ 1
В модуле прописаны заготовки для 8 функций
Под каждой функцией есть описание как она должна работать
ниже есть примеры использования функции
Задание: реализовать код функции, чтобы он работал по описанию и примеры использования давали верный результат
"""


def simple_separator():
    return '**********'

print(simple_separator())


def long_separator(count):
    return '*' * count

print(long_separator(3))
print(long_separator(4))


def separator(simbol, count):
    return simbol * count

print(separator('-', 10))
print(separator('#', 5))


def hello_world():
    return ' ********** \n Hello World! \n ##########'

print(hello_world())


def hello_who(who='World'):

    return ' ********** \n Hello '+ who +'! \n ##########'


print(hello_who())
print(hello_who('Max'))
print(hello_who('Kate'))


def pow_many(power, *args):
    resoult = 0
    # Функция складывает любое количество цифр и возводит результат в степень power (примеры использования ниже)
    for number in args:
        resoult += number
    return resoult ** power

print(pow_many(1, 1, 2))  # True -> (1 + 2)**1 == 3
print(pow_many(1, 2, 3))  # True -> (2 + 3)**1 == 5
print(pow_many(2, 1, 1))  # True -> (1 + 1)**2 == 4
print(pow_many(3, 2))  # True -> 2**3 == 8
print(pow_many(2, 1, 2, 3, 4))  # True -> (1 + 2 + 3 + 4)**2 == 10**2 == 100


def print_key_val(**kwargs):

    for a, b in kwargs.items():
       print( a,'-->', b)

print_key_val(name='Max', age=21)
print_key_val(animal='Cat', is_animal=True)


def my_filter(iterable, function):
    z = []
    for i in iterable:
        if function(i):
            z.append(i)
    return z

print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3))  # True == [4, 5]
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2))  # True == [2]
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3))  # True== [1, 2, 4, 5]
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba'))  # True == ['a', 'b']