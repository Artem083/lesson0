# Домашнее задание по теме "Режимы открытия файлов"

class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        prods_str = str(f"{self.name}, {self.weight}, {self.category}")
        return prods_str


class Shop:
    def __init__(self):
        self.__file_name = open('products.txt', 'a')
        self.__file_name.close()
    # Метод считывает всю информацию из файла __file_name,
    # закрывает его и возвращает единую строку со всеми товарами
    # из файла __file_name
    def get_products(self):
        # обращение к чтению файла products.txt (self.__file_name)
        get_file = open('products.txt', 'r')
        name_prod = get_file.read()
        get_file.close()
        # возвращение работы метода self.get_products()
        return name_prod
    # метод принимает неограниченное количество объектов класса Product и
    # добавляет отсутствующие в файл products.txt (self.__file_name)
    def add(self, *products):
        # цикл перебора наименований product в products
        for product in products:
            # условие проверки когда строки product нет в списке products.txt
            if str(product) not in self.get_products():
                # добавление отсутствующего product в файл products.txt
                file = open('products.txt', 'a+')
                file.write(f'{str(product)}\n')
                file.close()
            # когда запись product есть в файле products.txt
            else:
                print(f'Продукт {product} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)

s1.add(p1, p2, p3)
print(s1.get_products())