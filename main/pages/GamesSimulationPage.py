import pygame
import math

from main.constant.Size import *
from main.constant.Color import *
from main.constant.Position import *
from main.ui.Line import Line

from main.data.Ball import Ball
from main.data.Player import Player


class GamesSimulationPage:
    def __init__(self, left_team=None, right_team=None):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
        "== PAGE STATE =="
        self.isLoading = True
        self.isRunning = True
        
        "== GAMEPLAY STATE =="
        self.isFirstTouch = True

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
        self.init_player_blue()

    def init_player_blue(self):
        # plyr_x, plyr_y = START_FIELD_WIDHT, START_FIELD_HEIGHT + FIELD_HEIGHT // 2
        # self.player_blue = Player("Player Blue", plyr_x, plyr_y, 20, 20, BLUE, GK, "L")
        # self.player_blue.set_position()
        # self.players_blue = []

        self.players_blue = [
            Player("Player Blue 1", START_FIELD_WIDHT + 50, START_FIELD_HEIGHT + FIELD_HEIGHT // 2, 20, 20, BLUE, GK, "L"),
            Player("Player Blue 2", START_FIELD_WIDHT + 100, START_FIELD_HEIGHT + FIELD_HEIGHT // 3, 20, 20, BLUE, DF, "L"),
            Player("Player Blue 3", START_FIELD_WIDHT + 100, START_FIELD_HEIGHT + 2 * FIELD_HEIGHT // 3, 20, 20, BLUE, DF, "L"),
            Player("Player Blue 4", START_FIELD_WIDHT + 150, START_FIELD_HEIGHT + FIELD_HEIGHT // 4, 20, 20, BLUE, MF, "L"),
            Player("Player Blue 5", START_FIELD_WIDHT + 150, START_FIELD_HEIGHT + 3 * FIELD_HEIGHT // 4, 20, 20, BLUE, MF, "L"),
            Player("Player Blue 6", START_FIELD_WIDHT + 200, START_FIELD_HEIGHT + FIELD_HEIGHT // 2, 20, 20, BLUE, FW, "L"),
        ]

        for player in self.players_blue:
            player.set_position()


    def draw_player_blue(self):
        for player in self.players_blue:
            player.draw(self.screen)

        # self.player_blue.draw(self.screen)

    def update_player_blue(self):
        for player in self.players_blue:
            player.x += player.speed_x
            player.y += player.speed_y

        for player in self.players_blue:
            self.check_player_frame_collision(player)

        for i, player1 in enumerate(self.players_blue):
            for player2 in self.players_blue[i+1:]:
                if self.check_ball_player_collision(player1.x, player1.y, player1.width, player1.height, player2.x, player2.y, player2.width, player2.height):
                    player1.speed_x, player2.speed_x = player2.speed_x, player1.speed_x
                    player1.speed_y, player2.speed_y = player2.speed_y, player1.speed_y

        # collision check
        # self.check_gk_frame_collision(self.player_blue)

    "== BALL =="

    def init_ball(self):
        self.ball = Ball(START_FIELD_WIDHT + FIELD_WIDTH / 2, START_FIELD_HEIGHT + FIELD_HEIGHT / 2)

    def draw_ball(self):
        self.ball.draw(self.screen)

    def update_ball(self):
        if not self.isFirstTouch:
            self.ball.x += self.ball.speed_x
            self.ball.y += self.ball.speed_y
        else:
            self.ball.x += self.ball.speed_x

        self.ball.speed_x *= self.ball.friction
        self.ball.speed_y *= self.ball.friction

        if abs(self.ball.speed_x) < abs(self.ball.speed_y):
            self.ball.speed_x = 0
            self.ball.speed_y = 0

        self.check_ball_frame_collision()

        for player in self.players_blue:
            if self.check_ball_player_collision(self.ball.x, self.ball.y, self.ball.width, self.ball.height, player.x, player.y, player.width, player.height):
                self.isFirstTouch = False
                ball_center_x = self.ball.x + self.ball.width / 2
                player_center_x = player.x + player.width / 2

                relative_position = (ball_center_x - player_center_x) / (player.width / 2)

                self.ball.speed_x = relative_position * 7
                self.ball.speed_y = -7

   
    "== GAMEPLAY =="

    def check_ball_player_collision(self, ball_x, ball_y, ball_width, ball_height, player_x, player_y, player_width, player_height):
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

    def check_player_frame_collision(self, player):
        if player.x <= START_FIELD_WIDHT:
            player.x = START_FIELD_WIDHT
            player.speed_x = -player.speed_x
        if player.x + player.width >= START_FIELD_WIDHT + FIELD_WIDTH:
            player.x = START_FIELD_WIDHT + FIELD_WIDTH - player.width
            player.speed_x = -player.speed_x
        if player.y <= START_FIELD_HEIGHT:
            player.y = START_FIELD_HEIGHT
            player.speed_y = -player.speed_y
        if player.y + player.height >= START_FIELD_HEIGHT + FIELD_HEIGHT:
            player.y = START_FIELD_HEIGHT + FIELD_HEIGHT - player.height
            player.speed_y = -player.speed_y

    def check_gk_frame_collision(self, player):
        if player.side == "L":
            top = self.top_gk_left_field.get_rect().top
            left = self.left_field.get_rect().left
            right = self.gk_left_vertical.get_rect().left
            bottom = self.bottom_gk_left_field.get_rect().top

        elif player.side == "R":
            top = self.top_gk_right_field.get_rect().top
            left = self.gk_right_vertical.get_rect().left
            right = self.right_field.get_rect().left
            bottom = self.bottom_gk_right_field.get_rect().top
        
        if player.x <= left:
            player.x = left
            player.speed_x = -player.speed_x
        if player.x + player.width >= right:
            player.x = right - player.width
            player.speed_x = -player.speed_x
        if player.y <= top:
            player.y = top
            player.speed_y = -player.speed_y
        if player.y + player.height >= bottom:
            player.y = bottom - player.height
            player.speed_y = -player.speed_y

    def check_ball_frame_collision(self):
        if self.ball.x <= START_FIELD_WIDHT:
            self.ball.x = START_FIELD_WIDHT
            self.ball.speed_x = -self.ball.speed_x
        if self.ball.x + self.ball.width >= START_FIELD_WIDHT + FIELD_WIDTH:
            self.ball.x = START_FIELD_WIDHT + FIELD_WIDTH - self.ball.width
            self.ball.speed_x = -self.ball.speed_x
        if self.ball.y <= START_FIELD_HEIGHT:
            self.ball.y = START_FIELD_HEIGHT
            self.ball.speed_y = -self.ball.speed_y
        if self.ball.y + self.ball.height >= START_FIELD_HEIGHT + FIELD_HEIGHT:
            self.ball.y = START_FIELD_HEIGHT + FIELD_HEIGHT - self.ball.height
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

            self.draw_player_blue()
            self.update_player_blue()


            pygame.display.update()
            pygame.time.Clock().tick(60)


