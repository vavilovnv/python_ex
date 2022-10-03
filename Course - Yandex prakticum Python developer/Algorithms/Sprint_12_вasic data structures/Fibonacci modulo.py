"""
Фибоначчи по модулю.

У Тимофея было очень много стажёров, целых N (0 ≤ N ≤ 106) человек. Каждый
стажёр хотел быть лучше своих предшественников, поэтому i-й стажёр делал 
столько коммитов, сколько делали два предыдущих стажёра в сумме. Два первых
стажёра были менее инициативными — они сделали по одному коммиту.

Пусть Fi — число коммитов, сделанных i-м стажёром (стажёры нумеруются с нуля).
Первые два стажёра сделали по одному коммиту: F0=F1=1. Для всех i≥ 2 выполнено
Fi = F(i-1) + F(i-2).

Определите, сколько кода напишет следующий стажёр –— найдите последние k цифр
числа Fn.

Как найти k последних цифр. Чтобы вычислить k последних цифр некоторого числа
x, достаточно взять остаток от его деления на число 10k. Эта операция
обозначается как x mod 10k. Узнайте, как записывается операция взятия остатка
по модулю в вашем языке программирования.

Также обратите внимание на возможное переполнение целочисленных типов, если в
вашем языке такое случается.

Формат ввода
В первой строке записаны через пробел два целых числа n (0 ≤ n ≤ 106) и 
k (1 ≤ k ≤ 8).

Формат вывода
Выведите единственное число – последние k цифр числа Fn.

Если в искомом числе меньше k цифр, то выведите само число без ведущих нулей.

Пример 1
Ввод
3 1
Вывод
3

Пример 2
Ввод	
10 1
Вывод
9
"""

def factorial(n):
    if n <= 1:
        return 1
    n1, n2, mod = 1, 1, pow(10, k)
    for i in range(n-1):
        n1, n2 = n2, (n1 + n2) % mod
    return n2


n, k = map(int, input().split())
print(factorial(n))
