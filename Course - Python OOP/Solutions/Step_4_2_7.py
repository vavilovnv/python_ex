# Условие задачи https://stepik.org/lesson/701996/step/7?unit=702097

class Tuple(tuple):

    def __add__(self, other):
        return Tuple(super(Tuple, self).__add__(tuple(other)))


t = Tuple([1, 2, 3])
t = t + "Python"
print(t)   # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
t = (t + "Python") + "ООП"
print(t)
