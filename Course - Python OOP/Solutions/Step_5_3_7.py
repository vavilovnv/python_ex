# Условие задачи https://stepik.org/lesson/702004/step/7?unit=702105

class TupleLimit(tuple):

    def __new__(cls, lst, max_length, *args, **kwargs):
        if len(lst) > max_length:
            raise ValueError('число элементов коллекции превышает заданный предел')
        return super(TupleLimit, cls).__new__(cls, lst)

    def __repr__(self):
        return ' '.join([str(float(i)) for i in self])


digits = list(map(float, input().split()))
try:
    tl = TupleLimit(digits, 5)
    print(tl)
except ValueError as error:
    print(error)
