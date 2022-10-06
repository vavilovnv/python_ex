# Текст задания: https://stepik.org/lesson/24470/step/9?unit=6776

# Вам дана последовательность строк.
# Выведите строки, содержащие две буквы "z", между которыми ровно три символа.

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if re.search(r'z...z', line):
        print(line)
