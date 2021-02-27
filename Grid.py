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

    def draw(self, win: pygame.Surface):
        pass
        

    def quit(self):
        pygame.font.quit()
        pygame.quit()

    def run(self):

        self.display_init()

        run = True
        while run:
            
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_1:
                        print("1")

        self.quit()



if __name__ == "__main__":
    X = Grid()
    X.run()