"""
Ловкость рук.

Игра «Тренажёр для скоростной печати» представляет собой поле из клавиш 4x4. В
нём на каждом раунде появляется конфигурация цифр и точек. На клавише написана
либо точка, либо цифра от 1 до 9.
В момент времени t игрок должен одновременно нажать на все клавиши, на которых
написана цифра t. Гоша и Тимофей могут нажать в один момент времени на k
клавиш каждый. Если в момент времени t нажаты все нужные клавиши, то игроки
получают 1 балл.
Найдите число баллов, которое смогут заработать Гоша и Тимофей, если будут
нажимать на клавиши вдвоём.

Формат ввода
В первой строке дано целое число k (1 ≤ k ≤ 5).
В четырёх следующих строках задан вид тренажёра –— по 4 символа в каждой
строке. Каждый символ —– либо точка, либо цифра от 1 до 9. Символы одной
строки идут подряд и не разделены пробелами.

Формат вывода
Выведите единственное число – максимальное количество баллов, которое смогут
набрать Гоша и Тимофей.

Пример 1
Ввод
3
1231
2..2
2..2
2..2
Вывод
2

Пример 2
Ввод
4
1111
9999
1111
9911
Вывод
1

Пример 3
Ввод
4
1111
1111
1111
1111
Вывод
0
"""

def calc_points(fingers, data):
    """Функция подсчитывает количество баллов, которые Гоша и Тимофей
    могут получить, если будут нажимать k клавиш с цифрами для
    момента времени t каждый (или 2 * k вместе).

    Для нахождения правильного ответа достаточно для каждого момента
    времени t определить, является ли количество цифр на поле со значением
    t меньше либо равным количеству 2 * k клавиш, которые могут нажать
    ребята. Если да - Гоша и Тимофей получают 1 балл, в противном случае они
    проигрывают и балл не получают."""

    # заполняем список количеством каждой из цифр data от 1 до 9
    numbers = [data.count(str(i)) for i in range(1, 10)]
    # определяем число элементов списка numbers, для каждого из которых
    # количество на поле меньше, либо равно fingers (k * 2)
    points = len([num for num in numbers if 0 < num <= fingers])
    return points


if __name__ == '__main__':
    k = int(input())
    keys = ''.join([input() for i in range(4)])
    answer = calc_points(k * 2, keys)
    print(answer) 
