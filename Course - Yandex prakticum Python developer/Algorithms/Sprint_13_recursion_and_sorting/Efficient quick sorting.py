"""
Эффективная быстрая сортировка.

Тимофей решил организовать соревнование по спортивному программированию, чтобы
найти талантливых стажёров. Задачи подобраны, участники зарегистрированы,
тесты написаны. Осталось придумать, как в конце соревнования будет
определяться победитель.

Каждый участник имеет уникальный логин. Когда соревнование закончится, к нему
будут привязаны два показателя: количество решённых задач Pi и размер штрафа
Fi. Штраф начисляется за неудачные попытки и время, затраченное на задачу.

Тимофей решил сортировать таблицу результатов следующим образом: при сравнении
двух участников выше будет идти тот, у которого решено больше задач. При
равенстве числа решённых задач первым идёт участник с меньшим штрафом. Если же
и штрафы совпадают, то первым будет тот, у которого логин идёт раньше в
алфавитном (лексикографическом) порядке.

Тимофей заказал толстовки для победителей и накануне поехал за ними в магазин.
В своё отсутствие он поручил вам реализовать алгоритм быстрой сортировки
(англ. quick sort) для таблицы результатов. Так как Тимофей любит спортивное
программирование и не любит зря расходовать оперативную память, то ваша
реализация сортировки не может потреблять O(n) дополнительной памяти для
промежуточных данных (такая модификация быстрой сортировки называется
"in-place").

Как работает in-place quick sort
Как и в случае обычной быстрой сортировки, которая использует дополнительную
память, необходимо выбрать опорный элемент (англ. pivot), а затем
переупорядочить массив. Сделаем так, чтобы сначала шли элементы, не
превосходящие опорного, а затем —– большие опорного.

Затем сортировка вызывается рекурсивно для двух полученных частей. Именно на
этапе разделения элементов на группы в обычном алгоритме используется
дополнительная память. Теперь разберёмся, как реализовать этот шаг in-place.

Пусть мы как-то выбрали опорный элемент. Заведём два указателя left и right,
которые изначально будут указывать на левый и правый концы отрезка
соответственно. Затем будем двигать левый указатель вправо до тех пор, пока он
указывает на элемент, меньший опорного. Аналогично двигаем правый указатель
влево, пока он стоит на элементе, превосходящем опорный. В итоге окажется, что
что левее от left все элементы точно принадлежат первой группе, а правее от
right — второй. Элементы, на которых стоят указатели, нарушают порядок.
Поменяем их местами (в большинстве языков программирования используется
функция swap()) и продвинем указатели на следующие элементы. Будем повторять
это действие до тех пор, пока left и right не столкнутся.
На рисунке представлен пример разделения при pivot=5. Указатель left —
голубой, right — оранжевый.

Формат ввода
В первой строке задано число участников n, 1 ≤ n ≤ 100 000.
В каждой из следующих n строк задана информация про одного из участников.
i-й участник описывается тремя параметрами:
уникальным логином (строкой из маленьких латинских букв длиной не более 20)
числом решённых задач Pi
штрафом Fi

Fi и Pi — целые числа, лежащие в диапазоне от 0 до 10^9.

Формат вывода
Для отсортированного списка участников выведите по порядку их логины по одному
в строке.

Пример 1
Ввод
5
alla 4 100
gena 6 1000
gosha 2 90
rita 2 90
timofey 4 80
Вывод
gena
timofey
alla
gosha
rita

Пример 2
Ввод
5
alla 0 0
gena 0 0
gosha 0 0
rita 0 0
timofey 0 0
Вывод
alla
gena
gosha
rita
timofey
"""

from random import randint
from typing import List, Tuple


def gt(intern1: Tuple[str, int], intern2: Tuple[str, int]) -> bool:
    """Функция great then выполняет сравнение результатов двух стажеров по
    количеству решенных задач. Если у них одинаковое количество решенных
    задач, то проверяется, у кого меньше штрафное время. Если и оно одинаково,
    побеждает стажер у которого имя идет раньше в алфавитном порядке."""

    name1, tasks1, penalty1 = intern1  # результаты первого стажера
    name2, tasks2, penalty2 = intern2  # результаты второго стажера
    if tasks1 == tasks2:
        if penalty1 == penalty2:
            return name1 < name2
        return penalty1 < penalty2
    return tasks1 > tasks2


def quicksort(arr: List[tuple], left: int, right: int) -> List[tuple]:
    """Функция при помощи рекурсии выполняет быструю сортировку списка
    in-place."""

    if left >= right:  # базовый случай рекурсии
        return arr
    pivot = arr[randint(left, right)]  # выбор случайного элемента
    prev_left, prev_right = left, right  # сохранение границ выборки
    while left < right:
        # сравнение левых элементов с опорным и сдвиг указателя вправо
        while gt(arr[left], pivot) and left <= prev_right:
            left += 1
        # сравнение правых элементов с опорным и сдвиг указателя влево
        while not gt(arr[right], pivot) and right >= prev_left:
            right -= 1
        if left < right:
            # свап элементов нарушающих порядок последовательности
            arr[left], arr[right] = arr[right], arr[left]
            # сдвиг левого указателя вправо, правого - влево
            left += 1
            right -= 1
    # сортировка левой и правой части последовательности
    quicksort(arr, prev_left, right)  # от исх. левого до правого указателя
    quicksort(arr, left, prev_right)  # от левого к исх. правому указателю


if __name__ == '__main__':
    n, interns = int(input()), []
    for _ in range(n):
        name, tasks, penalty = input().split()
        interns.append((name, int(tasks), int(penalty)))
    quicksort(interns, 0, n - 1)
    print(*[intern[0] for intern in interns], sep='\n')
