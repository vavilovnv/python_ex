# Условие задачи https://stepik.org/lesson/701992/step/8?unit=702093

class Ellipse:

    def __init__(self, *args):
        if len(args) != 0:
            self.x1, self.y1 = args[0], args[1]
            self.x2, self.y2 = args[2], args[3]

    def __bool__(self):
        return all([hasattr(self, 'x1'), hasattr(self, 'y1'),
                    hasattr(self, 'x2'), hasattr(self, 'y2')])

    def get_coords(self):
        if self:
            return self.x1, self.y1, self.x2, self.y2
        else:
            raise AttributeError('нет координат для извлечения')


lst_geom = [Ellipse(1, 1, 4, 4), Ellipse(), Ellipse(), Ellipse(3, 3, 7, 7)]
for obj in lst_geom:
    if obj:
        obj.get_coords()
