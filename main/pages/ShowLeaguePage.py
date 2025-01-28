import pygame
import csv

from main.constant.Size import *
from main.constant.Color import *

from main.ui.TextBox import TextBox

from main.data.Schedule import *
from main.data.Team import *



class ShowLeaguePage:
    def __init__(self, league_id=0):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    

        "== GAMEPLAY STATE =="
        self.isLoading = True
        self.isRunning = True

        "== DATA =="
        self.teams_list = self.load_teams(league_id)

        "== CURSOR TEAM STATE =="
        self.cursor_index = 0
        self.current_team = self.teams_list[self.cursor_index]

        "== DATA AFTER LOAD TEAM =="
        self.teams_schedule = self.load_schedule()
        print(len(self.teams_schedule))
        self.change_teams()

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
    
    def load_schedule(self):
        schedules = []
        with open(f'{self.schedule_path}', mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if int(row['home_team_id'] == self.current_team.id):
                    home = self.current_team
                    away = None
                    for team in self.teams_list:
                        if int(team.id) == int(row['away_team_id']):
                            away = team
                    
                    schedule = Schedule(
                        home, away,
                        row['home_score'],
                        row['away_score']
                    )
                    schedules.append(schedule)

                elif int(row['away_team_id'] == self.current_team.id):
                    home = None
                    away = self.current_team
                    for team in self.teams_list:
                        if int(team.id) == int(row['home_team_id']):
                            home = team
                    
                    schedule = Schedule(
                        home, away,
                        row['home_score'],
                        row['away_score']
                    )
                    schedules.append(schedule)
                    
        return schedules
    
    def change_teams(self):
        self.current_team = self.teams_list[self.cursor_index]
        self.teams_schedule = self.load_schedule()

        self.longest_team_name = self.check_team_name_letter()

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
        self.leaderboard_background = TextBox("", 50, 200, 500, 800, BLACK, WHITE)

    def draw_content_leaderboard(self):
        pass

    def draw_schedule(self):
        self.schedule_background = TextBox("", 600, 200, 1000, 800, RED, WHITE)

    def draw_content_schedule(self):
        self.team_a = self.teams_schedule[0]
        self.team_a.set_rectangle(
            self.schedule_background.rect.left + 20, 
            self.schedule_background.rect.top + 20, 
            750, 40, BLACK, WHITE, WHITE, BLACK)
        self.team_a.draw(self.screen, self.longest_team_name)

    def draw_background(self):
        self.leaderboard_background.draw(self.screen)
        self.schedule_background.draw(self.screen)

    "== FUNCTION =="
    def check_team_name_letter(self):
        font = pygame.font.Font(None, 36)
        max_width = 0

        for schedule in self.teams_schedule:
            text_surface = font.render(schedule.home_team.name, True, BLACK)
            text_width = text_surface.get_width()
            if text_width > max_width:
                max_width = text_width

        return max_width

    "== KEY INPUT =="
    def key_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if self.cursor_index > 0:
                pygame.time.wait(150)  # Add delay to slow down the key press
                self.cursor_index -= 1
                self.change_teams()
        elif keys[pygame.K_RIGHT]:
            if self.cursor_index < len(self.teams_list) - 1:
                pygame.time.wait(150)  # Add delay to slow down the key press
                self.cursor_index += 1
                self.change_teams()             

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

            self.draw_background()

            self.draw_content_schedule()
            
            pygame.display.update()