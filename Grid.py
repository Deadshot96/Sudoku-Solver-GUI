import pygame
from Block import Block
from settings import *

class Grid:

    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.grid = None

    def quit(self):
        pygame.font.quit()
        pygame.quit()

    def run(self):

        run = True

        while run:
            pass



if __name__ == "__main__":
    X = Grid()
    X.run()