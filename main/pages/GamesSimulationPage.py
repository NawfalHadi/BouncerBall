import pygame
import math

from main.constant.Size import *
from main.constant.Color import *
from main.ui.Line import Line

from main.data.Ball import Ball
from main.data.Player import Player

class GamesSimulationPage:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
        "== GAMEPLAY STATE =="
        self.isLoading = True
        self.isRunning = True

        self.init_field()
        self.init_player()
        self.init_ball()

    "== FIELD =="

    def init_field(self):
        self.left_field = Line((START_FIELD_WIDHT, START_FIELD_HEIGHT), (START_FIELD_WIDHT, START_FIELD_HEIGHT + FIELD_HEIGHT), BLACK)
        self.right_field = Line((START_FIELD_WIDHT + FIELD_WIDTH, START_FIELD_HEIGHT), (START_FIELD_WIDHT + FIELD_WIDTH, START_FIELD_HEIGHT + FIELD_HEIGHT), BLACK)
        self.top_field = Line((START_FIELD_WIDHT, START_FIELD_HEIGHT), (START_FIELD_WIDHT + FIELD_WIDTH, START_FIELD_HEIGHT), BLACK)
        self.bottom_field = Line((START_FIELD_WIDHT, START_FIELD_HEIGHT + FIELD_HEIGHT), (START_FIELD_WIDHT + FIELD_WIDTH, START_FIELD_HEIGHT + FIELD_HEIGHT), BLACK)

        self.top_gk_left_field = Line((START_FIELD_GK_WIDHT, START_FIELD_GK_HEIGHT), (START_FIELD_GK_WIDHT + FIELD_GK_WIDTH, START_FIELD_GK_HEIGHT), RED)
        self.bottom_gk_left_field = Line((START_FIELD_WIDHT, START_FIELD_GK_HEIGHT + FIELD_GK_HEIGHT), (START_FIELD_WIDHT + FIELD_GK_WIDTH, START_FIELD_GK_HEIGHT + FIELD_GK_HEIGHT), RED)
        self.gk_left_vertical = Line((START_FIELD_WIDHT + FIELD_GK_WIDTH, START_FIELD_GK_HEIGHT), (START_FIELD_WIDHT + FIELD_GK_WIDTH, START_FIELD_GK_HEIGHT + FIELD_GK_HEIGHT), BLACK)

        self.center_field = Line((START_FIELD_WIDHT + FIELD_WIDTH // 2, START_FIELD_HEIGHT), (START_FIELD_WIDHT + FIELD_WIDTH // 2, START_FIELD_HEIGHT + FIELD_HEIGHT), BLACK)

        self.top_gk_right_field = Line((START_FIELD_WIDHT + FIELD_WIDTH - FIELD_GK_WIDTH, START_FIELD_GK_HEIGHT), (START_FIELD_WIDHT + FIELD_WIDTH, START_FIELD_GK_HEIGHT), RED)
        self.bottom_gk_right_field = Line((START_FIELD_WIDHT + FIELD_WIDTH - FIELD_GK_WIDTH, START_FIELD_GK_HEIGHT + FIELD_GK_HEIGHT), (START_FIELD_WIDHT + FIELD_WIDTH, START_FIELD_GK_HEIGHT + FIELD_GK_HEIGHT), RED)
        self.gk_right_vertical = Line((START_FIELD_WIDHT + FIELD_WIDTH - FIELD_GK_WIDTH, START_FIELD_GK_HEIGHT), (START_FIELD_WIDHT + FIELD_WIDTH - FIELD_GK_WIDTH, START_FIELD_GK_HEIGHT + FIELD_GK_HEIGHT), BLACK)


    def draw_field(self):
        self.left_field.draw(self.screen)
        self.right_field.draw(self.screen)
        self.top_field.draw(self.screen)
        self.bottom_field.draw(self.screen)

        self.top_gk_left_field.draw(self.screen)
        self.bottom_gk_left_field.draw(self.screen)
        self.gk_left_vertical.draw(self.screen)

        self.center_field.draw(self.screen)
        self.center_circle = pygame.draw.circle(self.screen, BLACK, (START_FIELD_WIDHT + FIELD_WIDTH / 2, START_FIELD_HEIGHT + FIELD_HEIGHT / 2), 73, 2)
        
        self.top_gk_right_field.draw(self.screen)
        self.bottom_gk_right_field.draw(self.screen)
        self.gk_right_vertical.draw(self.screen)

    "== PLAYER =="
    
    def init_player(self):
        self.init_left_team()

    def init_left_team(self):
        self.left_team = []
        player1 = Player("Ah Tong", START_FIELD_WIDHT + 50, START_FIELD_HEIGHT + 50, 30, 30, RED)
        player2 = Player("Uncle Muhtu", START_FIELD_WIDHT + 100, START_FIELD_HEIGHT + 100, 50, 50, RED)
        self.left_team.append(player1)
        self.left_team.append(player2)
        
        # Assigning individual variables for each player
        self.player1 = player1
        self.player2 = player2
        for i, player in enumerate(self.left_team):
            setattr(self, f'player{i+1}', player)
        for i in range(3, 23):
            player = Player(f"Player {i}", START_FIELD_WIDHT + i * 50, START_FIELD_HEIGHT + i * 50, 50, 50, RED)
            self.left_team.append(player)
            setattr(self, f'player{i}', player)

    def draw_left_team(self):
        for player in self.left_team:
            player.draw(self.screen)

    "== GAMEPLAY =="
    def check_collision(self, ball_x, ball_y, ball_width, ball_height, player_x, player_y, player_width, player_height):
        """
        Check if two rectangles collide.

        Args:
            x1 (float): The x-coordinate of the top-left corner of the first rectangle.
            y1 (float): The y-coordinate of the top-left corner of the first rectangle.
            w1 (float): The width of the first rectangle.
            h1 (float): The height of the first rectangle.
            x2 (float): The x-coordinate of the top-left corner of the second rectangle.
            y2 (float): The y-coordinate of the top-left corner of the second rectangle.
            w2 (float): The width of the second rectangle.
            h2 (float): The height of the second rectangle.

        Returns:
            bool: True if the rectangles collide, False otherwise.
        """
        return (
            ball_x < player_x + player_width and 
            ball_x + ball_width > player_x and 
            ball_y < player_y + player_height and 
            ball_y + ball_height > player_y
        )

    def init_ball(self):
        self.ball = Ball(START_FIELD_WIDHT + FIELD_WIDTH / 2, START_FIELD_HEIGHT + FIELD_HEIGHT / 2)

    def draw_ball(self):
        self.ball.draw(self.screen)

    def update_ball(self):
        self.ball.ball_x += self.ball.speed_x
        self.ball.ball_y += self.ball.speed_y

        self.ball.speed_x *= self.ball.friction
        self.ball.speed_y *= self.ball.friction

        if abs(self.ball.speed_x) < abs(self.ball.speed_y):
            self.ball.speed_x = 0
            self.ball.speed_y = 0

        if self.ball.ball_x <= START_FIELD_WIDHT:
            self.ball.ball_x = START_FIELD_WIDHT
            self.ball.speed_x = -self.ball.speed_x
        if self.ball.ball_x + self.ball.width >= START_FIELD_WIDHT + FIELD_WIDTH:
            self.ball.ball_x = START_FIELD_WIDHT + FIELD_WIDTH - self.ball.width
            self.ball.speed_x = -self.ball.speed_x
        if self.ball.ball_y <= START_FIELD_HEIGHT:
            self.ball.ball_y = START_FIELD_HEIGHT
            self.ball.speed_y = -self.ball.speed_y
        if self.ball.ball_y + self.ball.height >= START_FIELD_HEIGHT + FIELD_HEIGHT:
            self.ball.ball_y = START_FIELD_HEIGHT + FIELD_HEIGHT - self.ball.height
            self.ball.speed_y = -self.ball.speed_y
    
    def run(self):
        while self.isRunning:
            self.screen.fill(WHITE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRunning = False

            self.draw_field()

            self.draw_ball()
            self.update_ball()

            self.draw_left_team()
            # print(START_FIELD_GK_HEIGHT)

            pygame.display.update()
            pygame.time.Clock().tick(60)


