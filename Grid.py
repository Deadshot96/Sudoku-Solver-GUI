import pygame
from Block import Block
from settings import *

class Grid:

    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.grid = None
        self.win = None

    def display_init(self):

        pygame.init()
        pygame.font.init()

        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sudoku Solver")
        

    def quit(self):
        pygame.font.quit()
        pygame.quit()

    def run(self):

        run = True

        while run:
            pass

        self.quit()



if __name__ == "__main__":
    X = Grid()
    X.run()