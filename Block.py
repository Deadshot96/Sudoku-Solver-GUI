import pygame
from settings import *
from typing import Tuple

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
        self.tempfont = pygame.font.SysFont('comicsans', 30, False, True)

    def set_number(self, number: int) -> None:
        self.number = number

    def select(self) -> None:
        self.selected = True

    def is_selected(self) -> None:
        return self.selected

    def make_readonly(self) -> None:
        self.readonly = True
        self.tempNum = self.number

    def remove_readonly(self) -> None:
        self.readonly = False
        self.number = 0 

    def is_readonly(self) -> bool:
        return self.readonly

    def deselect(self) -> None:
        self.selected = False

    def is_empty(self) -> bool:
        return self.number == 0

    def set_temp(self, num: int) -> None:
        self.tempNum = num

    def remove_temp(self) -> None:
        self.tempNum = 0

    def get_dims(self) -> Tuple:
        return self.row, self.col

    def set_valid(self) -> None:
        self.set_number(self.tempNum)
        self.make_readonly()
        
    def get_number(self) -> int:
        return self.tempNum

    def __eq__(self, num: int) -> bool:
        return self.tempNum == num
    
    def draw(self, win: pygame.Surface):
        if self.is_selected():
            rect = self.x + 1, self.y + 1, self.size - 2, self.size - 2
            pygame.draw.rect(win, SELECTED_COLOR, rect, 2)

        if not (self.number == 0 and self.tempNum == 0):

            if self.is_readonly():
                numText = self.font.render(str(self.number), 1, MID_BLACK)
                w, h = numText.get_size()

                win.blit(numText, (self.x + (self.size - w) // 2, self.y + (self.size - h) // 2))
            
            else:
                numText = self.tempfont.render(str(self.tempNum), 1, TEMP_BLACK)
                w, h = numText.get_size()
                win.blit(numText, (self.x + 5, self.y + 5))

