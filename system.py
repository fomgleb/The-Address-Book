from func import *

Choice = ""
while True:
    Choice = input('''-----------------------------------------------------------------------------------
Введите команду: ''')
    Choice = Choice.lower().replace(" ", "")
    if Choice == "список" or Choice == "с":
        dir = Address_book.load_dict()
        if len(dir) == 0:
            print("Пусто")
        else:
            print(f"{'|Имя|': >40}:|Адрес|")

            for key in dir:
                print(f"{key: >39} : {dir[key]}")
    elif Choice == "найти" or Choice == "н":
        value = Address_book.find_key(input("Имя: "))
        if value == None:
            print("Не найдено")
        else:
            print(f"Адрес: {value}")
    elif Choice == "добавить" or Choice == "д":
        Address_book.save_dict(Address_book.add_to_dict(input("Имя: "), input("Адрес: ")))
    elif Choice == "удалить" or Choice == "у":
        key = Address_book.delete_one_key(input("Что: "))
        if key == False:
            print("Не найдено")
        else:
            print("Успешно удалено")
    elif Choice == "удалитьвсе" or Choice == "удалитьвсё" or Choice == "ув":
        Address_book.delete_all_dict()
        print("Успешно удалено")
    elif Choice == "помощь" or Choice == "п":
        print("""Команды:
    'список'или'с' - показать всю адресную книгу
    'найти'или'н' - найти адрес по имени
    'добавить'или'д' - добавить имя:адрес в список
    'удалить'или'у' - удалить имя:адрес из списка
    'удалить все'или'ув' - удалить весь список
    'выход'или'в' - выйти из программы""")
    elif Choice == "выход" or Choice == "в":
        break
    else:
        print("Введите 'помощь', что бы посмотреть список команд")
