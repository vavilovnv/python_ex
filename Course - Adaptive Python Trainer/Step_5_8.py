# Текст задания: https://stepik.org/lesson/21972/step/1?adaptive=true&unit=5232

# Кривая Коха -- это простой геометрический фрактал.
# Строится этот фрактал следующим образом: берётся отрезок, разделяется на три равных части. Вместо средней части
# вставляется два таких же отрезка, поставленные под углом 60 градусов друг к другу (см. иллюстрацию, переход от n=0 к
# n=1).
# Этот процесс повторяется на каждой итерации: каждый отрезок заменяется четырьмя.
# Напишите программу, которая принимает на вход число n − количество итераций генерации кривой и выводит
# последовательность углов поворота при рисовании соответствующей линии от начальной точки к конечной, без отрыва пера.
# Способ проверки своего решения приведён на следующем степе.
# Формат ввода:
# Строка с целым числом n, 1 ≤ n ≤ 10.
# Формат вывода:
# Строки, содержащие последовательность поворотов. Каждый поворот указывается на отдельной строке как слово "turn" и
# угол поворота в градусах. Угол поворота должен находиться в интервале [-180; 180].

def koch(n):
    return [60, -120, 60] if n == 1 else [*koch(n - 1), 60, *koch(n - 1), -120, *koch(n - 1), 60, *koch(n - 1)]

for i in koch(int(input())):
    print("turn", i)

# визуализация при помощи библиотеки turtle
# документация по библиотеке http://www.239.ru/sites/default/files/userdata/funkcii_turtle.pdf

# import turtle
#
# def koch_turns(n):
#     if n == 1:
#         return [60, -120, 60]
#     else:
#         step = koch_turns(n - 1)
#         return [*step, 60, *step, -120, *step, 60, *step]
#
# def turtle_koch_curve(n, line_length):
#     import turtle
#
#     turtle.speed(10)
#     sw = 1800  # ширина окна в пикселах
#     sh = sw // 2  # высота окна
#     turtle.setup(sw, sh)  # настройка размера окна
#     turtle.up()
#     turtle.setpos(-sw // 2, -sh // 3)  # устанавливаем начальную позицию
#     turtle.down()
#
#     line_length = sw * 3 // 10
#     for _ in range(n - 1):
#         line_length /= 3
#
#     for move in koch_turns(n):
#         turtle.forward(line_length)
#         turtle.left(move)
#     turtle.forward(line_length)
#     turtle.mainloop()
#
# turtle_koch_curve(int(input()),10)