# Текст задания: https://stepik.org/lesson/3372/step/9?unit=955

# Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения,
# а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного списка.
# Функция не должна осуществлять ввод/вывод информации.

def modify_list(my_list):

    for i in range(len(my_list)-1, -1, -1):
        if my_list[i] % 2 == 0:
            my_list[i] = int(my_list[i]/2)
        else:
            my_list.remove(my_list[i])


my_list = [10, 5, 8, 3]
modify_list(my_list)
print(*my_list)
