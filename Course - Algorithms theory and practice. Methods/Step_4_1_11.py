# Условие задачи https://stepik.org/lesson/13238/step/11?unit=3424

# По данному числу 1≤n≤10^9 найдите максимальное число k, для которого n можно
#  представить как сумму k различных натуральных слагаемых. Выведите в первой
# строке число k, во второй — k слагаемых.

def different_summations(num: int) -> list:
    '''Функция формирует максимальный по количеству элементов список из
    k-слагаемых для переданного числа num. Алгоритм основан на принципе
    жадного алгоритма. За достоверный шаг берется выбор наименьшего
    слагаемоего.'''
    summations, i = [], 1
    while num - i > i:
        summations.append(i)
        num -= i
        i += 1
    summations.append(num)
    return summations


if __name__ == '__main__':
    summations = different_summations(int(input()))
    print(len(summations))
    print(*summations)
