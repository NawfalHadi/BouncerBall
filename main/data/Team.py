import csv

from main.data.Player import Player

class Team():
    def __init__(self, id_team, name, nickname, color):
        self.id = id_team
        self.name = name
        self.nickname = nickname
        self.color = color