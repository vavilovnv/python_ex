# Условие задачи https://stepik.org/lesson/701994/step/11?unit=702095

class Matrix:

    def __init__(self, *args):
        if len(args) == 3:
            self.rows, self.cols, init_value = args
            if not (isinstance(self.rows, int)
                    and isinstance(self.cols, int)
                    and isinstance(init_value, (int, float))):
                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
            self.lst = [[args[2] for _ in range(self.cols)] for _ in range(self.rows)]
        elif len(args) == 1 and isinstance(args[0], list):
            self.lst = args[0]
            self.rows = len(self.lst)
            self.cols = min([len(row) for row in self.lst])
            if (self.cols != max([len(row) for row in self.lst])
                    or not all([all([isinstance(i, (int, float)) for i in row]) for row in self.lst])):
                raise TypeError('список должен быть прямоугольным, состоящим из чисел')

    def check_index(self, row, col):
        if not (isinstance(row, int)
                and 0 <= row < self.rows
                and isinstance(col, int)
                and 0 <= col < self.cols):
            raise IndexError('недопустимые значения индексов')

    def check_matrix(self, matrix):
        lst = matrix.lst
        rows = len(lst)
        cols_min = min([len(row) for row in lst])
        cols_max = max([len(row) for row in lst])
        if self.rows != rows or self.cols != cols_min or cols_min != cols_max:
            raise ValueError('операции возможны только с матрицами равных размеров')

    def __getitem__(self, idx):
        row, col = idx
        self.check_index(row, col)
        return self.lst[row][col]

    def __setitem__(self, idx, value):
        if not isinstance(value, (int, float)):
            raise TypeError('значения матрицы должны быть числами')
        row, col = idx
        self.check_index(row, col)
        self.lst[row][col] = value

    def __add__(self, other):
        if isinstance(other, int):
            return Matrix([[i + other for i in row] for row in self.lst])
        elif isinstance(other, Matrix):
            self.check_matrix(other)
            lst = [[self.lst[i][j] + other.lst[i][j] for j in range(len(self.lst[i]))] for i in range(len(self.lst))]
            return Matrix(lst)

    def __sub__(self, other):
        if isinstance(other, int):
            return Matrix([[i - other for i in row] for row in self.lst])
        elif isinstance(other, Matrix):
            self.check_matrix(other)
            lst = [[self.lst[i][j] - other.lst[i][j] for j in range(len(self.lst[i]))] for i in range(len(self.lst))]
            return Matrix(lst)
