# Текст задания: https://stepik.org/lesson/298796/step/2?unit=280623

# Дано натуральное число n. Напишите программу, которая печатает численный треугольник с высотой равной n, в
# соответствии с примером:
#
# 1
# 121
# 12321
# 1234321
# 123454321
# ...
# Формат входных данных
# На вход программе подается одно натуральное число.
#
# Формат выходных данных
# Программа должна вывести треугольник в соответствии с условием.
#
# Примечание. Используйте вложенный цикл for.

for i in range(int(input())):
    for j in range(i * 2 + 1):
        print(i - abs(i - j) + 1, end='')
    print()
