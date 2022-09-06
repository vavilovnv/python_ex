# Условие задачи https://stepik.org/lesson/701989/step/11?unit=702090

class MaxPooling:

    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    @staticmethod
    def check_matrix(matrix):
        if not isinstance(matrix, list) or len(matrix) == 0:
            return False
        if not all([len(row) == len(matrix[0]) for row in matrix]):
            return False
        if not all([all([isinstance(value, (int, float)) for value in row]) for row in matrix]):
            return False
        return True

    def __call__(self, matrix):
        if not self.check_matrix(matrix):
            raise ValueError('Неверный формат для первого параметра matrix.')
        n, m = len(matrix) - (len(matrix) % self.size[0]), len(matrix[0]) - (len(matrix[0]) % self.size[1])
        new_matrix = [[0] * (m // self.step[0]) for _ in range(n // self.step[1])]
        for i in range(0, n-1, self.step[1]):
            for j in range(0, m-1, self.step[0]):
                window_matrix = [[matrix[x][y] for y in range(j, j + self.size[0])] for x in range(i, i + self.size[1])]
                new_matrix[i//self.step[1]][j//self.step[0]] = max([max(row) for row in window_matrix])
        return new_matrix
