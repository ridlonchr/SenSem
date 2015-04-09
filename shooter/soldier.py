# Christian Ridlon
# soldier.py
# will serve as a parent class for sniper, infantry, medic

from random import randint

class Soldier_container(object):

    def __init__ (self):
        self.soldiers = {}
        self.player_count  = 0


    def add_to_dict(self, player):
        # add the player to the soldier dict

        player.player_count += 1
        self.player_number = int(player.player_count)
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

    def die(self):

        self.alive = False
        print self.name, "is down!"

    def reload(self):
        self.ammo = 15

    def attack(self, enemy):
        # will call the d20 attack system
        pass




class Infantry(Soldier):
    pass

class Medic(Soldier):
    pass
class Sniper(Soldier):
    pass


#test
b = Soldier_container()
a = Soldier("Christian")
b.add_to_dict(a)
#b.print_dict()
a1 = Soldier("Jeff")
b.add_to_dict(a1)
#a1.print_dict()
a2 = Soldier("Charles")
b.add_to_dict(a2)
b.print_dict()
