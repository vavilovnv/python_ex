# Условие задачи https://stepik.org/lesson/702001/step/9?unit=702102

class Note:

    def __init__(self, name, ton):
        self._name = name
        self._ton = ton

    def __setattr__(self, key, value):
        if (key == '_name' and value not in ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')
                or key == '_ton' and value not in (-1, 0, 1)):
            raise ValueError('недопустимое значение аргумента')
        self.__dict__[key] = value


class Notes:

    __instance = None
    __notes_rus = 'до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си'
    __slots__ = '_do', '_re', '_mi', '_fa', '_solt', '_la', '_si'
    __notes = dict(enumerate(__slots__))

    def __new__(cls, *args, **kwargs):
        cls.__instance = cls.__instance or super().__new__(cls)
        return cls.__instance

    def __init__(self):
        for idx, name in Notes.__notes.items():
            object.__setattr__(self, name, Note(Notes.__notes_rus[idx], 0))

    def __getitem__(self, idx):
        if not (isinstance(idx, int) and 0 <= idx <= 6):
            raise IndexError('недопустимый индекс')
        return getattr(self, Notes.__notes[idx])
