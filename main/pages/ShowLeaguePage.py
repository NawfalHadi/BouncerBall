import pygame
import csv

from main.constant.Size import *
from main.constant.Color import *

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
        print(self.teams_list)

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

    def run(self):
        while self.isRunning:
            self.screen.fill(WHITE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRunning = False
            
            pygame.display.update()