# Условие задачи https://stepik.org/lesson/512854/step/16?unit=505068

# На вход программе на первой строке подаются коэффициенты многочлена,
# разделенные символом пробела и целое число x на второй строке. Напишите
# программу, которая вычисляет значение указанного многочлена при заданном
# значении x.
#
# Программа должна вывести одно число — значение указанного многочлена при
# заданном значении x.Решение задачи необходимо оформить в виде функции
# evaluate(coefficients, x), которая принимает список коэффициентов и значение
# аргумента. Функция evaluate() должна быть реализована на основе встроенных
# функций map() и reduce().

from functools import reduce
from operator import add


def evaluate(coefficients, x):
    data = list(zip(
        coefficients,
        reversed([i for i in range(len(coefficients))])
    ))
    return reduce(add, [i[0] * pow(x, i[1]) for i in data], 0)


if __name__ == '__main__':
    print(evaluate(list(map(int, input().split())), int(input())))
