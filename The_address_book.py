import pickle, os, shutil

class Address_book:
    way_to_dir = os.path.abspath("save_AddressBook") #abspath() там где находится командная строка or исполняемый файл достраивает путь
    #Метод который создает папку Address_book
    def create_dir():
        if os.path.isdir(Address_book.way_to_dir) == False: #isdir() проверяет есть ли папка
            os.mkdir(Address_book.way_to_dir) #mkdir() создает папку
        else:
            pass
    #Убирает все из строки, что написано в переменной forbidden
    def delete_forbidden(string):
        forbidden = (",","?","!",":",";","-","(",")","[","]","'","«","»","/",'"')
        for i in forbidden:
            return string.replace(i, "")
    #Создает файл.data, который содержит словарь
    def create_data(name, address):
        Address_book.create_dir()
        new_name = Address_book.delete_forbidden(name)
        dict = {name:address}
        f = open(Address_book.way_to_dir+"\\"+new_name+".data", "wb") #открываем
        pickle.dump(dict, f) #Вгружаем
        f.close()
    #В файле словарь, из словаря берётся значение и возвращается
    def return_address(name):
        name = Address_book.delete_forbidden(name)
        if os.path.isfile(Address_book.way_to_dir+"\\"+name+".data") == False: #isfile() - есть такой файл, или нет
            address = f"Не удалось найти {name}"
        else:
            f = open(Address_book.way_to_dir+"\\"+name+".data", "rb")
            file_load = pickle.load(f) #загружаем
            for value in file_load:
                address = file_load[value] # возвращаем значение, а ключ не.
        return address
    # возвращает список в котором словари, все словари.
    def print_all_dict():
        Address_book.create_dir()
        files = os.listdir(Address_book.way_to_dir) #получаем список всех файлов в директории
        list = []
        for file in files: #открываем и загружаем в список каждый словарь из файлов другого списка
            f = open(Address_book.way_to_dir+"\\"+file, "rb")
            file_load = pickle.load(f)
            list.append(file_load)
            f.close()
        if list == []:
            list = "Пусто"
        return list
    #Удаляет из директории указаный файл
    def delete_dict(name):
        name = Address_book.delete_forbidden(name)
        try:
            os.remove(Address_book.way_to_dir+"\\"+name+".data")
        except:
            return f"Не удается найти {name}"
        else:
            return "Успешно удалено"
    #Удаляет папку со всем что внутри
    def delete_all_dict():
        try:
            shutil.rmtree(Address_book.way_to_dir) #Удаляет папку со всем что внутри
        except:
            pass
        return "Успешно удалено"


Choice = ""
while Choice != "выход":
    Choice = input("\nВведите команду: ")
    Choice = Address_book.delete_forbidden(Choice.lower().replace(" ", ""))
    if Choice == "список":
        list = Address_book.print_all_dict()
        if list == "Пусто":
            print("Пусто")
        else:
            for dict in list:
                for value in dict:
                    print(value,":",dict[value])
    elif Choice == "найти":
        print("Адрес: "+Address_book.return_address(input("Имя: ")))
    elif Choice == "добавить":
        Address_book.create_data(input("Имя: "), input("Адрес: "))
    elif Choice == "удалить":
        print(Address_book.delete_dict(input("Что: ")))
    elif Choice == "удалитьвсе" or Choice == "удалитьвсё":
        print(Address_book.delete_all_dict())
    elif Choice == "помощь":
        print("""Команды:
    'список' - Показать список имя:адрес
    'добавить' - добавить имя:адрес в список
    'удалить' - удалить имя:адрес из списка
    'удалить все' - удалить весь список
    'выход' - выйти из программы""")
    elif Choice == "выход":
        continue
    else:
        print("Введите 'помощь', что бы посмотреть список команд")
