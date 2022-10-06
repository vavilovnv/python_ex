# Текст задания: https://stepik.org/lesson/24470/step/7?unit=6776

# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall(r'(cat)', line)) >= 2:
        print(line)


