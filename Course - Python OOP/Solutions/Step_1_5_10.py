# Условие задачи https://stepik.org/lesson/701975/step/10?unit=702076

import sys


class ListObject:
    def __init__(self, data, next_obj=None):
        self.data = data
        self.next_obj = next_obj

    def link(self, obj):
        self.next_obj = obj


head_obj = None
lst_in = list(map(str.strip, sys.stdin.readlines()))
for i in reversed(lst_in):
    head_obj = ListObject(i, head_obj)
