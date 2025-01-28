import pygame
import csv

from main.constant.Size import *
from main.constant.Color import *

from main.ui.TextBox import TextBox

from main.data.Team import *



class ShowLeaguePage:
    def __init__(self, league_id=0):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    

        "== GAMEPLAY STATE =="
        self.isLoading = True
        self.isRunning = True

        "== DATA =="
        self.teams_list = self.load_teams(league_id)
        self.teams_schedule = None

        "== CURSOR TEAM STATE =="
        self.cursor_index = 0
        self.current_team = self.teams_list[self.cursor_index]

        "== INTERFACE =="
        self.text_explanation = "Press Left & Arrow To Check Another Teams Schedule"

    "== TEAMS =="
    def load_teams(self, id):
        self.schedule_path = None
        self.league_path = None

        with open('main/db/League.csv', mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if int(row['id']) == int(id):
                    self.schedule_path = row['schedule_path']
                    self.league_path = row['league_path']

        teams = []
        with open(f'{self.league_path}', mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                team = Team(
                    id_team=row['team_id'],
                    name=row['team_name'],
                    nickname=row['team_nickname'],
                    color=row['team_color']
                    )
                teams.append(team)
        return teams
    
    

    "== INTERFACE =="
    def draw_instruction(self):
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text_explanation, True, BLACK)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, START_FIELD_HEIGHT - 25))
        self.screen.blit(text_surface, text_rect)

    def draw_teams(self):
        font = pygame.font.Font(None, 64)
        text_surface = font.render(self.current_team.name, True, BLACK)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, START_FIELD_HEIGHT - 75))
        self.screen.blit(text_surface, text_rect)

    def draw_leaderboard(self):
        self.leaderboard_background = TextBox("", 50, 200, 500, 800, BLACK, WHITE).draw(self.screen)

    def draw_content_leaderboard(self):
        pass

    def draw_schedule(self):
        self.schedule_background = TextBox("", 600, 200, 1000, 800, RED, WHITE).draw(self.screen)

    def draw_content_schedule(self):
        pass

    "== KEY INPUT =="
    def key_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if self.cursor_index > 0:
                pygame.time.wait(150)  # Add delay to slow down the key press
                self.cursor_index -= 1
                self.current_team = self.teams_list[self.cursor_index]
        elif keys[pygame.K_RIGHT]:
            if self.cursor_index < len(self.teams_list) - 1:
                pygame.time.wait(150)  # Add delay to slow down the key press
                self.cursor_index += 1
                self.current_team = self.teams_list[self.cursor_index]

    def run(self):
        while self.isRunning:
            self.screen.fill(WHITE)

            self.key_input()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRunning = False

            self.draw_teams()
            self.draw_instruction()
            self.draw_leaderboard()
            self.draw_schedule()
            
            pygame.display.update()