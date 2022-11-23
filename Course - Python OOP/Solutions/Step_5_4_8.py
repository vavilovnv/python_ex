# Условие задачи https://stepik.org/lesson/702005/step/8?unit=702106
"""
 Вам поручается разработать класс TupleData, элементами которого могут
 являются только объекты классов: CellInteger, CellFloat и CellString.

Вначале в программе нужно объявить класс CellInteger, CellFloat и CellString,
объекты которых создаются командами:
cell_1 = CellInteger(min_value, max_value)
cell_2 = CellFloat(min_value, max_value)
cell_3 = CellString(min_length, max_length)
где min_value, max_value - минимальное и максимальное допустимое значение в
ячейке; min_length, max_length - минимальная и максимальная допустимая длина
строки в ячейке.

В каждом объекте этих классов должны формироваться локальные атрибуты с
именами _min_value, _max_value или _min_length, _max_length и соответствующими
значениями.

Запись и считывание текущего значения в ячейке должно выполняться через
объект-свойство (property) с именем:
value - для записи и считывания значения в ячейке (изначально возвращает
значение None).

Если в момент записи новое значение не соответствует диапазону [min_value;
max_value] или [min_length; max_length], то генерируется исключения командами:
# для объектов класса CellInteger
raise CellIntegerException('значение выходит за допустимый диапазон')  
# для объектов класса CellFloat
raise CellFloatException('значение выходит за допустимый диапазон')
# для объектов класса CellString
raise CellStringException('длина строки выходит за допустимый диапазон')

Все три класса исключений должны быть унаследованы от одного общего класса:
CellException

Далее, объявите класс TupleData, объекты которого создаются командой:
ld = TupleData(cell_1, ..., cell_N)
где cell_1, ..., cell_N - объекты классов CellInteger, CellFloat и CellString
(в любом порядке и любом количестве).

Обращение к отдельной ячейке должно выполняться с помощью оператора:
value = ld[index] # считывание значения из ячейке с индексом index
ld[index] = value # запись нового значения в ячейку с индексом index
Индекс index отсчитывается с нуля (для первой ячейки) и является целым числом.
Если значение index выходит за диапазон [0; число ячеек-1], то генерировать
исключение IndexError.

Также с объектами класса TupleData должны выполняться следующие функции и
операторы:
 # возвращает общее число элементов (ячеек) в объекте ld
res = len(ld)
# перебирает значения ячеек объекта ld (значения, а не объекты ячеек)
for d in ld:  
    print(d)

Все эти классы в программе можно использовать следующим образом:
ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))

try:
    ld[0] = 1
    ld[1] = 20
    ld[2] = -5.6
    ld[3] = "Python ООП"
except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException:
    print("Ошибка при обращении к ячейке")
except Exception:
    print("Общая ошибка при работе с объектом TupleData")

P.S. Данная программа должна быть выполнена штатно, без ошибок. На экран
отображать ничего не нужно.
"""

class CellException(Exception):
    pass


class CellIntegerException(CellException):
    pass


class CellFloatException(CellException):
    pass


class CellStringException(CellException):
    pass


class CellInteger:

    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not (self._min_value <= value <= self._max_value):
            raise CellIntegerException('значение выходит за допустимый диапазон')
        self._value = value


class CellFloat:

    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not (self._min_value <= value <= self._max_value):
            raise CellFloatException('значение выходит за допустимый диапазон')
        self._value = value


class CellString:

    def __init__(self, min_length, max_length):
        self._min_length = min_length
        self._max_length = max_length
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not (self._min_length <= len(value) <= self._max_length):
            raise CellStringException('длина строки выходит за допустимый диапазон')
        self._value = value


class TupleData:

    def __init__(self, *args):
        self.lst = [obj for obj in args]

    def __len__(self):
        return len(self.lst)

    def _validate_index(self, idx):
        if not (isinstance(idx, int) and 0 <= idx < len(self.lst)):
            raise IndexError

    def __getitem__(self, idx):
        self._validate_index(idx)
        return self.lst[idx].value

    def __setitem__(self, idx, value):
        self._validate_index(idx)
        self.lst[idx].value = value

    def __iter__(self):
        for obj in self.lst:
            yield obj.value


ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))

try:
    ld[0] = 1
    ld[1] = 20
    ld[2] = -5.6
    ld[3] = "Python ООП"
except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException:
    print("Ошибка при обращении к ячейке")
except Exception:
    print("Общая ошибка при работе с объектом TupleData")
