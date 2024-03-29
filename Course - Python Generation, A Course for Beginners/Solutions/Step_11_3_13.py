# Текст задания: https://stepik.org/lesson/327207/step/13?unit=310501

# На вход программе подается натуральное число n и n строк, а затем число k. Напишите программу, которая выводит k-ую
# букву из введенных строк на одной строке без пробелов.
#
# Формат входных данных
# На вход программе подается натуральное число n, далее n строк, каждая на отдельной строке. В конце вводится
# натуральное число k – номер буквы (нумерация начинается с единицы).
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Примечание. Если некоторые строки слишком короткие, и в них нет символа с заданным номером, то такие строки при выводе
# нужно игнорировать.

lst = [input() for i in range(int(input()))]
k = int(input())
for w in lst:
    print(w[k - 1:k], end='')
