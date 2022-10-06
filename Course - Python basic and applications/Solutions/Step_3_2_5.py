# Текст задания: https://stepik.org/lesson/24470/step/11?unit=6776

# Вам дана последовательность строк.
# Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if re.search(r'\b(\w+)\1\b', line):
        print(line)
