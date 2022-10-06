# Текст задания: https://stepik.org/lesson/24470/step/8?unit=6776

# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве слова.

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if re.search(r'\bcat\b', line):
        print(line)
