"""
Два велосипеда.

Вася решил накопить денег на два одинаковых велосипеда — себе и сестре. У Васи
есть копилка, в которую каждый день он может добавлять деньги (если, конечно,
у него есть такая финансовая возможность). В процессе накопления Вася не
вынимает деньги из копилки.

У вас есть информация о росте Васиных накоплений — сколько у Васи в копилке
было денег в каждый из дней.

Ваша задача — по заданной стоимости велосипеда определить первый день, в
которой Вася смог бы купить один велосипед, и первый день, в который Вася смог
бы купить два велосипеда.
Подсказка: решение должно работать за O(log n).

Формат ввода
В первой строке дано число дней n, по которым велись наблюдения за Васиными
накоплениями. 1 ≤ n ≤ 10^6.

В следующей строке записаны n целых неотрицательных чисел. Числа идут в
порядке неубывания. Каждое из чисел не превосходит 10^6.

В третьей строке записано целое положительное число s — стоимость велосипеда.
Это число не превосходит 10^6.

Формат вывода
Нужно вывести два числа — номера дней по условию задачи.

Если необходимой суммы в копилке не нашлось, нужно вернуть -1 вместо номера
дня.

Пример 1
Ввод
6
1 2 4 4 6 8
3
Вывод
3 5

Пример 2
Ввод
6
1 2 4 4 4 4
3
Вывод
3 -1

Пример 3
Ввод
6
1 2 4 4 4 4
10
Вывод
-1 -1
"""

def binary_search(left, right):
    if right == left:
        if money[left] >= cost:
            return left
        else:
            return -2
    mid = (left + right) // 2
    if money[mid] >= cost:
        return binary_search(left, mid)
    else:
        return binary_search(mid + 1, right)


n = int(input())
money = list(map(int, input().split()))
cost = int(input())
indx = binary_search(0, n - 1)
if indx == -2:
    print(-1, -1)
else:
    cost += cost
    print(indx + 1, binary_search(indx, n - 1) + 1)
