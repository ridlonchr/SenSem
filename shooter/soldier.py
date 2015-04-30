# Christian Ridlon
# soldier.py
# will serve as a parent class for sniper, infantry, medic
from d20 import *
from random import randint

class Soldier_container(object):

    def __init__ (self):
        self.soldiers = {}
        self.player_count  = 0


    def add_to_dict(self, player):
        # add the player to the soldier dict

        self.player_count += 1
        self.player_number = int(self.player_count)
        self.soldiers[self.player_number] = player

    def print_dict(self):
        for player in sorted(self.soldiers.keys()):
            print "\n", player, self.soldiers[player].name

    def dict_len(self):
        return len(self.soldiers)

    def get_entry(self,index):
        return self.soldiers[index]

# attributes
class Soldier(object):

    def __init__(self, name):
        self.name = name
        self.alive = True

    def __str__(self):

        if self.alive:
            return "%s ( %i health, %i armor, %i shells)"%(self.name,self.hitpoints, self.armor, self.ammo)
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

    def __init__(self,name):
        Soldier.__init__(self,name)
        self.hitpoints = 10
        self.armor = 1
        self.strength = 1
        self.dexterity = 1
        self.constition = 1
        self.knowledge = 1
        self.luck = 1
        self.accuracy = 1
        self.ammo = 15

class Medic(Soldier):

    def __init__(self,name):
        Soldier.__init__(self,name)
        self.hitpoints = 10
        self.armor = 1
        self.strength = 1
        self.dexterity = 1
        self.constition = 1
        self.knowledge = 1
        self.luck = 1
        self.accuracy = 1
        self.ammo = 10

class Sniper(Soldier):

    def __init__(self,name):
        Soldier.__init__(self,name)
        self.hitpoints = 10
        self.armor = 1
        self.strength = 1
        self.dexterity = 1
        self.constition = 1
        self.knowledge = 1
        self.luck = 1
        self.accuracy = 1
        self.ammo = 7

"""
test
"""
# tests
if __name__ == '__main__':

    b = Soldier_container()

    a = Infantry("Christian")
    b.add_to_dict(a)


    a1 = Medic("Jeff")
    b.add_to_dict(a1)

    a2 = Sniper("Charles")
    b.add_to_dict(a2)

    aliveSoilders = b.dict_len()

    #print b.print_dict()

    while aliveSoilders > 1:


        print b.print_dict()


        first = int(raw_input("Who fires? "))
        second = int(raw_input("Who at? " ))


        #try:
        first_soilder = b.get_entry(first)
        print first_soilder
        second_soilder = b.get_entry(second)
        # catch friendly fire

        #except:
            #print "No such soilder exits!"
            #continue


        d20 = d20_Combat(b.get_entry(first),b.get_entry(second))
        print d20.total_attack
        print d20.total_defense
        print d20.damage




    for soilder in b.values():
        if soilder.alive:
            print b.soldiers.name, "is the winner!"
            break
