# Christian Ridlon
# soldier.py
# will serve as a parent class for sniper, infantry, medic

from random import randint

class Soldier_container(self):

    def __init__ (self):
        soldiers = {}
        player_count  = 0


    def add_to_dict(self, player):
        # add the player to the soldier dict

        player.player_count += 1
        self.player_number = int(player.player_count)
        #print self.player_number
        player.soldiers[self.player_number] = self.name

    def print_dict(self):
        for player in sorted(self.soldiers.keys()):
            print "\n", player, self.soldiers[player]

# attributes
class Soldier(object):

    def __init__(self, name):
        self.name = name
        self.hitpoints = 10
        self.armor = 1
        self.strength = 1
        self.dexterity = 1
        self.constition = 1
        self.knowledge = 1
        self.luck = 1
        self.accuracy = 1


    def __str__(self):

        if self.alive:
            return "%s ( %i health, %i armor, %i shells)"%(self.name,self.health, self.armor, self.ammo)
        else:
            return "%s (DEAD)"%self.name



#test
a = Soldier("Christian")
a.add_to_dict(a)
a.print_dict()
a1 = Soldier("Jeff")
a1.add_to_dict(a1)
a1.print_dict()
a2 = Soldier("Charles")
a2.add_to_dict(a2)
a2.print_dict()
