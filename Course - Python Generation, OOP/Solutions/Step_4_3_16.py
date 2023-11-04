# Условие задачи https://stepik.org/lesson/794582/step/16?unit=797335

"""
Класс Knight ♞

Реализуйте класс Knight, описывающий шахматного коня. При создании экземпляра
класс должен принимать три аргумента в следующем порядке:
- horizontal — координата коня по горизонтальной оси, представленная латинской
буквой от a до h
- vertical — координата коня по вертикальной оси, представленная целым числом от
1 до 8 включительно
- color — цвет коня (black или white)

Экземпляр класса Knight должен иметь три атрибута:
- horizontal — координата коня на шахматной доске по горизонтальной оси
- vertical — координата коня на шахматной доске по вертикальной оси
- color — цвет коня

Класс Knight должен иметь четыре метода экземпляра:
- get_char() — метод, возвращающий символ N
- can_move() — метод, принимающий в качестве аргументов координаты клетки по
горизонтальной и по вертикальной осям и возвращающий True, если конь может
переместиться на клетку с данными координатами, или False в противном случае
- move_to() — метод, принимающий в качестве аргументов координаты клетки по
горизонтальной и по вертикальной осям и заменяющий текущие координаты коня на
переданные. Если конь из текущей клетки не может переместиться на клетку с
указанными координатами, его координаты должны остаться неизменными
- draw_board() — метод, печатающий шахматное поле, отмечающий на этом поле
коня и клетки, на которые может переместиться конь. Пустые клетки должны быть
отображены символом ., конь — символом N, клетки, на которые может
переместиться конь, — символом *
"""

class Knight:
    
    BOARD_SIZE = 8
    
    def __init__(self, horizontal: str, vertical: int, color: str):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color
        self._columns = {v: i for i, v in enumerate('abcdefgh', 1)}
        self._columns_str = {i: v for i, v in enumerate('abcdefgh', 1)}

    @staticmethod
    def get_char() -> str:
        return 'N'

    def can_move(self, column: str, row: int) -> bool:
        column1 = self._columns[self.horizontal]
        column2 = self._columns[column]
        return (
                abs(column1 - column2) == 1
                and abs(self.vertical - row) == 2
                or abs(column1 - column2) == 2
                and abs(self.vertical - row) == 1
        )

    def move_to(self, horizontal: str, vertical: int):
        if self.can_move(horizontal, vertical):
            self.horizontal = horizontal
            self.vertical = vertical

    def draw_board(self) -> None:
        board = [['.' for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)]
        board[self.vertical - 1][self._columns[self.horizontal] - 1] = self.get_char()
        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                if self.can_move(self._columns_str[j + 1], i + 1):
                    board[i][j] = '*'
        [print(*row, sep='') for row in board[::-1]]
