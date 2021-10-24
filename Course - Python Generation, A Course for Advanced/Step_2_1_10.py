# Текст задания: https://stepik.org/lesson/415553/step/10?unit=405082

# Задача Иосифа Флавия
# n человек, пронумерованных числами от 1 до n, стоят в кругу. Они начинают считаться, каждый k-й по счету человек
# выбывает из круга, после чего счет продолжается со следующего за ним человека. Напишите программу, определяющую номер
# человека, который останется в кругу последним.
#
# Формат входных данных
# На вход программе подаются два числа n и k, записанные на отдельных строках.
#
# Формат выходных данных
# Программа должна вывести одно число – номер человека, который останется в кругу последним.

n, k, ind = int(input()), int(input()), 0
people = [i for i in range(1, n + 1)]
while len(people) > 1:
    ind = (ind + k - 1) % len(people)
    people.pop(ind)
print(people[0])
