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
