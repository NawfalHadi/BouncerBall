import pygame
import math

from main.constant.Size import *
from main.constant.Color import *

class GamesSimulationPage:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
        "== GAMEPLAY STATE =="
        self.isLoading = True
        self.isRunning = True

    def draw_field(self):
        pass

    def run(self):
        while self.isRunning:
            self.screen.fill(WHITE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRunning = False

            pygame.display.update()


