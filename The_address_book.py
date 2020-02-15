import pickle, os, shutil

class Address_book:
    way_to_dir = os.path.abspath("save_AddressBook") #abspath() Достраивает путь к исполняемому файлу
    way_to_dict = way_to_dir + "\\" + "save_dict" + ".data"
    #Метод который создает папку save_Address_book
    def create_folder():
        if os.path.isdir(Address_book.way_to_dir) == False: #isdir() проверяет, есть ли папка
            os.mkdir(Address_book.way_to_dir) #mkdir() создает папку
        else:
            pass
    #Сохраняем словарь в файл.data
    def save_dict(dict):
        Address_book.create_folder()
        f = open(Address_book.way_to_dict, "wb")
        pickle.dump(dict, f)
        f.close()
    #Добавляем в словарь ключ:значение
    def add_to_dict(key, value):
        dict = Address_book.load_dict()#Загружаем словарь
        dict[key] = value              #В словарь dict вставляем ключ и значение
        return dict
    #Загружаем словарь из файла.data
    def load_dict():
        if os.path.isfile(Address_book.way_to_dict):
            f = open(Address_book.way_to_dict, "rb")
            return pickle.load(f)
        else:
            return {}
    #Удаляет папку
    def delete_all_dict():
        try:
            shutil.rmtree(Address_book.way_to_dir) #Удаляет папку со всем что внутри
        except:
            pass
    #Найти значение по ключу
    def find_key(key):
        load1 = Address_book.load_dict()
        try:
            find = load1[key]
        except:
            return None
        return find
    #Удалить ключ
    def delete_one_key(key):
        dict = Address_book.load_dict()
        try:
            dict.pop(key)
        except:
            return False
        Address_book.save_dict(dict)



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
