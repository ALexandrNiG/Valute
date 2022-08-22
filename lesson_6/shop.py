"""
1. В подпрограмме Мой банковский счет;
2. Добавить сохранение суммы счета в файл.

При первом открытии программы на счету 0
После того как мы воспользовались программой и вышли сохранить сумму счета
При следующем открытии программы прочитать сумму счета, которую сохранили
...
3. Добавить сохранение истории покупок в файл

При первом открытии программы истории нет.
После того как мы что нибудь купили и закрыли программу сохранить историю покупок.
При следующем открытии программы прочитать историю и новые покупки уже добавлять к ней;
...
4. Формат сохранения количество файлов и способ можно выбрать самостоятельно.
"""
story = {}
cash = 0
with open("story.txt",'r', encoding='utf-8' ) as out:
    for line in out:
        key, *value = line.split()
        story[key] = value


with open('cash.txt', 'r') as f:
    cash = int(f.read())
    # cash = f.read()
    print(cash)
while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню ')
    if choice == '1':
        result = int(input("Введите сумму "))
        cash += result
        pass
    elif choice == '2':
        print(cash)
        product = int(input("Введите стоимость товара "))

        if cash - product >= 0:
            cash = cash - product
            name = str(input("Введите наименование товара "))
            story[name] = product
            with open('story.txt', 'w', encoding='utf-8') as out:
                for key, val in story.items():
                    out.write('{}:{}\n'.format(key, val))

        else:
            сash = cash + product
            print("Нехватает средств на счете")
        pass
    elif choice == '3':

        print(story)
        pass
    elif choice == '4':
        with open('cash.txt', 'w') as f:
            # сash = str(cash)
            f.write(str(cash))
        break
    else:
        print('Неверный пункт меню')