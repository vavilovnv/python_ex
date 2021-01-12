# Текст задания: https://stepik.org/lesson/24470/step/9?unit=6776

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if re.search(r'z...z', line):
        print(line)

