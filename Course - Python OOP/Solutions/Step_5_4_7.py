# Условие задачи https://stepik.org/lesson/702005/step/7?unit=702106

from datetime import datetime


class DateError(Exception):
    pass


class DateString:

    def __init__(self, date_string):
        try:
            self.date = datetime.strptime(date_string, '%d.%m.%Y').strftime('%d.%m.%Y')
        except ValueError:
            raise DateError

    def __str__(self):
        return self.date


date_string = input()
try:
    print(DateString(date_string))
except DateError:
    print("Неверный формат даты")