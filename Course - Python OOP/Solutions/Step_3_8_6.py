# Условие задачи https://stepik.org/lesson/701993/step/6?auth=login&unit=702094

class Value:

    VALUE_TYPE = None

    @classmethod
    def check_value(cls, value):
        if cls.VALUE_TYPE is int and not isinstance(value, int):
            raise ValueError('возможны только целочисленные значения')
        if cls.VALUE_TYPE is str and not isinstance(value, str):
            raise ValueError('возможны только строковые значения')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.check_value(value)
        setattr(instance, self.name, value)


class IntegerValue(Value):

    VALUE_TYPE = int


class StringValue(Value):

    VALUE_TYPE = str


class CellInteger:

    value = IntegerValue()

    def __init__(self, start_value=0):
        self.value = start_value


class CellString:

    value = StringValue()

    def __init__(self, start_value=''):
        self.value = start_value


class TableValues:

    def __init__(self, rows, cols, cell):
        self.rows = rows
        self.cols = cols
        if cell is None:
            raise ValueError('параметр cell не указан')
        elif cell is CellInteger:
            self.cells = tuple(tuple(CellInteger() for _ in range(cols)) for _ in range(rows))
        elif cell is CellString:
            self.cells = tuple(tuple(CellString() for _ in range(cols)) for _ in range(rows))

    def __getitem__(self, idx):
        col, row = idx
        return self.cells[col][row].value

    def __setitem__(self, idx, value):
        col, row = idx
        self.cells[col][row].value = value