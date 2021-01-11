# Текст задания: https://stepik.org/lesson/24470/step/11?unit=6776

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if re.search(r'\b(\w+)\1\b', line):
        print(line)

