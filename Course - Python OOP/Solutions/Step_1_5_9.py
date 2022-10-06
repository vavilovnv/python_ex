# Условие задачи https://stepik.org/lesson/701975/step/9?unit=702076

class Goods:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV(Goods):
    pass


class Table(Goods):
    pass


class Notebook(Goods):
    pass


class Cup(Goods):
    pass


class Cart:
    def __init__(self, goods=[]):
        self.goods = goods[:]

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        del self.goods[indx]

    def get_list(self):
        return [f"{i.name}: {i.price}" for i in self.goods]


cart = Cart()
cart.add(TV('Samsung', 50000))
cart.add(TV('Sony', 70000))
cart.add(Table('Столик', 5000))
cart.add(Notebook('Samsung', 75000))
cart.add(Notebook('Sony', 105000))
cart.add(Cup('Кружка', 1000))

