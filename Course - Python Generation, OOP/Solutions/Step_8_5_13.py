# Условие задачи https://stepik.org/lesson/835206/step/13

"""
Декоратор @singleton

Реализуйте декоратор @singleton для декорирования класса. Декоратор должен
превращать декорируемый класс в синглтон, то есть в класс, при первом вызове
создающий единственный свой экземпляр и при последующих вызовах возвращающий
его же.
"""

import functools

def singleton(cls):
    old_new = cls.__new__
    cls._instance = None

    @functools.wraps(old_new)
    def new_new(cls, *args, **kwargs):
        if not cls._instance:
            old_new(cls)
            cls._instance = object.__new__(cls)
        return cls._instance

    cls.__new__ = new_new
    return cls
