# Условие задачи https://stepik.org/lesson/701995/step/11?unit=702096

class Vector:

    def __init__(self, *args):
        self.coords = [x for x in args]

    def __len__(self):
        return len(self.coords)

    @staticmethod
    def check_size(obj1, obj2):
        if len(obj1) != len(obj2):
            raise TypeError('размерности векторов не совпадают')

    def belong_type(self, type_value, values):
        return all([isinstance(x, type_value) for x in values])

    def __add__(self, other):
        self.check_size(self, other)
        lst = [self.coords[i] + other.coords[i] for i in range(len(self))]
        return Vector(*lst)

    def __sub__(self, other):
        self.check_size(self, other)
        lst = [self.coords[i] - other.coords[i] for i in range(len(self))]
        return Vector(*lst)

    def get_coords(self):
        return tuple(self.coords)


class VectorInt(Vector):

    def __init__(self, *args):
        super().__init__(*args)
        if not self.belong_type(int, self.coords):
            raise ValueError('координаты должны быть целыми числами')
        
    def __add__(self, other):
        lst = super(VectorInt, self).__add__(other).coords
        if not self.belong_type(int, other.coords):
            return Vector(*lst)
        return VectorInt(*lst)

    def __sub__(self, other):
        lst = super(VectorInt, self).__sub__(other).coords
        if not self.belong_type(int, other.coords):
            return Vector(*lst)
        return VectorInt(*lst)
