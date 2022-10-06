# Условие задачи https://stepik.org/lesson/701986/step/4?unit=702087

class Book:

    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if (key in ('title', 'author') and not isinstance(value, str)
                or key in ('pages', 'year') and not isinstance(value, int)):
            raise TypeError('Неверный тип присваиваемых данных.')
        super().__setattr__(key, value)


book = Book('Python ООП', 'Сергей Балакирев', 123, 2022)
