import pygame
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from constant.Size import *
from constant.Color import *

class Main:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
        "== GAMEPLAY STATE =="
        self.isLoading = True
        self.isRunning = True

    def create_button(self):
        pass

    def run(self):
        while self.isRunning:
            self.screen.fill(WHITE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRunning = False

            pygame.display.update()

if __name__ == "__main__":
    Main().run()
    pygame.quit()
    sys.exit()