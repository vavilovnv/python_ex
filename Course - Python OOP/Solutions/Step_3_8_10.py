# Условие задачи https://stepik.org/lesson/701993/step/10?auth=login&unit=702094

class Thing:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Bag:

    def __init__(self, max_weight):
        self.__items = []
        self.max_weight = max_weight
        self.__curr_weight = 0

    def __check_index(self, idx):
        if not (isinstance(idx, int) and 0 <= idx < len(self.__items)):
            raise IndexError('неверный индекс')

    def __check_weight(self, curr_weight, add_weight):
        if curr_weight + add_weight > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')

    def add_thing(self, thing):
        self.__check_weight(self.__curr_weight, thing.weight)
        self.__items.append(thing)
        self.__curr_weight += thing.weight

    def __getitem__(self, idx):
        self.__check_index(idx)
        return self.__items[idx]

    def __setitem__(self, idx, value):
        self.__check_index(idx)
        self.__check_weight(self.__curr_weight - self.__items[idx].weight, value.weight)
        self.__curr_weight -= self.__items[idx].weight
        self.__items[idx] = value
        self.__curr_weight += value.weight

    def __delitem__(self, idx):
        self.__check_index(idx)
        self.__curr_weight -= self.__items[idx].weight
        del self.__items[idx]
