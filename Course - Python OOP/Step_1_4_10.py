# Условие задачи https://stepik.org/lesson/701974/step/10?unit=702075

import sys


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        for s in data:
            self.lst_data.append({c: v for c, v in zip(self.FIELDS, s.split())})

    def select(self, a, b):
        return self.lst_data[a:min(b, len(self.lst_data))+1]


db = DataBase()
lst_in = list(map(str.strip, sys.stdin.readlines()))
db.insert(lst_in)
