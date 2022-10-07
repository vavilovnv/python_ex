# Условие задачи https://stepik.org/lesson/701993/step/11?auth=login&unit=702094

class Cell:

    def __init__(self, value):
        self.value = value


class SparseTable:

    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.data = {}

    def update_cols_and_rows(self):
        self.rows = max(self.data.keys(), key=lambda x: x[0])[0] + 1
        self.cols = max(self.data.keys(), key=lambda x: x[1])[1] + 1

    def add_data(self, row, col, data):
        self.data[(row, col)] = data
        self.update_cols_and_rows()

    def remove_data(self, row, col):
        if self.data.get((row, col)) is None:
            raise IndexError('ячейка с указанными индексами не существует')
        self.data.pop((row, col))
        self.update_cols_and_rows()

    def check_index(self, idx):
        if idx not in self.data.keys():
            raise ValueError('данные по указанным индексам отсутствуют')

    def __getitem__(self, idx):
        self.check_index(idx)
        return self.data[idx]

    def __setitem__(self, idx, value):
        self.add_data(*idx, value)
