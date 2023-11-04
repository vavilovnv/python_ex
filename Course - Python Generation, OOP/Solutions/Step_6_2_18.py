# Условие задачи https://stepik.org/lesson/805785/step/18

"""
Класс MutableString 🌶️

Реализуйте класс MutableString, описывающий изменяемую строку. При создании
экземпляра класс должен принимать один аргумент:
- string — строка, определяющая начальное значение изменяемой строки. Если не
передана, строка считается пустой

Класс MutableString должен иметь два метода экземпляра:
- lower() — метод, переводящий все символы изменяемой строки в нижний регистр
- upper() — метод, переводящий все символы изменяемой строки в верхний регистр

Экземпляр класса MutableString должен иметь неформальное строковое
представление в следующем виде: <текущее значение изменяемой строки>

Также экземпляр класса MutableString должен иметь формальное строковое
представление в следующем виде: MutableString('<текущее значение изменяемой
строки>')

При передаче экземпляра класса MutableString в функцию len() должно
возвращаться количество символов в нем.

Помимо этого, экземпляр класса MutableString должен быть итерируемым объектом,
то есть позволять перебирать свои символы, например, с помощью цикла for.

Также экземпляр класса MutableString должен позволять получать, изменять и
удалять значения своих элементов с помощью индексов, причем как положительных,
так и отрицательных. Экземпляр класса MutableString должен поддерживать
полноценные срезы, результатами которых должны быть новые изменяемые строки.

Наконец, экземпляры класса MutableString должны поддерживать между собой
операцию сложения с помощью оператора +, результатом которой должен являться
новый экземпляр класса MutableString, представляющий конкатенацию исходных.

Примечание 1. Реализация класса MutableString может быть произвольной, то
есть требований к наличию определенных атрибутов нет.

Примечание 2. Дополнительная проверка данных на корректность в методах не
требуется. Гарантируется, что реализованный класс используется только с
корректными данными.
"""

class MutableString:
    def __init__(self, string=""):
        self.string = list(string)

    def __repr__(self):
        return f"MutableString('{''.join(self.string)}')"

    def __str__(self):
        return "".join(self.string)

    def __len__(self):
        return len(self.string)

    def __iter__(self):
        return iter(self.string)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return MutableString("".join(
                self.string[key.start: key.stop: key.step])
            )
        return self.string[key]

    def __setitem__(self, key, value):
        if isinstance(key, slice):
            self.string = list(''.join(self.string))
            self.string[key] = value
            return
        self.string[key] = value

    def __delitem__(self, key):
        del self.string[key]

    def __add__(self, other):
        return MutableString(
            "".join(self.string) + "".join(other.string)
        )

    def lower(self):
        self.string = [i.lower() for i in self.string]

    def upper(self):
        self.string = [i.upper() for i in self.string]
