# Условие задачи https://stepik.org/lesson/701990/step/5?unit=702091

class InDimensions:

    def __init__(self, min_d, max_d):
        self.min_d = min_d
        self.max_d = max_d

    def check_value(self, value):
        return self.min_d <= value <= self.max_d

    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.check_value(value):
            setattr(instance, self.name, value)


class Dimensions:

    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    a = InDimensions(MIN_DIMENSION, MAX_DIMENSION)
    b = InDimensions(MIN_DIMENSION, MAX_DIMENSION)
    c = InDimensions(MIN_DIMENSION, MAX_DIMENSION)

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_volume(self):
        return self.a * self.b * self.c

    def __gt__(self, other):
        return self.get_volume() > other.get_volume()

    def __ge__(self, other):
        return self.get_volume() >= other.get_volume()


class ShopItem:

    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim

    @property
    def dim_volume(self):
        return self.dim.get_volume()


lst_shop = [
    ShopItem('кеды', 1024, Dimensions(40, 30, 120)),
    ShopItem('зонт', 500.24, Dimensions(10, 20, 50)),
    ShopItem('холодильник', 40000, Dimensions(2000, 600, 500)),
    ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))
]

lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim_volume)
