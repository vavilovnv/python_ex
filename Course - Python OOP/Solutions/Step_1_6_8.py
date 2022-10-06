# Условие задачи https://stepik.org/lesson/701976/step/8?unit=702077

class SingletonFive:
    __instance = None
    __count = 0

    def __new__(cls, *args, **kwargs):
        if cls.__count < 5:
            cls.__count += 1
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        SingletonFive.__count = 0

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]
