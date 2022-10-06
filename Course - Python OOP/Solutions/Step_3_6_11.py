# Условие задачи https://stepik.org/lesson/701991/step/11?unit=702092

class Side:

    @classmethod
    def check_value(cls, value):
        if not (isinstance(value, (int, float)) and value > 0):
            raise ValueError(
                "длины сторон треугольника должны быть положительными числами"
            )

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name, None)

    def __set__(self, instance, value):
        self.check_value(value)
        setattr(instance, self.name, value)


class Triangle:

    a = Side()
    b = Side()
    c = Side()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def __is_triangle(a, b, c):
        if a and b and c:
            return a < b + c and b < a + c and c < a + b
        return True

    def __setattr__(self, key, value):
        if (key == 'a' and not self.__is_triangle(value, self.b, self.c)
                or key == 'b' and not self.__is_triangle(self.a, value, self.c)
                or key == 'c' and not self.__is_triangle(self.a, self.b, value)):
            raise ValueError("с указанными длинами нельзя образовать треугольник")
        super().__setattr__(key, value)

    def __len__(self):
        return int(self.a + self.b + self.c) if self.a and self.b and self.c else None

    def __call__(self, *args, **kwargs):
        p = self.__len__() * 0.5
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
