from abc import ABC, abstractmethod


# Банкомат.
# Умеет выдавать купюры для заданной суммы, либо отвечать отказом.
# Допустимые номиналы: 50₽, 100₽, 500₽, 1000₽, 5000₽.

# мой говнокод
class ATM:
    IDS = {
        1: 50,
        2: 100,
        3: 500,
        4: 1000,
        5: 5000,
    }

    # место для кода
    def __init__(self):
        self._sdk = ClassSDK()
        self._all_money = 0
        self._init_atm()


    def withdraw(self, amount):


        if not self._is_correct_amount(amount):
            raise ValueError("Incorrect amount")

        banknotes: dict[int, int] = self._to_count_banknotes(amount)


        for k, v in banknotes.items():
            self._sdk.move_banknote_to_dispenser(self.IDS[k], v)
            self._count_money[k] -= v
            self._all_money -= self.IDS[k] * v

        self._sdk.open_dispenser()

    def _init_atm(self):
        self._count_money = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0
        }
        for k in self._count_money:
            self._count_money[k] = self._sdk.count_banknotes(k)
            self._all_money += self.IDS[k] * self._count_money[k]


    def _is_correct_amount(self, amount: int) -> bool:
        if amount > self._all_money:
            return False

        curr = amount

        for nominal in sorted(self.IDS.values(), reverse=True):
            count_nom = curr // nominal
            to_withdraw = min(count_nom, self._count_money[1])
            curr -= to_withdraw * nominal
            if curr <= 0:
                break

        if curr != 0:
            return False

        return True

    def _to_count_banknotes(self, amount: int) -> dict[int, int]:
        result = {}
        curr = amount
        for nominal, count_banknotes in sorted(self.IDS.items(), reverse=True, key=lambda x: x[1]):
            if curr <=0 :
                break
            result[nominal] = min(curr // self.IDS[nominal], self._count_money[nominal])
            curr -= result[nominal] * self.IDS[nominal]
        return result

# было по условию
# API для взаимодействия с аппаратурой банкомата.
# Краткий ликбез по устройству банкомата:
# - деньги расположены в кассетах, кассеты устанавливаются инкассацией;
# - в каждой кассете лежат свои купюры, количество известно инкассатору при установке;
# - банкомат может подсчитать оставшиеся в кассетах банкноты, но эта операция занимает около 10 секунд, и шумная, её стоит вызывать как можно реже.
class SDK(ABC):
    @abstractmethod
    def count_banknotes(self, banknote_id: int) -> int:
        pass

    @abstractmethod
    def move_banknote_to_dispenser(self, banknote_id: int, count: int) -> None:
        pass

    @abstractmethod
    def open_dispenser(self) -> None:
        pass


# добавил для тестов
class ClassSDK(SDK):
    def count_banknotes(self, banknote_id: int) -> int:
        return 2

    def move_banknote_to_dispenser(self, banknote_id: int, count: int) -> None:
        print(f"Выдано {banknote_id}: {count}")

    def open_dispenser(self) -> None:
        print("Деньги выданы")

banknotes = {
    50: 1,
    100: 2,
    500: 2,
    1000: 2,
    5000: 2,
}
atm = ATM()
atm.withdraw(sum(k * v for k, v in banknotes.items()))
