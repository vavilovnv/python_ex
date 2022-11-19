# Условие задачи https://stepik.org/lesson/702004/step/6?unit=702105

class Test:

    def __init__(self, descr):
        self.descr = descr

    def __setattr__(self, name, value):
        if name == 'descr' and not (10 <= len(value) <= 100):
            raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')
        super().__setattr__(name, value)

    def run(self):
        raise NotImplementedError


class TestAnsDigit(Test):

    def __init__(self, descr, ans_digit, max_error_digit=0.01):
        super(TestAnsDigit, self).__init__(descr)
        self.ans_digit = ans_digit
        self.max_error_digit = max_error_digit

    def __setattr__(self, name, value):
        if (name in ('ans_digit', 'max_error_digit')
                and not isinstance(value, (int, float))):
            raise ValueError('недопустимые значения аргументов теста')
        if name == 'max_error_digit' and value < 0:
            raise ValueError('недопустимые значения аргументов теста')
        super().__setattr__(name, value)

    def run(self):
        ans = float(input())
        a = self.ans_digit - self.max_error_digit
        b = self.ans_digit + self.max_error_digit
        return a <= ans <= b


descr, ans = map(str.strip, input().split('|'))
ans = float(ans)
try:
    obj = TestAnsDigit(descr, ans)
    print(obj.run())
except ValueError as error:
    print(error)
