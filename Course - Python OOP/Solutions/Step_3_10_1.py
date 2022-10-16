# Условие задачи https://stepik.org/lesson/717070/step/1?unit=717930
"""
Крестики-нолики.
"""
from random import choice


class Cell:

    def __init__(self):
        self.value = TicTacToe.FREE_CELL

    def __bool__(self):
        return self.value == TicTacToe.FREE_CELL


class TicTacToe:

    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2
    SIZE = 3

    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(TicTacToe.SIZE)) for _ in range(TicTacToe.SIZE))
        self.wins = {
            'human': False,
            'computer': False,
            'draw': False}

    def init(self):
        self.__init__()

    @property
    def is_human_win(self):
        return self.wins['human']

    @property
    def is_computer_win(self):
        return self.wins['computer']

    @property
    def is_draw(self):
        return self.wins['draw']

    @is_draw.setter
    def is_draw(self, value):
        self.is_draw = value

    def check_index(self, row, col):
        if (not(isinstance(row, int) and 0 <= row < TicTacToe.SIZE
                or not(isinstance(col, int) and 0 <= col < TicTacToe.SIZE))):
            raise IndexError('некорректно указанные индексы')

    def check_win(self):
        for value in (TicTacToe.HUMAN_X, TicTacToe.COMPUTER_O):
            key = 'human' if value == TicTacToe.HUMAN_X else 'computer'
            for i in range(TicTacToe.SIZE):
                if (all([self.pole[i][j].value == value for j in range(TicTacToe.SIZE)])
                        or all([self.pole[j][i].value == value for j in range(TicTacToe.SIZE)])):
                    self.wins[key] = True
                    return
            if (all([self.pole[i][i].value == value for i in range(TicTacToe.SIZE)])
                    or (all([self.pole[i][TicTacToe.SIZE-1-i].value == value for i in range(TicTacToe.SIZE)]))):
                self.wins[key] = True
                return
        if (not self.is_human_win
                and not self.is_computer_win
                and not any([any([bool(cell) for cell in row]) for row in self.pole])):
            self.wins['draw'] = True
            return

    def show(self):
        for i in range(TicTacToe.SIZE):
            print('-------')
            for j in range(TicTacToe.SIZE):
                print(('|X' if self.pole[i][j].value == TicTacToe.HUMAN_X
                       else '|O' if self.pole[i][j].value == TicTacToe.COMPUTER_O else '| '), end='')
            print('|')
        print('-------')

    def human_go(self):
        while True:
            row, col = list(map(int, input('Введите координаты:').split()))
            self.check_index(row, col)
            if self.pole[row][col]:
                self.pole[row][col].value = TicTacToe.HUMAN_X
                break

    def computer_go(self):
        while True:
            row, col = choice((0, 1, 2)), choice((0, 1, 2))
            if self.pole[row][col]:
                self.pole[row][col].value = TicTacToe.COMPUTER_O
                break

    def __getitem__(self, idx):
        row, col = idx
        self.check_index(row, col)
        return self.pole[row][col].value

    def __setitem__(self, idx, value):
        row, col = idx
        self.check_index(row, col)
        self.pole[row][col].value = value
        self.check_win()

    def __bool__(self):
        return (not self.is_human_win
                and not self.is_computer_win
                and not self.is_draw)


def main():
    game = TicTacToe()
    game.init()
    step_game = 0
    while game:
        game.show()

        if step_game % 2 == 0:
            game.human_go()
        else:
            game.computer_go()

        step_game += 1

    game.show()

    if game.is_human_win:
        print("Поздравляем! Вы победили!")
    elif game.is_computer_win:
        print("Все получится, со временем.")
    else:
        print("Ничья.")


if __name__ == '__main__':
    main()
