# Условие задачи https://stepik.org/lesson/701987/step/11?unit=702088

class InputValues:

    def __init__(self, render):
        self.render = render

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            return list(map(self.render, func(*args, **kwargs).strip().split()))
        return wrapper


class RenderDigit:

    def __call__(self, string, *args, **kwargs):
        try:
            return int(string)
        except:
            return None


input_dg = InputValues(RenderDigit())(input)
res = input_dg()
print(res)
