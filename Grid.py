import pygame
from Block import Block
from settings import *

class Grid:

    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.grid = None
        self.win = None
        self.clock = None
        self.fps = FPS

    def display_init(self):

        pygame.init()
        pygame.font.init()

        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sudoku Solver")

        self.clock = pygame.time.Clock()

    def draw(self, win: pygame.Surface):
        win.fill((51, 51, 51))

        pygame.display.update()
        

    def quit(self):
        pygame.font.quit()
        pygame.quit()

    def run(self):

        self.display_init()

        run = True
        while run:
            self.clock.tick(self.fps)
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_1:
                        print("1")

            self.draw(self.win)

        self.quit()



if __name__ == "__main__":
    X = Grid()
    X.run()