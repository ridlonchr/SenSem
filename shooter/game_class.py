from soilder import *

class Game(object):

    def __init__(self):

        self.player_count = raw_input("How many people are playing? ")
        self.players = []
        self.soilders = {}

        for player in range(int(self.player_count)):
            self.players.append(Player())
            self.soilders[int(player+1)] = Soilder(self.players[player].name)




"""
class Player(object):

    def __init__(self):

        self.name = raw_input("What is the players name? ")
"""
