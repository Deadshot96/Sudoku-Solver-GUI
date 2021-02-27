import pygame

class Block:

    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.size = 50
        self.number = 0

    def set_number(self, number: int) -> None:
        self.number = number


    def draw(self, win: pygame.Surface):
        pass
