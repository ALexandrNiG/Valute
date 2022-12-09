'''
ЗАДАНИЕ 2
5. В программе консольный файловый менеджер есть пункт "просмотр содержимого рабочей директории";
6. Добавить пункт "сохранить содержимое рабочей директории в файл";
7. При выборе этого пункта создать файл listdir.txt (если он есть то пересоздать) и сохранить туда
содержимое рабочей директории следующим образом: сначала все файлы, потом все папки, пример как может выглядеть итоговый файл.
files: victory.py, bill.py, main.py
dirs: modules, packages
'''
import os
import shutil
import sys
import victory
import shop
import pathlib
from os import walk


while True:
    try:
        print('1 создать папку')
        print('2 удалить(файл / папку)')
        print('3 копировать(файл / папку)')
        print('4 просмотр содержимого рабочей директории')
        print('5 сохранить содержимое рабочей директории в файл')
        print('6 посмотреть только папки')
        print('7 посмотреть только файлы')
        print('8 просмотр информации об операционной системе')
        print('9 создатель программы')
        print('10 играть в викторину')
        print('11 мой банковский счет')
        print('12 выход.')

        choice = input('Выберите пункт меню ')
        if choice == '1':
            name = input("Введите имя создаваемой папки")
            os.mkdir(name)
            pass
        elif choice == '2':
            namedell = input("Введите имя удаляемой папки/файла")
            if (os.path.isfile(namedell)):
                os.remove(namedell)
            else:
                os.rmdir(namedell)
            pass
        elif choice == '3':
            copyname = input("Введите имя копируемой папки/файла")
            name2 = input("Введите имя копии файла папки/файла")
            shutil.copyfile(copyname,name2)


        elif choice == '4':
            print(os.listdir())

        elif choice == '5':
            with open("listdir.txt", "w+", encoding='utf-8') as f:

                # for (dirpath, dirnames, filenames) in walk('.'):
                #     print(dirpath)
                print(dirpath for (dirpath, dirnames, filenames) in walk('.'))

                    coord = {'dirs': dirnames, 'files': filenames}


                    # for key, val in coord.items():
                    #     f.write('{}:{}\n'.format(key, val))
                    (f.write('{}:{}\n'.format(key, val)) for key, val in coord.items())


        elif choice == '6':
            # for (dirpath, dirnames, filenames) in walk('.'):
            #     print(dirnames)
            print(dirnames for (dirpath, dirnames, filenames) in walk('.'))

        elif choice == '7':
            # for (dirpath, dirnames, filenames) in walk("."):
            #     print(filenames)
            print(filenames for (dirpath, dirnames, filenames) in walk('.'))
            pass
        elif choice == '8':
            print(sys.platform)

        elif choice == '9':
            print("Александр Николаевич")
            pass
        elif choice == '10':
            victory.victory()
            pass
        elif choice == '11':
            shop.shop()
            pass
        elif choice == '12':
            break
    # else: меняем на :
    except:
        print('Неверный пункт меню')