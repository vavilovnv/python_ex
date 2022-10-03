"""
Хаотичность погоды.

Метеорологическая служба вашего города решила исследовать погоду новым
способом. Под температурой воздуха в конкретный день будем понимать
максимальную температуру в этот день. Под хаотичностью погоды за n дней служба
понимает количество дней, в которые температура строго больше, чем в день до
(если такой существует) и в день после текущего (если такой существует).
Например, если за 5 дней максимальная температура воздуха составляла
[1, 2, 5, 4, 8] градусов, то хаотичность за этот период равна 2: в 3-й и 5-й
дни выполнялись описанные условия.
Определите по ежедневным показаниям температуры хаотичность погоды за этот
период. Заметим, что если число показаний n=1, то единственный день будет
хаотичным.

Формат ввода
В первой строке дано число n – длина периода измерений в днях, 1 ≤ n≤ 10^5.
Во второй строке даны n целых чисел – значения температуры в каждый из n дней.
Значения температуры не превосходят 273 по модулю.

Формат вывода
Выведите единственное число — хаотичность за данный период.

Пример 1
Ввод
7
-1 -10 -8 0 2 0 5
Вывод
3

Пример 2
Ввод
5
1 2 5 4 8
Вывод
2
"""

n, res = int(input()), 0 
lst = list(map(int, input().split()))
if n == 1:
    res += 1
else:
    for i in range(n): 
        if (i == 0 and lst[i+1] < lst[i]
                or i == n-1 and lst[i-1] < lst[i]
                or lst[i-1] < lst[i] and lst[i+1] < lst[i]):
            res += 1
print(res)