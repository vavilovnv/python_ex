# Условие задачи https://stepik.org/lesson/702003/step/9?unit=702104

class Rect:
    def __init__(self, x, y, width, height):
        self._x, self._y = x, y
        self._width, self._height = width, height

    def __setattr__(self, name, value):
        if name in ('_x', '_y') and not isinstance(value, (int, float)):
            raise ValueError('некорректные координаты и параметры прямоугольника')
        if (name in ('_width', '_height')
                and not (isinstance(value, (int, float)) and value > 0)):
            raise ValueError('некорректные координаты и параметры прямоугольника')
        super().__setattr__(name, value)

    def is_collision(self, rect):
        if ((self._x <= rect._x <= self._x + self._width
                or rect._x <= self._x <= rect._x + rect._width)
            and (self._y - self._height <= rect._y <= self._y
                 or rect._y - rect._height <= self._y <= rect._y)):
            raise TypeError('прямоугольники пересекаются')


lst_not_collision = []
lst_rect = [Rect(0, 0, 5, 3), Rect(6, 0, 3, 5), Rect(3, 2, 4, 4), Rect(0, 8, 8, 1)]
for rect1 in lst_rect:
    try:
        for rect2 in lst_rect:
            if rect1 != rect2:
                rect1.is_collision(rect2)
    except TypeError:
        pass
    else:
        lst_not_collision.append(rect2)
