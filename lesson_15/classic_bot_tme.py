# Импорт библиотеки requests для работы с запросами
import requests

# Импорт библиотеки pprint для вывода данных
import pprint

# Импорт библиотеки time
import time

from os import getenv
# библиотека для загрузки данных из env
from dotenv import load_dotenv
# метода ищет файл env и переменные из него
load_dotenv()

# достает из файла переменную token
TOKEN = getenv('TOKEN')


# Необходимо скопировать свой token
# Зададим переменную с информацией о боте
BOT_URL = f'https://api.telegram.org/bot{TOKEN}'
print('# Выведем информацию: BOT_URL = ', BOT_URL)

url = f'{BOT_URL}/getMe'
print('# Выведем информацию: url = /getMe', url)

# Для того, чтобы подстраховаться и не возникало ошибок, можно использовать прокси, в зависмости от провайдера интернета, прокси может не понадобится.
# Указанные адреса могут не работать, тогда нужно подобрать из бесплатных proxy для обхода блокировки
proxies = {
    'http': 'https://173.245.49.19:80',
}

# proxies = {
#     'http': 'http://167.86.96.4:3128',
# }
# *Проверим работу с прокси.
result = requests.get(url, proxies=proxies)
print(result)

# Запуск без прокси (как альтернатива):
result = requests.get(url)
print(result)

# Выведем подробную информацию о нашем боте
pprint.pprint(result.json())
# Выведем информации другим способом
print(result.text)
# Проверим статус код
print(result.status_code)

# Рассмотрим метод getUpdates, для получения обновлений.
url = f'{BOT_URL}/getUpdates'
result = requests.get(url, proxies=proxies)
pprint.pprint(result.json())

# Теперь, получив сообщение, ответим на него. Сделать это можно с помощью метода sendMessage.
url_send = f'{BOT_URL}/sendMessage'
# Получим список сообщений.
messages = result.json()['result']
for message in messages:  # В цикле пройдем по списку всех сообщений
    chat_id = message['message']['chat']['id']  # Получим значение id сообщения
    params = {
        'chat_id': chat_id,  # Назначим id сообщения
        'text': 'Добрый день!'  # Задаем текст сообщения
    }

    answer = requests.post(url_send, params=params, proxies=proxies)  # Выводим сообщение "Добрый день!"



# Цикл для вывода сообщения от бота для каждого сообщения от пользователя
while True:
    time.sleep(5)                                       # Задержка времени 5 секунд
    url = f'{BOT_URL}/getUpdates'                       # Обновим информацию

    result = requests.get(url, proxies=proxies)         # Делаем get запрос

    pprint.pprint(result.json())                        # Выведем результат обновления

    messages = result.json()['result']                  # Поместим в json файл полученную информацию о сообщении от пользователя

    for message in messages:                            # В цикле пройдем по списку всех сообщений

        chat_id = message['message']['chat']['id']      # Получим значение id сообщения
        url_send = f'{BOT_URL}/sendMessage'             # С помощью метода sendMessage ответим на сообщение пользователя
        params = {
            'chat_id': chat_id,                         # Назначим id сообщения
            'text': 'Добрый день!'                      # Задаем текст сообщения
        }

        answer = requests.post(url_send, params=params, proxies=proxies)    # Выводим сообщение "Добрый день!"