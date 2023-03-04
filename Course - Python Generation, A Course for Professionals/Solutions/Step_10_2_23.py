# Условие задачи https://stepik.org/lesson/640044/step/23?unit=636564

"""
Реализуйте функцию get_min_max(), которая принимает один аргумент:

iterable — итерируемый объект, элементы которого сравнимы между собой
Функция должна возвращать кортеж, в котором первым элементом является
минимальный элемент итерируемого объекта iterable, вторым — максимальный
элемент итерируемого объекта iterable. Если итерируемый объект iterable пуст,
функция должна вернуть значение None.
"""

from copy import copy


def get_min_max(iterable):
    iterable_copy = copy(iterable)
    try:
        return min(iterable), max(iterable_copy)
    except Exception:
        return None
