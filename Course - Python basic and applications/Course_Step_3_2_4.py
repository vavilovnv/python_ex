# Текст задания: https://stepik.org/lesson/24470/step/10?unit=6776

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if re.search(r'\\', line):
        print(line)

