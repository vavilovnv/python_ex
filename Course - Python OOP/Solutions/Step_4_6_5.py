# Условие задачи https://stepik.org/lesson/702000/step/5?unit=702101

class Value:

    def __init__(self, value):
        self.types = int, float
        self.value = self.check_value(value)

    def check_value(self, value):
        if not isinstance(value, self.types):
            raise TypeError('значение не соответствует типу объекта')
        return value


class Digit(Value):
    pass


class Integer(Value):

    def __init__(self, value):
        self.types = int
        self.value = self.check_value(value)


class Float(Value):

    def __init__(self, value):
        self.types = float
        self.value = self.check_value(value)


class Positive(Value):

    def check_value(self, value):
        if value < 0:
            raise TypeError('значение не соответствует типу объекта')
        return super(Positive, self).check_value(value)


class Negative(Value):

    def check_value(self, value):
        if value > 0:
            raise TypeError('значение не соответствует типу объекта')
        return super(Negative, self).check_value(value)


class PrimeNumber(Integer, Positive):
    pass


class FloatPositive(Float, Positive):
    pass


digits = [PrimeNumber(i + 1) for i in range(3)]
digits.extend([FloatPositive(i + 1.0) for i in range(5)])
lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))
