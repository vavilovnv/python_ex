# Условие задачи https://stepik.org/lesson/701994/step/10?unit=702095

class Cell:

    def __init__(self, data):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class TableValues:

    d = {int: 0, float: 0.0, str: '', list: []}

    def __init__(self, rows, cols, type_data=int):
        self.rows = rows
        self.cols = cols
        self.cells = tuple(tuple(Cell(TableValues.d[type_data]) for _ in range(cols)) for _ in range(rows))

    def check_indexes(self, row, col):
        if (not (isinstance(col, int) and 0 <= col < self.cols)
                or not(isinstance(row, int) and 0 <= row < self.rows)):
            raise IndexError('неверный индекс')

    def __getitem__(self, idx):
        row, col = idx
        self.check_indexes(row, col)
        return self.cells[row][col].data

    def __setitem__(self, idx, value):
        row, col = idx
        self.check_indexes(row, col)
        if type(self.cells[row][col].data) != type(value):
            raise TypeError('неверный тип присваиваемых данных')
        self.cells[row][col].data = value

    def __iter__(self):
        for row in self.cells:
            yield (cell.data for cell in row)
