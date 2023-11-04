# Условие задачи https://stepik.org/lesson/906773/step/15

"""
Класс ProtectedObject

Будем считать атрибут защищенным, если его имя начинается с символа нижнего
подчеркивания (_). Например, _password, __email и __dict__.

Реализуйте класс ProtectedObject. При создании экземпляра класс должен
принимать произвольное количество именованных аргументов. Все передаваемые
аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов.

Класс ProtectedObject должен запрещать получать и изменять значения защищенных
атрибутов своих экземпляров, а также удалять эти атрибуты. При попытке
получить или изменить значение защищенного атрибута, а также попытке удалить
атрибут, должно возбуждаться исключение AttributeError с текстом:
Доступ к защищенному атрибуту невозможен

Примечание 1. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными
данными.

Примечание 2. Никаких ограничений касательно реализации класса
ProtectedObject нет, она может быть произвольной.
"""

class ProtectedObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __getattribute__(self, name):
        if name.startswith("_") and object.__getattribute__(self, name):
            raise AttributeError("Доступ к защищенному атрибуту невозможен")
        return object.__getattribute__(self, name)

    def __getattr__(self, name):
        if name.startswith("_"):
            raise AttributeError("Доступ к защищенному атрибуту невозможен")
        return "Атрибут отсутствует"

    def __setattr__(self, name, value):
        if name.startswith("_") and self.__dict__.get(name):
            raise AttributeError("Доступ к защищенному атрибуту невозможен")
        object.__setattr__(self, name, value)

    def __delattr__(self, name):
        if name.startswith("_"):
            raise AttributeError("Доступ к защищенному атрибуту невозможен")
        object.__delattr__(self, name)
