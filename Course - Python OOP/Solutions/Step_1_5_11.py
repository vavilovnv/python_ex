# Условие задачи https://stepik.org/lesson/701975/step/11?unit=702076

from random import randint


class Cell:
    def __init__(self, around_mines, mine):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    def __init__(self, n, m):
        self.pole = []
        self.N = n
        self.M = m
        self.init()

    def init(self):

        def count_mines(pole, i, j):
            count = 0
            for x in range(max(0, i - 1), min(self.N, i + 2)):
                for y in range(max(0, j - 1), min(self.N, j + 2)):
                    if pole[x][y] == '*' and not (x == i and y == j):
                        count += 1
            return count

        cells, mines = pow(self.N, 2), set()
        while len(mines) < self.M:
            mines.add(randint(0, cells))
        pole, x = [[0] * self.N for _ in range(self.N)], 0
        for i in range(self.N):
            for j in range(self.N):
                if x in mines:
                    pole[i][j] = '*'
                x += 1
        for i in range(self.N):
            self.pole.append([])
            for j in range(self.N):
                self.pole[i].append(Cell(count_mines(pole, i, j), pole[i][j] == '*'))

    def show(self):
        for i in range(self.N):
            for j in range(self.N):
                if self.pole[i][j].mine:
                    print('*', end=' ')
                else:
                    print(self.pole[i][j].around_mines, end=' ')
            print()


pole_game = GamePole(10, 12)
pole_game.show()
