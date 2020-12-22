# Текст задания: https://stepik.org/lesson/24464/step/4?unit=6769

class Multifilter():
    def judge_half(pos, neg):
        return pos >= neg # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)

    def judge_any(pos, neg):
        return pos > 0 # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)

    def judge_all(pos, neg):
        return neg == 0 # допускает элемент, если его допускают все функции (neg == 0)

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable # iterable - исходная последовательность
        self.funcs = funcs # funcs - допускающие функции
        self.judge = judge # judge - решающая функция

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        for i in self.iterable:
            pos, neg = 0, 0
            for fnc in self.funcs:
                if fnc(i):
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg):
                yield i

def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)]

print(list(Multifilter(a, mul2, mul3, mul5)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(Multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(Multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# [0, 30]