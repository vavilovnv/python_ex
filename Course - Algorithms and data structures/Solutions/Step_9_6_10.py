# Условие задачи https://stepik.org/lesson/241770/step/10?unit=756053

"""
Пересечение списков
Даны два списка целых чисел A и B, упорядоченных по возрастанию. Сформируйте
новый список C, состоящий из элементов, входящих и в список A и в список B.

Входные данные
В первой строке задается одно натуральное число n, не превосходящее 10^5.
Во второй строке вводятся n целых чисел списка A, каждое из которых по модулю
не превосходит 10^5. Числа отсортированы по возрастанию.
В третьей строке задается одно натуральное число m, не превосходящее 10^5.
В четвертой строке вводятся m целых чисел списка B, каждое из которых по
модулю не превосходит 10^5. Числа отсортированы по возрастанию.

Выходные данные
Программа должна вывести последовательность возрастающих чисел, являющихся
элементами обоих списков.
"""

def main(n, arr):
    res = []
    while arr1 and arr2:
        if arr1[-1] == arr2[-1]:
            res.append(arr1[-1])
            arr1.pop()
            arr2.pop()
        elif arr1[-1] < arr2[-1]:
            arr2.pop()
        else:
            arr1.pop()
    return res[::-1]


if __name__ == '__main__':
    input()
    arr1 = list(map(int, input().split()))
    input()
    arr2 = list(map(int, input().split()))
    print(*main(arr1, arr2))