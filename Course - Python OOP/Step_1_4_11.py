# Условие задачи https://stepik.org/lesson/701974/step/11?unit=702075

class Translator:
    DICTIONARY = {}
    
    def add(self, eng, rus):
        if eng not in self.DICTIONARY:
            self.DICTIONARY[eng] = [rus]
        else:
            self.DICTIONARY[eng].append(rus)
    
    def remove(self, eng):
        del self.DICTIONARY[eng]
    
    def translate(self, eng):
        return self.DICTIONARY[eng]


tr = Translator()
tr.add('tree', 'дерево')
tr.add('car', 'машина')
tr.add('car', 'автомобиль')
tr.add('leaf', 'лист')
tr.add('river', 'река')
tr.add('go', 'идти')
tr.add('go', 'ехать')
tr.add('go', 'ходить')
tr.add('milk', 'молоко')
tr.remove('car')
print(*tr.translate('go'))
