# Условие задачи https://stepik.org/lesson/793864/step/17

"""
Класс User

Реализуйте класс User, описывающий интернет-пользователя. При создании
экземпляра класс должен принимать два аргумента в следующем порядке:
- name — имя пользователя. Если name не является непустой строкой, состоящей
только из букв, должно быть возбуждено исключение ValueError с текстом:
Некорректное имя
- age — возраст пользователя. Если age не является целым числом, принадлежащим
отрезку [0; 110], должно быть возбуждено исключение ValueError с текстом:
Некорректный возраст

Экземпляр класса User должен иметь два атрибута:
_name — имя пользователя
_age — возраст пользователя

Класс User должен иметь четыре метода экземпляра:
- get_name() — метод, возвращающий имя пользователя
- set_name() — метод, принимающий в качестве аргумента значение new_name и
изменяющий имя пользователя на new_name. Если new_name не является непустой
строкой, состоящей только из букв, должно быть возбуждено исключение
ValueError с текстом: Некорректное имя
- get_age() — метод, возвращающий возраст пользователя
- set_age() — метод, принимающий в качестве аргумента значение new_age и
изменяющий возраст пользователя на new_age. Если new_age не является целым
числом, принадлежащим отрезку [0; 110], должно быть возбуждено исключение
ValueError с текстом: Некорректный возраст

Примечание 1. Если при создании экземпляра класса User имя и возраст
одновременно являются некорректными, должно быть возбуждено исключение,
связанное с именем.
"""

class User:

    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

    def get_name(self) -> str:
        return self._name

    def get_age(self) -> int:
        return self._age

    @staticmethod
    def validate_name(new_name: str) -> None:
        if not (new_name and isinstance(new_name, str) and new_name.isalpha()):
            raise ValueError("Некорректное имя")

    @staticmethod
    def validate_age(new_age: int) -> None:
        if not (isinstance(new_age, int) and 0 <= new_age <= 100):
            raise ValueError("Некорректный возраст")

    def set_name(self, new_name: str) -> None:
        self.validate_name(new_name)
        self._name = new_name

    def set_age(self, new_age: int) -> None:
        self.validate_age(new_age)
        self._age = new_age
