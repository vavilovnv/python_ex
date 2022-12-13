"""
Печеньки.

К Васе в гости пришли одноклассники. Его мама решила угостить ребят печеньем.

Но не всё так просто. Печенья могут быть разного размера. А у каждого ребёнка
есть фактор жадности —– минимальный размер печенья, которое он возьмёт. Нужно
выяснить, сколько ребят останутся довольными в лучшем случае, когда они
действуют оптимально.

Каждый ребёнок может взять не больше одного печенья.

Формат ввода
В первой строке записано n —– количество детей.
Во второй —– n чисел, разделённых пробелом, каждое из которых –— фактор
жадности ребёнка. Это натуральные числа, не превосходящие 1000.
В следующей строке записано число m –— количество печенек.
Далее —– m натуральных чисел, разделённых пробелом – размеры печенек. Размеры
печенек не превосходят 1000.

Оба числа n и m не превосходят 10000.

Формат вывода
Нужно вывести одно число –— количество детей, которые останутся довольными

Пример 1
Ввод
2
1 2
3
2 1 3
Вывод
2

Пример 2
Ввод
3
2 1 3
2
1 1
Вывод
1
"""

n, greedy = int(input()), sorted(map(int, input().split()))
m, cakes = int(input()), sorted(map(int, input().split()))
result = 0
for i in greedy:
    while len(cakes) > 0:
        if cakes[0] >= i:
            result += 1
            cakes.pop(0)
            break
        cakes.pop(0)
print(result)