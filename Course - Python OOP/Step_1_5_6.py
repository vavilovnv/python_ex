# Условие задачи https://stepik.org/lesson/701975/step/6?unit=702076

class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if (any([not (isinstance(self.a, (float, int))),
                 not (isinstance(self.b, (float, int))),
                 not (isinstance(self.c, (float, int)))])
                or any([self.a <= 0, self.b <= 0, self.c <= 0])):
            return 1
        elif any([self.a + self.b < self.c,
                  self.a + self.c < self.b,
                  self.b + self.c < self.a]):
            return 2
        return 3


a, b, c = map(int, input().split())
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
