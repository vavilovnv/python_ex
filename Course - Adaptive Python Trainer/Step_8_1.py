# Текст задания: https://stepik.org/lesson/22243/step/1?adaptive=true&unit=5316

# Напишите простой интерпретатор математического выражения.
# На вход подаётся строка с выражением, состоящим из двух чисел, объединённых бинарным оператором: a operator b, где
# вместо operator могут использоваться следующие слова: plus, minus, multiply, divide для, соответственно, сложения,
# вычитания, умножения и целочисленного деления.
# Формат ввода:
# Одна строка, содержащая выражение вида a operator b, 0 ≤ a,b ≤ 1000. Оператор может быть plus, minus, multiply,
# divide.
# Формат вывода:
# Строка, содержащая целое число -− результат вычисления.

d = input().split()
if d[1] == "plus":
    print(int(d[0]) + int(d[2]))
elif d[1] == "minus":
    print(int(d[0]) - int(d[2]))
elif d[1] == "multiply":
    print(int(d[0]) * int(d[2]))
elif d[1] == "divide":
    print(int(d[0]) // int(d[2]))


