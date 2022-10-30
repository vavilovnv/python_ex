# Условие задачи https://stepik.org/lesson/701999/step/10?unit=702100

class PointTrack:

    def __init__(self, x, y):
        self.x = self.check_value(x)
        self.y = self.check_value(y)

    def check_value(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('координаты должны быть числами')
        return value

    def __str__(self):
        return f'PointTrack: {self.x}, {self.y}'


class Track:

    def __init__(self, *args):
        self.__points = list(args)

    def __setattr__(self, name, value):
        if isinstance(value[0], PointTrack):
            super().__setattr__(name, value)
        else:
            super().__setattr__(name, [PointTrack(value[0], value[1])])

    @property
    def points(self):
        return tuple(self.__points)

    def add_back(self, pt):
        self.__points.append(pt)

    def add_front(self, pt):
        self.__points.insert(0, pt)

    def pop_back(self):
        self.__points.pop()

    def pop_front(self):
        self.__points.pop(0)
