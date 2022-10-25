# Условие задачи https://stepik.org/lesson/701997/step/10?unit=702098

class StringDigit(str):

    def __init__(self, string):
        self.check_value(string)

    def check_value(self, value):
        if not value.isdigit():
            raise ValueError("в строке должны быть только цифры")

    def __add__(self, other):
        return StringDigit(super(StringDigit, self).__add__(other))

    def __radd__(self, other):
        return StringDigit(other).__add__(self)
