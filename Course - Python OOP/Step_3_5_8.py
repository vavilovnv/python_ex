# Условие задачи https://stepik.org/lesson/701990/step/8?unit=702091

class FileAcceptor:

    def __init__(self, *args):
        self.__exts = [filename.split('.')[-1] for filename in args]

    def __call__(self, filename, *args, **kwargs):
        return filename.split('.')[-1] in self.__exts

    @property
    def exts(self):
        return self.__exts

    def __add__(self, other):
        self.__exts = list(set(self.exts + other.exts))
        return self

    def __iadd__(self, other):
        return self.__add__(other)
