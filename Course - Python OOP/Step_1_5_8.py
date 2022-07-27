# Условие задачи https://stepik.org/lesson/701975/step/8?unit=702076

class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, mem_slots):
        self.name = name
        self.cpu = cpu
        self.mem_slots = mem_slots
        self.total_mem_slots = 4

    def get_config(self):
        return [f'Материнская плата: {self.name}',
                f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
                f'Слотов памяти: {self.total_mem_slots}',
                f'Память:  {"; ".join([f"{i.name} - {i.volume}" for i in self.mem_slots])}']


mb = MotherBoard('Asus', CPU('Intel', 5400), [Memory('Xen1', 3333), Memory('Xen2', 3333)])
