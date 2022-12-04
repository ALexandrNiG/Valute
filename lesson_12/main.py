from flask import Flask # Подключаем flask

app = Flask(__name__) # Создаем объект класса Flask

@app.route('/') # Указываем путь нашей функции в обязательном декораторе
def hello():
    return 'Hello, World!'  # Пишем какую то функцию

app.run() # Запускаем приложение