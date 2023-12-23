# Условие задачи https://stepik.org/lesson/864077/step/13

"""
Класс MultiKeyDict 🌶️

Реализуйте класс MultiKeyDict, который практически во всем повторяет класс
dict. Создание экземпляра класса MultiKeyDict должно происходить аналогично
созданию экземпляра класса dict:

multikeydict1 = MultiKeyDict(x=1, y=2, z=3)
multikeydict2 = MultiKeyDict([('x', 1), ('y', 2), ('z', 3)])

print(multikeydict1['x'])        # 1
print(multikeydict2['z'])        # 3
Особенностью класса MultiKeyDict должен являться метод alias(), который
должен позволять давать имеющимся ключам псевдонимы. Обращение по созданному
псевдониму не должно ничем отличаться от обращения по оригинальному ключу, то
есть с момента создания псевдонима у значения становится два ключа (или
больше, если псевдонимов несколько):
multikeydict = MultiKeyDict(x=100, y=[10, 20])

multikeydict.alias('x', 'z')     # добавление ключу 'x' псевдонима 'z'
multikeydict.alias('x', 't')     # добавление ключу 'x' псевдонима 't'
print(multikeydict['z'])         # 100
multikeydict['t'] += 1
print(multikeydict['x'])         # 101

multikeydict.alias('y', 'z')     # теперь 'z' становится псевдонимом ключа 'y'
multikeydict['z'] += [30]
print(multikeydict['y'])         # [10, 20, 30]
Значение должно оставаться доступным по псевдониму даже в том случае, если
оригинальный ключ был удален:

multikeydict = MultiKeyDict(x=100)

multikeydict.alias('x', 'z')
del multikeydict['x']
print(multikeydict['z'])         # 100
Ключи должны иметь приоритет над псевдонимами. Если некоторые ключ и псевдоним
совпадают, то все операции при обращении к ним должны выполняться именно с
ключом:
multikeydict = MultiKeyDict(x=100, y=[10, 20])

multikeydict.alias('x', 'y')
print(multikeydict['y'])         # [10, 20]
"""

from collections import UserDict

class MultiKeyDict(UserDict):

    def __init__(self, *args, **kwargs):
        self._keys = {}
        self._items = {}
        super().__init__(*args, **kwargs)

    def alias(self, key, alias_key):
        self._keys[alias_key] = key
        self._items[alias_key] = self.data[key]

    def __getitem__(self, item):
        if self.data.get(item):
            return self.data[item]
        if self._keys.get(item):
            if self.data.get(self._keys[item]):
                return self.data.get(self._keys[item])
            return self._items[item]
        raise KeyError("Ключ отстутствует")

    def __setitem__(self, key, value):
        if self.data.get(key):
            self.data[key] = value
        elif self._keys.get(key):
            self.data[self._keys[key]] = value
        else:
            super().__setitem__(key, value)
