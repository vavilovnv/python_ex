# Условие задачи https://stepik.org/lesson/864077/step/10

"""
Классы Game и Cell

В этой задаче вам необходимо реализовать поле для игры в Сапера в виде двух
классов Game и Cell. Экземпляр первого класса будет описывать само игровое
поле, экземпляр класса Cell — одну его ячейку. Экземпляр класса Game должен
создаваться на основе трех значений: количество строк (длина поля), количество
столбцов (ширина поля) и общее количество мин на поле:
game = Game(14, 18, 40)    # 14 строк, 18 столбцов и 40 мин

Количество строк и столбцов, а также общее количество мин должны быть доступны
по соответствующим атрибутам:
print(game.rows)           # 14
print(game.cols)           # 18
print(game.mines)          # 40

Также экземпляр класса Game должен иметь атрибут board, представляющий игровое
поле в виде двумерного списка. Количество подсписков в этом списке должно
совпадать с количеством строк, количество элементов в подсписках — с
количеством столбцов. Каждый элемент подсписка должен представлять собой
экземпляр класса Cell и иметь соответствующий набор атрибутов:
cell = game.board[0][0]

print(cell.row)            # 0; строка ячейки
print(cell.col)            # 0; столбец ячейки
print(cell.mine)           # True или False в зависимости от того, содержит ячейка мину или нет
print(cell.neighbours)     # число от 0 до 8, количество мин в соседних ячейках

Игровое поле при создании должно заполняться минами случайным образом.

Примечание 1. Для проверки того, что в экземпляре класса Cell хранится верное
количество мин в соседних ячейках, в одном из тестов мы используем
собственную функцию get_neighbours_count(), которая считает это количество.
"""

from random import shuffle

class Cell:

    def __init__(self, row, col, mine):
        self.row = row
        self.col = col
        self.mine = mine
        self.neighbours = 0

class Game:

    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self._init_board()

    def _init_board(self):
        self.board = [[Cell(i, j, False) for j in range(self.cols)] for i in range(self.rows)]
        self._set_mines()
        self._find_neighbours()

    def _set_mines(self):
        mines_coords = []
        for i in range(self.rows):
            for j in range(self.cols):
                mines_coords.append((i, j))
        shuffle(mines_coords)
        for coord in mines_coords[:self.mines]:
            self.board[coord[0]][coord[1]].mine = True

    def _find_neighbours(self):
        moves = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        for i in range(self.rows):
            for j in range(self.cols):
                count = 0
                for move in moves:
                    is_mine = (
                            0 <= i + move[0] < self.rows
                            and 0 <= j + move[1] < self.cols
                            and self.board[i + move[0]][j + move[1]].mine
                    )
                    if is_mine:
                        count += 1
                self.board[i][j].neighbours = count
