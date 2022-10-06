# Условие задачи https://stepik.org/lesson/701986/step/5?unit=702087

class Shop:

    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    __UID = 0

    def __new__(cls, *args, **kw):
        cls.__UID += 1
        return super().__new__(cls)

    def __init__(self, name, weight, price):
        self.id = self.__UID
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if (key == 'id' and (not isinstance(value, int) or value < 1)
                or key == 'name' and not isinstance(value, str)
                or key in ('weight', 'price') and (not isinstance(value, (int, float)) or value < 0)):
            raise TypeError('Неверный тип присваиваемых данных.')
        super().__setattr__(key, value)

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError('Атрибут id удалять запрещено.')
        super.__delattr__(self, item)
