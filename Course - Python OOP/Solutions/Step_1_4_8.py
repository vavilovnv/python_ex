# Условие задачи https://stepik.org/lesson/701974/step/8?unit=702075

import sys


class StreamData:
    def create(self, fields, lst_values):
        if len(fields) != len(lst_values):
            return False
        else:
            try:
                for i in range(len(fields)):
                    setattr(self, fields[i], lst_values[i])
            except:
                return False
            return True


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()
