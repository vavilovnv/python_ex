# Условие задачи https://stepik.org/lesson/701993/step/5?auth=login&unit=702094

class Array:

    def __init__(self, max_length, cell):
        self.max_length = max_length
        if cell in (Integer, ):
            self.lst = [cell.INIT_VALUE] * max_length
        else:
            self.lst = []

    @staticmethod
    def check_index(idx, max_length):
        if not (isinstance(idx, int) and 0 <= idx < max_length):
            raise IndexError('неверный индекс для доступа к элементам массива')

    @staticmethod
    def check_value(value):
        if not isinstance(value, int):
            raise ValueError('должно быть целое число')

    def __getitem__(self, idx):
        self.check_index(idx, self.max_length)
        return self.lst[idx]

    def __setitem__(self, idx, value):
        self.check_index(idx, self.max_length)
        self.check_value(value)
        self.lst[idx] = value

    def __str__(self):
        return ' '.join(list(map(str, self.lst)))


class Integer:

    INIT_VALUE = 0

    def __init__(self, start_value):
        self.__value = start_value

    @staticmethod
    def check_value(value):
        if not isinstance(value, int):
            raise ValueError('должно быть целое число')

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.check_value(value)
        self.__value = value
