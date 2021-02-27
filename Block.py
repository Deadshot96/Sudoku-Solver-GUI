import pygame

class Block:

    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.size = 50
        self.number = 0
        self.x = self.size * self.col
        self.y = self.size * self.row
        self.selected = False

    def set_number(self, number: int) -> None:
        self.number = number

    def select(self) -> None:
        self.selected = True

    def is_selected(self) -> None:
        return self.selected

    def deselect(self) -> None:
        self.selected = False
    
    def draw(self, win: pygame.Surface):
        pass
