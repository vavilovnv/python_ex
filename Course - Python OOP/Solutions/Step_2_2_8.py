# Условие задачи https://stepik.org/lesson/701984/step/8?unit=702085

class RadiusVector2D:

    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__is_verify(x):
            self.__x = x
        if self.__is_verify(y):
            self.__y = y

    @classmethod
    def __is_verify(cls, val):
        return (isinstance(val, (int, float))
                and cls.MIN_COORD <= val <= cls.MAX_COORD)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if self.__is_verify(x):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if self.__is_verify(y):
            self.__y = y

    @staticmethod
    def norm2(vector):
        return pow(vector.x, 2) + pow(vector.y, 2)
