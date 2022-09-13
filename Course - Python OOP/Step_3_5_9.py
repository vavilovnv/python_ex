# Условие задачи https://stepik.org/lesson/701990/step/9?unit=702091

class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def register(cls, money):
        money.cb = cls


class Money:
    curr = None

    def __init__(self, volume=0):
        self.__cb = None
        self.__volume = volume

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, obj):
        self.__cb = obj

    def check_wallet(self):
        if self.curr is None:
            raise ValueError("Неизвестна валюта кошелька.")
        if self.__cb is None:
            raise ValueError("Неизвестен курс валют.")

    def get_volumes(self, other):
        self.check_wallet()
        other.check_wallet()
        value1 = self.volume / self.cb.rates[self.curr]
        value2 = other.volume / other.cb.rates[other.curr]
        return value1, value2

    def __lt__(self, other):
        volume1, volume2 = self.get_volumes(other)
        return volume1 < volume2

    def __eq__(self, other):
        volume1, volume2 = self.get_volumes(other)
        return abs(volume1 - volume2) < 0.1

    def __le__(self, other):
        volume1, volume2 = self.get_volumes(other)
        return volume1 <= volume2


class MoneyR(Money):
    curr = 'rub'


class MoneyD(Money):
    curr = 'dollar'


class MoneyE(Money):
    curr = 'euro'


CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(45000)
d = MoneyD(500)

CentralBank.register(r)
CentralBank.register(d)

if r > d:
    print("неплохо")
else:
    print("нужно поднажать")
