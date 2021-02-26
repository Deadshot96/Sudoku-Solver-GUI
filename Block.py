import pygame

class Block:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.size = 20

    def draw(self, win: pygame.Surface):
        pass
