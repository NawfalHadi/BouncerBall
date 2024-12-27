import pygame
import math

from main.constant.Size import *
from main.constant.Color import *
from main.ui.Line import Line

class GamesSimulationPage:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
        "== GAMEPLAY STATE =="
        self.isLoading = True
        self.isRunning = True

        self.init_field()

    def init_field(self):
        self.left_field = Line((70, 1), (70, 1 + FIELD_HEIGHT), BLACK)
        self.right_field = Line((70 + FIELD_WIDTH, 1), (70 + FIELD_WIDTH, 1 + FIELD_HEIGHT), BLACK)
        self.top_field = Line((70, 1), (70 + FIELD_WIDTH, 1), BLACK)
        self.bottom_field = Line((70, 1 + FIELD_HEIGHT), (70 + FIELD_WIDTH, 1 + FIELD_HEIGHT), BLACK)

        self.top_gk_left_field = Line((70, 183), (70 + FIELD_GK_WIDTH, 183), RED)
        self.bottom_gk_left_field = Line((70, 393), (70 + FIELD_GK_WIDTH, 393), RED)
        self.gk_left_vertical = Line((70 + FIELD_GK_WIDTH, 183), (70 + FIELD_GK_WIDTH, 183 + FIELD_GK_HEIGHT), BLACK)

        self.center_field = Line((70 + FIELD_WIDTH / 2, 1), (70 + FIELD_WIDTH / 2, 1 + FIELD_HEIGHT), BLACK)

        self.top_gk_right_field = Line((70 + FIELD_WIDTH - FIELD_GK_WIDTH, 183), (70 + FIELD_WIDTH, 183), RED)
        self.bottom_gk_right_field = Line((70 + FIELD_WIDTH - FIELD_GK_WIDTH, 393), (70 + FIELD_WIDTH, 393), RED)
        self.gk_right_vertical = Line((70 + FIELD_WIDTH - FIELD_GK_WIDTH, 183), (70 + FIELD_WIDTH - FIELD_GK_WIDTH, 183 + FIELD_GK_HEIGHT), BLACK)


    def draw_field(self):
        self.left_field.draw(self.screen)
        self.right_field.draw(self.screen)
        self.top_field.draw(self.screen)
        self.bottom_field.draw(self.screen)

        self.top_gk_left_field.draw(self.screen)
        self.bottom_gk_left_field.draw(self.screen)
        self.gk_left_vertical.draw(self.screen)

        self.center_field.draw(self.screen)
        self.center_circle = pygame.draw.circle(self.screen, BLACK, (70 + FIELD_WIDTH / 2, 1 + FIELD_HEIGHT / 2), 73, 2)

        self.top_gk_right_field.draw(self.screen)
        self.bottom_gk_right_field.draw(self.screen)
        self.gk_right_vertical.draw(self.screen)  

    def run(self):
        while self.isRunning:
            self.screen.fill(WHITE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRunning = False

            self.draw_field()

            pygame.display.update()


