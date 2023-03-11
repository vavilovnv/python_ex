# Условие задачи https://stepik.org/lesson/124572/step/14?unit=756164

"""
Лучшие
В 39 школе в 7Б классе учатся N учеников. Недавно они писали проверочную 
работу по информатике. Определите трех учеников с наилучшими баллами. Выведите
фамилии и имена этих учащихся в порядке убывания их баллов. Известно, что у
всех учеников разные баллы.

Входные данные

На первой строке дано число N (3≤ N ≤100 000)– количество учеников.
В следующих N строках заданы фамилия, имя и балл по информатике. Данные в
каждой из строк разделены одним пробелом. Балл – это целое значение от 1 до
100 000.

Выходные данные

Необходимо вывести пары фамилия-имя по одной на строке, разделяя фамилию и имя
одним пробелом. Выводить оценки не нужно.
"""

def bubble_sort(iterable):
    for i in range(3):
        for j in range(len(iterable) - i - 1):
            if iterable[j][1] > iterable[j + 1][1]:
                iterable[j], iterable[j + 1] = iterable[j + 1], iterable[j]
    return reversed(iterable)


def main():
    result = []
    for _ in range(int(input())):
        surname, name, score = input().split()
        result.append((f'{surname} {name}', int(score)))
    print(*(v[0] for i, v in enumerate(bubble_sort(result)) if i < 3), sep='\n')


if __name__ == '__main__':
    main()
