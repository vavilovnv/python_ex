# Условие задачи https://stepik.org/lesson/701986/step/11?unit=702087

import time


class Filter:

    def __init__(self, date=0):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and isinstance(value, float) and 'date' not in self.__dict__:
            super().__setattr__(key, value)


class Mechanical(Filter):
    pass


class Aragon(Filter):
    pass


class Calcium(Filter):
    pass


class GeyserClassic:

    MAX_DATE_FILTER = 100
    FILTER_TYPES = {1: Mechanical, 2: Aragon, 3: Calcium}

    def __init__(self):
        self.slots = [None] * 3

    def add_filter(self, slot_num, filter):
        if (self.FILTER_TYPES[slot_num] == type(filter)
                and self.slots[slot_num - 1] is None):
            self.slots[slot_num - 1] = filter

    def remove_filter(self, slot_num):
        self.slots[slot_num - 1] = None

    def get_filters(self):
        return tuple(self.slots)

    def water_on(self):
        return (all(self.slots)
                and all([time.time() - t.date <= self.MAX_DATE_FILTER for t in self.slots]))
