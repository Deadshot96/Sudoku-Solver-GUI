import pygame
from Block import Block
from settings import *
from typing import Tuple

class Sudoku:

    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.sudoku_width = SUDOKU_WIDTH
        self.sudoku_height = SUDOKU_HEIGHT
        self.x_delta = X_DELTA
        self.y_delta = Y_DELTA
        self.size = SIZE
        self.grid = None
        self.win = None
        self.sudokuWin = None
        self.clock = None
        self.fps = FPS
        self.selected = None

    def display_init(self):

        pygame.init()
        pygame.font.init()

        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sudoku Solver")

        self.sudokuWin = self.win.subsurface((self.x_delta, self.y_delta, self.sudoku_width, self.sudoku_width))

        self.clock = pygame.time.Clock()

    def grid_init(self):
        self.grid = list()
        for row in range(9):
            self.grid.append(list())
            for col in range(9):
                self.grid[row].append(Block(row, col))

        for i, row in enumerate(self.board):
            for j, element in enumerate(row):
                self.grid[i][j].set_number(element)
                if element != 0:
                    self.grid[i][j].make_readonly()

    def get_row_col(self, pos: Tuple) -> Tuple:
        x, y = pos
        row = (y - self.y_delta) // self.size
        col = (x - self.x_delta) // self.size

        return row, col

    def is_valid_dims(self, row: int, col: int) -> bool:
        return row in range(9) and col in range(9)



    def draw_grid(self, win: pygame.Surface):
        width, height = win.get_size()
        color = MID_BLACK

        # pygame.draw.line(win, color, (0, 0), (width, 0), 2)
        # pygame.draw.line(win, color, (0, 0), (0, height), 2)

        for i in range(9):
            linewidth = 2 if i % 3 == 0 else 1

            pygame.draw.line(win, color, (0, i * self.size), (width, i * self.size), linewidth)
            pygame.draw.line(win, color, (i * self.size, 0), (i * self.size, height), linewidth)

        pygame.draw.line(win, color, (width - 2, 0), (width - 2, height), 2)
        pygame.draw.line(win, color, (0, height - 2), (width, height - 2), 2)



    def draw_board(self, win: pygame.Surface) -> None:
        if self.grid is None:
            return

        for row in self.grid:
            for block in row:
                block.draw(win)
        

            

    def draw(self, win: pygame.Surface):
        win.fill(BACKGROUND_COLOR)
        self.sudokuWin.fill(CREAM)

        self.draw_grid(self.sudokuWin)
        self.draw_board(self.sudokuWin)

        pygame.display.update()
        

    def quit(self):
        pygame.font.quit()
        pygame.quit()

    def run(self):

        self.display_init()
        self.grid_init()

        run = True
        while run:
            self.clock.tick(self.fps)
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_1:
                        print("1")

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = self.get_row_col(pos)

                    if self.is_valid_dims(row, col) and not self.grid[row][col].is_readonly():
                        if self.selected:
                            self.selected.deselect()

                        self.selected = self.grid[row][col]
                        self.selected.select()

                    print(row, col, sep='\t')

            self.draw(self.win)

        self.quit()



if __name__ == "__main__":
    X = Sudoku()
    X.run()