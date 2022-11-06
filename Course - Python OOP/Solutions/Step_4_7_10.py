# Условие задачи https://stepik.org/lesson/702001/step/10?unit=702102

class Function:
    def __init__(self):
        self._amplitude = 1.0     # амплитуда функции
        self._bias = 0.0          # смещение функции по оси Oy

    def __call__(self, x, *args, **kwargs):
        return self._amplitude * self._get_function(x) + self._bias

    def _get_function(self, x):
        raise NotImplementedError('метод _get_function должен быть переопределен в дочернем классе')

    def __add__(self, other):
        if type(other) not in (int, float):
            raise TypeError('смещение должно быть числом')

        obj = self.__class__(self)
        obj._bias = self._bias + other
        return obj

    def __mul__(self, other):
        if type(other) not in (int, float):
            raise TypeError('смещение должно быть числом')

        obj = self.__class__(self)
        obj._amplitude = self._amplitude * other
        return obj


class Linear(Function):

    def __init__(self, *args, **kwargs):
        super(Linear, self).__init__()
        if isinstance(args[0], Linear):
            self._k, self._b = args[0]._k, args[0]._b
        else:
            self._k, self._b = args[0], args[1]

    def _get_function(self, x):
        return self._k * x + self._b
