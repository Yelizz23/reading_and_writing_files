from pprint import pprint
import os


class CookBook:
    def __init__(self):
        self.cook_book = None
        self.shop_list = None

    def get_cook_book(self, path):
        self.cook_book = {}
        with open(path, 'rt', encoding='utf-8') as file:
            for dish in file:
                counter = int(file.readline().strip())
                tempor_data = []
                for item in range(counter):
                    name, quantity, measure = file.readline().split('|')
                    tempor_data.append(
                        {'ingredient_name': name.strip(), 'quantity': int(quantity.strip()), 'measure': measure.strip()}
                    )
                self.cook_book[dish.strip()] = tempor_data
                file.readline()

    def get_shop_list_by_dishes(self, dishes, person_count):
        if not self.cook_book:
            return 'Кулинарная книга не создана!'
        self.shop_list = {}
        for dish in dishes:
            if dish not in self.cook_book.keys():
                return 'Такого блюда не существует! Выберите другое блюдо.'
            for item in self.cook_book[dish]:
                if item['ingredient_name'] not in self.shop_list.keys():
                    self.shop_list[item['ingredient_name']] = {'measure': item['measure'],
                                                               'quantity': item['quantity'] * person_count}
                else:
                    self.shop_list[item['ingredient_name']]['quantity'] += item['quantity'] * person_count


cook_book = CookBook()
cook_book.get_cook_book(os.path.join(os.getcwd(), 'recipes.txt'))
pprint(cook_book.cook_book)

cook_book.get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
pprint(cook_book.shop_list)
