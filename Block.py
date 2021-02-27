import pygame
from settings import *

class Block:



    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.size = SIZE
        self.number = 0
        self.x = self.size * self.col
        self.y = self.size * self.row
        self.selected = False
        self.tempNum = 0
        self.readonly = False

        pygame.font.init()
        self.font = pygame.font.SysFont('comicsans', 40)

    def set_number(self, number: int) -> None:
        self.number = number

    def select(self) -> None:
        self.selected = True

    def is_selected(self) -> None:
        return self.selected

    def make_readonly(self) -> None:
        self.readonly = True

    def is_readonly(self) -> bool:
        return self.readonly

    def deselect(self) -> None:
        self.selected = False

    def is_empty(self) -> None:
        return self.number == 0
    
    def draw(self, win: pygame.Surface):
        if self.is_selected():
            rect = self.x + 1, self.y + 1, self.size - 2, self.size - 2
            pygame.draw.rect(win, SELECTED_COLOR, rect, 2)

        if not self.is_empty():
            numText = self.font.render(str(self.number), 1, MID_BLACK)
            w, h = numText.get_size()

            win.blit(numText, (self.x + (self.size - w) // 2, self.y + (self.size - h) // 2))
    

