# Текст задания: https://stepik.org/lesson/265110/step/7?unit=246058

# Даны три вещественных числа a, b, c. Напишите программу, которая находит вещественные корни квадратного уравнения
# ax^2 + bx + c = 0.
# Формат входных данных
# На вход программе подается три вещественных числа a !=0,b,c, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести вещественные корни уравнения если они существуют или текст «Нет корней» в противном случае.
#
# Примечание. Если уравнение имеет два корня, то следует вывести их в порядке возрастания.

from math import pow, sqrt

a, b, c = (float(input()) for i in range(3))
d = pow(b, 2) - 4 * a * c
if d > 0:
    x1, x2 = (-b - sqrt(pow(b, 2) - 4 * a * c)) / (2 * a), (-b + sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)
    print(min(x1, x2), max(x1, x2), sep='\n')
else:
    print(-b / (2 * a) if d == 0 else 'Нет корней')
