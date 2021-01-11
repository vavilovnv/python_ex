# Условие задачи: https://stepik.org/lesson/24463/step/9?auth=login&unit=6771

class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, n):
        if n > 0:
            super().append(n)
        else:
            raise NonPositiveError
