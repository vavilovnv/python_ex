# Условие задачи https://stepik.org/lesson/864077/step/11

"""
Класс Currency

Реализуйте класс Currency для работы со значениями в различных валютах.
Экземпляр класса Currency должен создаваться на основе числового значения и
валюты:
money1 = Currency(10, 'EUR')
money2 = Currency(20, 'USD')

Поддерживаемые валюты: EUR (евро), USD (доллар) и RUB (рубль).

В качестве неформального строкового представления экземпляр класса Currency
должен иметь собственное числовое значение и валюту:
print(money1)                                      # 10 EUR
print(money2)                                      # 20 USD

Экземпляр класса Currency должен поддерживать операцию конвертации в другую
валюту с помощью метода change_to():
money1.change_to('RUB')
print(money1)                                      # 900 RUB

Экземпляры класса Currency должны поддерживать между собой операции сложения,
вычитания, умножения и деления с помощью операторов +, -, * и / соответственно:
print(Currency(5, 'EUR') + Currency(5, 'EUR'))     # 10 EUR
print(Currency(5, 'EUR') + Currency(11, 'USD'))    # 15.0 EUR
print(Currency(5, 'RUB') + Currency(11, 'USD'))    # 905.0 RUB
print(Currency(5, 'USD') * Currency(5, 'EUR'))     # 27.5 USD

Обратите внимание, результирующую валюту должен определять левый операнд. 

Примечание. Таблица курсов валют:

1 EUR	90 RUB
1 EUR	1.1 USD
"""

from dataclasses import dataclass

COURSES = {
    'EUR': {'EUR': 1, 'USD': 1.1, 'RUB': 90},
    'USD': {'EUR': 1 / 1.1, 'USD': 1,  'RUB': 1 / 1.1 * 90},
    'RUB': {'EUR': 1 / 90, 'USD': 1 / 90 * 1.1, 'RUB': 1}
}

@dataclass
class Currency:

    amount: int
    val: str

    def __str__(self):
        return f"{round(self.amount, 2)} {self.val}"

    def change_to(self, val):
        self.amount = COURSES[self.val][val] * self.amount
        self.val = val

    def __add__(self, other):
        amount = COURSES[other.val][self.val] * other.amount
        return Currency(self.amount + amount, self.val)

    def __sub__(self, other):
        amount = COURSES[other.val][self.val] * other.amount
        return Currency(self.amount - amount, self.val)

    def __mul__(self, other):
        amount = COURSES[other.val][self.val] * other.amount
        return Currency(self.amount * amount, self.val)

    def __truediv__(self, other):
        amount = COURSES[other.val][self.val] * other.amount
        return Currency(self.amount / amount, self.val)
