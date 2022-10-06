# Условие задачи https://stepik.org/lesson/701988/step/5?unit=702089

class WordString:

    def __init__(self, words=''):
        self.__words = words

    @property
    def string(self):
        return self.__words

    @string.setter
    def string(self, value):
        self.__words = value

    def __len__(self):
        return len(self.string.split())

    def __call__(self, indx, *args, **kwargs):
        lst = self.string.split()
        if len(lst) >= indx:
            return lst[indx]
        return ''
