# Условие задачи https://stepik.org/lesson/701991/step/7?unit=702092

import sys


class ShopItem:

    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()


lst_in = list(map(str.strip, sys.stdin.readlines()))
shop_items = {}
for line in lst_in:
    lst = [i.strip() for i in line.split(':')]
    weight, price = list(map(float, lst[1].split()))
    obj = ShopItem(lst[0], weight, price)
    if obj not in shop_items:
        shop_items[obj] = [obj, 0]
    shop_items[obj][1] += 1
