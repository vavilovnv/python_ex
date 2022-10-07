# Условие задачи https://stepik.org/lesson/701993/step/9?auth=login&unit=702094

class Cell:

    def __init__(self):
        self.is_free = True
        self.value = 0

    def __bool__(self):
        return self.is_free


class TicTacToe:

    def __init__(self):
        self.pole = tuple((Cell(), Cell(), Cell()) for _ in range(3))

    def clear(self):
        for i in range(3):
            for j in range(3):
                self.pole[i][j].value = 0
                self.pole[i][j].is_free = True

    @staticmethod
    def check_index(idx):
        r, c = idx
        if (isinstance(r, int) and 0 > r >= 3
                or isinstance(c, int) and 0 > c >= 3):
            raise IndexError('неверный индекс клетки')

    def __getitem__(self, idx):
        self.check_index(idx)
        r, c = idx
        if isinstance(r, slice):
            return tuple(self.pole[i][c].value for i in range(3))
        if isinstance(c, slice):
            return tuple(self.pole[r][i].value for i in range(3))
        return self.pole[r][c].value

    def __setitem__(self, idx, value):
        self.check_index(idx)
        r, c = idx
        cell = self.pole[r][c]
        if cell:
            cell.value = value
            cell.is_free = False
        else:
            raise ValueError('клетка уже занята')
