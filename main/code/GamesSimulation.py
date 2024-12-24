import sys, os

import pygame
import math

from main.constant.Size import *
from main.constant.Color import *

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

class GamesSimulation:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
        "== GAMEPLAY STATE =="
        self.isLoading = True
        self.isRunning = True

    def run(self):
        while self.isRunning:
            self.screen.fill(WHITE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRunning = False

            pygame.display.update()


if __name__ == "__main__":
    GamesSimulation().run()
    pygame.quit()
    sys.exit()