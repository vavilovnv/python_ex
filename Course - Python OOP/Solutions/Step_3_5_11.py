# Условие задачи https://stepik.org/lesson/701990/step/11?unit=702091

class Box:

    def __init__(self):
        self.__items = {}

    def add_thing(self, obj):
        if obj.name not in self.get_things():
            self.__items[obj.name] = obj

    def get_things(self):
        return self.__items

    def __eq__(self, other):
        return self.get_things() == other.get_things()


class Thing:

    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        return (self.name.lower() == other.name.lower()
                and self.mass == other.mass)
