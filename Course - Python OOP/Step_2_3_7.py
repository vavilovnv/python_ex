# Условие задачи https://stepik.org/lesson/701985/step/7?unit=702086

class FloatValue:

    @classmethod
    def verify_value(cls, value):
        if not isinstance(value, float):
            raise TypeError('Присваивать можно только вещественный тип данных.')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_value(value)
        setattr(instance, self.name, value)


class Cell:

    value = FloatValue()

    def __init__(self, value):
        self._value = value


class TableSheet:

    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.cells = [[Cell(0.0) for _ in range(self.M)] for _ in range(self.N)]


table = TableSheet(5, 3)
value = iter(range(1, table.N * table.M + 1))
table.cells = [[Cell(next(value)) for _ in range(table.M)] for _ in range(table.N)]
