# Текст задания: https://stepik.org/lesson/298796/step/3?unit=280623

# На вход программе подается два натуральных числа a и b (a < b). Напишите программу, которая находит натуральное число
# из отрезка [a, b] с максимальной суммой делителей.
#
# Формат входных данных
# На вход программе подаются два числа, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести два числа на одной строке, разделенных пробелом: число с максимальной суммой делителей и
# сумму его делителей.
#
# Примечание. Если таких чисел несколько, то выведите наибольшее из них.

n1, n2 = int(input()), int(input())
n_max, s_max = n1, 0
for i in range(n1, n2 + 1):
    s = 0
    for j in range(1, i + 1):
        if i % j == 0:
            s += j
    if s >= s_max:
        n_max, s_max = i, s
print(n_max, s_max)
