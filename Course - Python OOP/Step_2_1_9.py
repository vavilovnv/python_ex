# Условие задачи https://stepik.org/lesson/701983/step/9?unit=702084

class Point:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:

    def __init__(self, *args):
        self.__sp = None
        self.__ep = None
        if len(args) == 2:
            self.set_coords(args[0], args[1])
        else:
            self.set_coords(Point(args[0], args[1]), Point(args[2], args[3]))

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print((f'Прямоугольник с координатами: '
               f'{Point.get_coords(self.__sp)} {Point.get_coords(self.__ep)}'))


rect = Rectangle(0, 0, 20, 34)
