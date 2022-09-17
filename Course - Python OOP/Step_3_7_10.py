# Условие задачи https://stepik.org/lesson/701992/step/10?unit=702093

class Vector:

    def __init__(self, *args):
        self.coords = [x for x in args]

    def __len__(self):
        return len(self.coords)

    @staticmethod
    def check_size(obj1, obj2):
        if len(obj1) != len(obj2):
            raise ArithmeticError('размерности векторов не совпадают')

    def __eq__(self, other):
        self.check_size(self, other)
        return all([self.coords[i] == other.coords[i] for i in range(len(self))])

    def __add__(self, other):
        self.check_size(self, other)
        lst = [self.coords[i] + other.coords[i] for i in range(len(self))]
        return Vector(*lst)

    def __iadd__(self, other):
        if isinstance(other, Vector):
            self.check_size(self, other)
            for i in range(len(self)):
                self.coords[i] += other.coords[i]
        else:
            for i in range(len(self)):
                self.coords[i] += other
        return self

    def __sub__(self, other):
        self.check_size(self, other)
        lst = [self.coords[i] - other.coords[i] for i in range(len(self))]
        return Vector(*lst)

    def __isub__(self, other):
        if isinstance(other, Vector):
            self.check_size(self, other)
            for i in range(len(self)):
                self.coords[i] -= other.coords[i]
        else:
            for i in range(len(self)):
                self.coords[i] -= other
        return self

    def __mul__(self, other):
        self.check_size(self, other)
        lst = [self.coords[i] * other.coords[i] for i in range(len(self))]
        return Vector(*lst)
