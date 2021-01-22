# Текст задания: https://stepik.org/lesson/21209/step/2?adaptive=true&unit=5095

# Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения,
# а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного списка,
# например:
# lst = [1, 2, 3, 4, 5, 6]
# print(modify_list(lst))  # None
# print(lst)               # [1, 2, 3]
# modify_list(lst)
# print(lst)               # [1]
#
# lst = [10, 5, 8, 3]
# modify_list(lst)
# print(lst)               # [5, 4]

def modify_list(lst):
    for i in range(len(lst)-1, -1, -1):
        if lst[i] % 2 == 0:
            lst[i] = round(lst[i] / 2)
        else:
            lst.remove(lst[i])

lst = [int(i) for i in input().split()]
print(modify_list(lst))
print(lst)
