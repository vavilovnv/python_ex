# условие задачи https://stepik.org/lesson/24462/step/7?auth=login&unit=6768

# Вам дано описание наследования классов в следующем формате.
# <имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
# Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.
# Или эквивалентно записи:
# class Class1(Class2, Class3 ... ClassK):
#     pass
# Класс A является прямым предком класса B, если B отнаследован от A:
# class B(A):
#     pass
# Класс A является предком класса B, если
# A = B;
# A - прямой предок B
# существует такой класс C, что C - прямой предок B и A - предок C
# Например:
# class B(A):
#     pass
#
# class C(B):
#     pass
#
# # A -- предок С
#
# Вам необходимо отвечать на запросы, является ли один класс предком другого класса
# Важное примечание:
# Создавать классы не требуется.
# Мы просим вас промоделировать этот процесс, и понять существует ли путь от одного класса до другого.
# Формат входных данных
# В первой строке входных данных содержится целое число n - число классов.
# В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется
# i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется
# сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.
# В следующей строке содержится число q - количество запросов.
# В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
# Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.
# Формат выходных данных
# Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2, и "No", если не
# является.

# import sys

def is_ancestor(ans, cls):
    if ans in classes[cls]:
        return True
    else:
        for i in classes[cls]:
            if i != cls:
                check = is_ancestor(ans, i)
                if check:
                    return True
        return False


classes = {}
for line in [input().strip().split() for i in range(int(input()))]:
    classes[line[0]] = [line[0]]
    if len(line) > 1:
        classes[line[0]] += line[2:]

for line in [input().strip().split() for i in range(int(input()))]:
    print('Yes' if is_ancestor(line[0], line[1]) else 'No')

# альтернативный ввод данных из файлов
#
# classes = {}
# with open('classes.txt', 'r') as f:
#     for line in f:
#         line = line.strip().split()
#         classes[line[0]] = [line[0]]
#         if len(line) > 1:
#             classes[line[0]] += line[2:]
# print(classes)
#
# with open('input.txt', 'r') as f:
#     for line in f:
#         line = line.strip().split()
#         if is_ancestor(line[0], line[1]):
#             print('Yes')
#         else:
#             print('No')
