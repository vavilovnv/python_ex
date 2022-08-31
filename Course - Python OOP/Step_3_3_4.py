# Условие задачи https://stepik.org/lesson/701988/step/4?unit=702089

class Model:

    def __init__(self):
        self.queries = {}

    def query(self, *args, **kwargs):
        for key, value in kwargs.items():
            self.queries[key] = value

    def __str__(self):
        if len(self.queries) == 0:
            return 'Model'
        lst = [f'{k} = {v}' for k, v in self.queries.items()]
        return f'Model: {", ".join(lst)}'
