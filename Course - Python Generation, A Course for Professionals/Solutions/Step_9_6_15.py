# Условие задачи https://stepik.org/lesson/655394/step/15?unit=652334

"""
Реализуйте функцию top_grade() c использованием аннотаций типов, которая
принимает один аргумент:

grades — словарь, содержащий данные об ученике, а именно имя по ключу name и
список оценок по ключу grades

Функция должна возвращать словарь, содержащий имя ученика по ключу name и его
самую высокую оценку по ключу top_grade.

Примечание 1. Используйте встроенные типы (list, tuple, ...), а не типы из
модуля typing. Также используйте нотацию |, а не тип Union из модуля typing.

Примечание 2. В возвращаемом функцией словаре сначала должно следовать имя, а
затем — самая высокая оценка.
"""

def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
    return {'name': grades['name'], 'top_grade': max(grades['grades'])}
