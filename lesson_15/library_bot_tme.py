# !pip install pyTelegramBotAPI
# Импорт библиотеки telebot
import telebot
# Импорт модуля apihelper
from telebot import apihelper
# Импорт библиотеки time
import time
# Импорт библиотеки os
import os

# Необходимо скопировать свой token
TOKEN = '5962545375:AAGvOCth5vhaYmdibRPi9ULWAiVh8gr5SNk'
# Зададим переменную с информацией о боте
bot = telebot.TeleBot(TOKEN)    # Определим бота, указав token
@bot.message_handler(commands=['start'])      # С помощью декоратора регистрируем функцию send_welcome как обработчик
def send_welcome(message):                            # На вход функции подадим сообщения в виде команд (commands)
    bot.reply_to(message, "Рад Вас приветствовать!")  # На выходе функции сообщение - Рад Вас приветствовать!

@bot.message_handler(commands=['timer'])          # С помощью декоратора регистрируем функцию timer как обработчик
def timer(message):                               # На вход функции подадим сообщение в виде команды /timer
    for i in range(5):                            # Пройдём по значениям в цикле от 0 до 5 (не включительно)
        time.sleep(1)                             # Задержка времени 1 секунда
        bot.send_message(message.chat.id, i + 1)  # Выведем числовое значения i + 1, где i - значение от 0 до 5
@bot.message_handler(commands=['say'])              # С помощью декоратора регистрируем функцию say как обработчик
def say(message):
    # Получим все, что после команды
    text = ' '.join(message.text.split(' ')[1:])    # Оазделим команду от текста, получив все после команды [1:]
    bot.reply_to(message, f'***{text.upper()}!***') # Выводим полученный текст заглавными буквами

# @bot.message_handler(content_types=['sticker'])     # С помощью декоратора регистрируем функцию send_sticker как обработчик
# def send_sticker(message):                          # На вход функции подадим сообщение
#     print(message)                                  # Выводим сообщение
#     bot.reply_to(message, "?")

@bot.message_handler(
    content_types=['sticker'])  # С помощью декоратора регистрируем функцию send_sticker как обработчик
def send_sticker(message):  # На вход функции подадим сообщение
    FILE_ID = 'CAACAgIAAxkBAAMUY8dCJJPg8T7EVfL9trFtWRol4AUAAg0EAAJ-8sUMZl-Djnw36eUtBA'  # Вводим полученный file_id
    bot.send_sticker(message.chat.id, FILE_ID)  # На выходе функции - стикер


# Команда администратора
# @bot.message_handler(commands=['admin'], func=lambda message: message.from_user.username == 'galaganenko_tat')  # С помощью декоратора регистрируем функцию admin как обработчик
# def admin(message):                 # На вход функции подадим сообщения в виде команды (commands)
#     print(message)                  # Выводим сообщение
#     info = os.name                  # Получим информацию об админе
#     bot.reply_to(message, info)     # Выводим полученную информацию

@bot.message_handler(commands=['admin'])                       # С помощью декоратора регистрируем функцию admin2 как обработчик
def admin(message):                                            # На вход функции подадим сообщения в виде команды (commands)
    if message.from_user.username == 'galaganenko_tat':
        info = os.name                                          # Получим информацию об админе
        bot.reply_to(message, info)                             # Выводим полученную информацию
    else:
        bot.reply_to(message, 'Метод недоступен, нет прав!')    # Выводим сообщение
bot.polling()  # Для начала работы необходимо запустить ячейку, для финала работы - остановить