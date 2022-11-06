# Условие задачи https://stepik.org/lesson/702002/step/10?unit=702103

class Triangle:

    def __init__(self, a, b, c):
        self._a = self.__check_value(a)
        self._b = self.__check_value(b)
        self._c = self.__check_value(c)
        if a + b < c or a + c < b or c + b < a:
            raise ValueError('из указанных длин сторон нельзя составить треугольник')

    def __check_value(self, value):
        if not (isinstance(value, (int, float)) and value > 0):
            raise TypeError('стороны треугольника должны быть положительными числами')
        return value


input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]
lst_tr = []
for i in input_data:
    try:
        triangle = Triangle(*i)
        lst_tr.append(triangle)
    except Exception:
        pass
