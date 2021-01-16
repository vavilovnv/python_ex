# Текст задания: https://stepik.org/lesson/24470/step/14?unit=6776

# Вам дана последовательность строк.
# В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
# Буквой считается символ из группы \w.

import sys
import re


def change(m):
    return m.group(2) + m.group(1)


for line in sys.stdin:
    line = line.rstrip()
    line = re.sub(r'\b(\w)(\w)', change, line)
    print(line)
