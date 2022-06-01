# Условие задачи https://stepik.org/lesson/13238/step/9?unit=3424

# По данным n отрезкам необходимо найти множество точек минимального размера,
# для которого каждый из отрезков содержит хотя бы одну из точек.
#
# В первой строке дано число 1≤n≤100 отрезков. Каждая из последующих nn строк
# содержит по два числа 0≤l≤r≤10, задающих начало и конец отрезка. Выведите
# оптимальное число m точек и сами m точек. Если таких множеств точек
# несколько, выведите любое из них.

def set_of_points(samples: list) -> list:
    '''Применение жадного алгоритма для нахождения минимального количества
    общих точек для отрезков в переданном списке. Принцип работы алгоритма
    в том, что за достоверный шаг берется правая граница первого отрезка и
    сравнивается с левыми границами остальных отрезков. Как только правая
    граница будет меньше левой, значит у этих отрезков нет общих точек. Пока
    это не так, правая граница отрезка считается общей точкой для всех отрезков
    для которых она больше, либо равна их левым границам.'''
    points = [samples[0][1]]
    for sample in samples:
        if sample[0] > points[-1]:
            points.append(sample[1])
    return points


if __name__ == '__main__':
    samples = sorted(
        [[int(i) for i in input().split()] for _ in range(int(input()))],
        key=lambda x: x[1]
    )
    points = set_of_points(samples)
    print(str(len(points)), ' '.join(map(str, points)),  sep='\n')
