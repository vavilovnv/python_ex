# Текст задания: https://stepik.org/lesson/415554/step/10?unit=405083

# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. Теперь он использует их в
# качестве серверов "Пегого дудочника". Помогите владельцу фирмы отыскать все зараженные холодильники.
#
# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней присутствует
# слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв), то холодильник заражен и
# нужно вывести номер холодильника, нумерация начинается с единицы
#
# Формат входных данных
# В первой строке подаётся число nn – количество холодильников. В последующих nn строках вводятся строки, содержащие
# латинские строчные буквы и цифры, в каждой строке от 55 до 100100 символов.
#
# Формат выходных данных
# Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, ничего выводить
# не нужно.

import re

ref = [input() for i in range(int(input()))]
for i in range(len(ref)):
    if len(re.findall(r'\w*a\w*n\w*t\w*o\w*n\w*', ref[i])) > 0:
        print(i + 1, end=' ')
